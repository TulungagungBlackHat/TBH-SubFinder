# TBH-SubFinder v2.0 Pro - + Takeover Check

<p align="center"><img src="https://img.shields.io/badge/Version-v2.0%20Pro-red?style=for-the-badge"><img src="https://img.shields.io/badge/Pro-Takeover-green?style=for-the-badge"></p>

> **Pro** - Tambah deteksi potensi **subdomain takeover** (High severity bug bounty).

## ✨ v2.0 vs v1.0
- ✅ **Takeover Hint** - cek body `github.io`/`herokuapp`/`404 not found`

## 🚀 Usage
```bash
python3 subfinder.py -d example.com --json out.json
# [FOUND] test.example.com -> 1.2.3.4 [404] [TAKEOVER?]
```

## 🛡️ Bug Bounty
Takeover High severity - cek CNAME manual jika `[TAKEOVER?]`

## 👥 TBH
