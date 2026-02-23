# 🛡 Python Multi-Service Honeypot

## 📌 Overview
A modular Python honeypot framework supporting SSH and HTTP service emulation for intrusion detection, credential capture, and security analysis.

## 🚀 Features
- SSH Honeypot using Paramiko
- HTTP WordPress-style login honeypot using Flask
- Credential capture and logging
- Rotating log files
- Multi-threaded SSH handling
- CLI-based service selection

## 🛠 Technologies Used
- Python
- Flask
- Paramiko
- Socket Programming
- Logging

## ⚠ Before running SSH honeypot, generate a server key:
ssh-keygen -t rsa -b 2048 -f server.key

## 🔐 Run SSH Honeypot
python honeypy.py -a 0.0.0.0 -p 2223 -s

## 🌐 Run HTTP Honeypot
python honeypy.py -p 5000 -w

Then open:
http://localhost:5000

## 📂 Logs
- http_audits.log
- audits.log
- cmd_audits.log

📄 For further detials refer Full Documentation.