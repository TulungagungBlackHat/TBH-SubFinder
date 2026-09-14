# TBH-SubFinder - Bug Bounty Subdomain Finder

<p align="center">
  <img src="https://img.shields.io/badge/Bug%20Bounty-SubFinder-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Threads-20-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Scope-Only%20Authorized-green?style=for-the-badge">
</p>

> **Hanya untuk scope bug bounty yang diizinkan.**

## ✨ Features
- 🔍 25 subdomains umum + custom wordlist
- ⚡ 20 threads
- 🌐 HTTP status check
- 📄 JSON export

## 🚀 Usage
```bash
git clone https://github.com/TulungagungBlackHat/TBH-SubFinder
cd TBH-SubFinder
python3 subfinder.py -d example.com --json out.json

# Custom wordlist
python3 subfinder.py -d example.com -w wordlist.txt --json out.json
```

## 🛡️ Bug Bounty Tips
- Subdomain `test`, `staging`, `dev` sering vulnerable
- Cek takeover (CNAME)

## 👥 TBH
uchil404 - Tulungagung Black Hat

## 📄 License
MIT
