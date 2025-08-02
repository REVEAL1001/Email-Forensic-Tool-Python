# 🕵️‍♂️ Email Forensic Analyzer (GUI, Python)

**Email Forensic Analyzer** is a GUI-based Python tool built with `tkinter` that allows users to inspect `.eml` files for forensic indicators. The tool parses key headers to determine whether the email might be spoofed and extracts useful metadata like SPF/DKIM/DMARC records, sender IP address, provider info, and more — all without needing to understand raw EML format.

## 🧠 Key Features

- ✅ Detects potential **email spoofing** using SPF, DKIM, and DMARC
- 🌐 Extracts **sender IP address**
- 🔍 Identifies **email service provider** (Gmail, Outlook, Yahoo, etc.)
- 🧾 Displays important email metadata:
  - Message-ID
  - Subject
  - Content-Type
  - Date and Time
- 📂 Easy `.eml` file picker and scrolling output
- 🖥️ GUI built using Python's `tkinter` — beginner friendly!

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/REVEAL1001/Email-Forensic-Tool-Python.git
cd Email-Forensic-Tool-Python
```

2. **Install Dependencies**

No external libraries required — only Python's standard libraries are used.  
Ensure you have **Python 3.6+** installed.

## 🚀 Usage

1. Place your `.eml` files somewhere accessible.

2. Run the tool:

```bash
python main.py
```

3. A GUI window will open:
   - Click **"Open .eml File"**
   - Select an email file
   - View the parsed forensic output

## 🧪 Example Output

```
Message-ID: <1234@mail.example.com>
SPF Record: pass (google.com: domain of user@example.com designates ...)
DKIM Record: pass
DMARC Record: pass
Spoofed Email Check: No spoofing detected ✅
Sender IP Address: 198.51.100.1
Service Provider: Gmail (Google)
Content-Type: text/plain
Date and Time: Thu, 01 Aug 2025 10:30:00 -0700
Subject: Important Security Alert
```

## 🤝 Contributing

Have an idea or improvement? Feel free to fork and submit a pull request.  
All suggestions are welcome.

## 🛡️ License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author
**Sambardhan Khanal**  
[R3VEAL1001](https://github.com/REVEAL1001)
