
### ✅ **Corrected Version**

Here's a corrected version of your `README.md` content with **proper code block usage**:

````markdown
# 🛠️ KeyWatch – Advanced Keystroke Logger

**KeyWatch** is an advanced keylogger tool that records every keystroke made by a user and includes additional features like screen capturing and periodic email reporting.

> ⚠️ **DISCLAIMER**: This project is for **educational and ethical security research purposes only**. Do **NOT** use it for malicious or unauthorized monitoring. Unauthorized keylogging is illegal in many countries.

---

## 📌 Features

- ✅ Records all keystrokes, including special keys (e.g., Enter, Tab, Space)
- 🖼️ Captures a screenshot each time the Enter key is pressed
- 📧 Sends logs and screenshots via email
- 🧾 Saves logs locally to a file
- ⏱️ Sends reports at user-defined intervals

---

## 📦 Requirements

- Python 3.6 or later
- Third-party libraries:
  - `pynput`
  - `mss`

Install the required packages using:

```bash
pip install -r requirements.txt
````

---

## ⚙️ How to Use

### 1. Configure Email

For Gmail:

* Enable “Allow less secure apps” OR
* Use an **App Password** if 2FA is enabled.

### 2. Setup Configuration

In `startup.py`, modify the values:

```python
kelogger = Kelogger(
    time_interval=60,  # seconds between reports
    email="your_email@gmail.com",
    password="your_email_password",
    LOG_FILE_PATH="log.txt"
)
kelogger.start()
```

### 3. Run the Program

```bash
python startup.py
```

---

## 📁 Project Structure

```
KeyWatch/
│
├── config.py
├── encryption.py
├── logger.py
├── main.py
├── startup.py
├── requirements.txt
├── logs/
├── __pycache__/
└── screenshots/
```

---

## 📧 Email Report Example

* Subject: `Keylogger Report - 2025-05-23 16:45`
* Body: Contains timestamped key logs
* Attachment: Screenshot of the user's screen

---

## ⚠️ Legal Warning

> This software **must not** be used to monitor or log activity on any system or user **without full and explicit consent**.
> Any unauthorized use may be **a violation of privacy laws** and can result in **criminal charges**.
> The author is **not responsible** for any misuse of this software.

---

## 👨‍💻 Author

* **Name**: Mohammed Bakkali
* **Website**: [mohammed-bakkali.netlify.app](https://mohammed-bakkali.netlify.app)

```


