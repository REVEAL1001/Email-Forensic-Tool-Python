import tkinter as tk
from tkinter import filedialog, scrolledtext
from email import policy
from email.parser import BytesParser
import re

def extract_ip(headers):
    received = headers.get_all('Received', [])
    for line in received:
        match = re.search(r'\[([\d\.]+)\]', line)
        if match:
            return match.group(1)
    return "N/A"

def detect_provider(headers):
    received = headers.get_all('Received', [])
    for line in received:
        if 'google.com' in line:
            return "Gmail (Google)"
        elif 'outlook.com' in line or 'hotmail.com' in line:
            return "Outlook (Microsoft)"
        elif 'yahoo.com' in line:
            return "Yahoo"
    return "Unknown"

def spoof_detect(spf, dkim, dmarc):
    if 'pass' in spf.lower() and 'pass' in dkim.lower() and 'pass' in dmarc.lower():
        return "No spoofing detected ✅"
    else:
        return "⚠️ Potential spoofing attempt!"

def apply_tagged_output(tag, label, value):
    output_text.insert(tk.END, f"{label}: ", tag)
    output_text.insert(tk.END, f"{value}\n", "value")

def load_eml_file():
    file_path = filedialog.askopenfilename(filetypes=[("EML files", "*.eml")])
    if not file_path:
        return

    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    headers = msg

    # Clear previous output
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)

    # Extract fields
    message_id = headers.get('Message-ID', 'N/A')
    spf = headers.get('Received-SPF', 'N/A')
    dkim = headers.get('Authentication-Results', '')
    dkim_match = re.search(r'dkim=(\w+)', dkim)
    dkim = dkim_match.group(1) if dkim_match else "N/A"
    dmarc_match = re.search(r'dmarc=(\w+)', headers.get('Authentication-Results', ''))
    dmarc = dmarc_match.group(1) if dmarc_match else "N/A"
    ip = extract_ip(headers)
    provider = detect_provider(headers)
    content_type = headers.get_content_type()
    date = headers.get('Date', 'N/A')
    subject = headers.get('Subject', 'N/A')
    spoof_status = spoof_detect(spf, dkim, dmarc)

    # Print output with tags
    apply_tagged_output("section", "Message-ID", message_id)
    apply_tagged_output("section", "SPF Record", spf)
    apply_tagged_output("section", "DKIM Record", dkim)
    apply_tagged_output("section", "DMARC Record", dmarc)
    apply_tagged_output("section", "Spoofed Email Check", spoof_status)
    apply_tagged_output("section", "Sender IP Address", ip)
    apply_tagged_output("section", "Service Provider", provider)
    apply_tagged_output("section", "Content-Type", content_type)
    apply_tagged_output("section", "Date and Time", date)
    apply_tagged_output("section", "Subject", subject)

    output_text.config(state=tk.DISABLED)

# GUI Setup
root = tk.Tk()
root.title("Email Analyzer - Digital Forensics")
root.geometry("800x600")
root.config(bg="#f5f5f5")

tk.Label(root, text="Email Forensic Analyzer", font=("Helvetica", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

tk.Button(root, text="Open .eml File", command=load_eml_file, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30, font=("Courier", 10))
output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Color tags
output_text.tag_configure("section", foreground="#007ACC", font=("Courier", 10, "bold"))
output_text.tag_configure("value", foreground="#444")

output_text.config(state=tk.DISABLED)

root.mainloop()
