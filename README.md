# TBH-SubFinder

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-SubFinder/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-SubFinder/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/takeover-hints-orange.svg" alt="Takeover hints">
</p>

Subdomain brute-force enumerator with DNS resolution and **subdomain takeover hints**.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Does

- Expands a wordlist against the target domain (25+ built-in words)
- Resolves each candidate with DNS and reports live hosts + IP + status
- Flags CNAMEs pointing at dangling services (GitHub Pages, Heroku, S3-style) — takeover candidates, typically High severity
- Custom wordlist and thread control

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-SubFinder
cd TBH-SubFinder
pip install -r requirements.txt
```

## Usage

```
usage: subfinder.py [-h] -d DOMAIN [-w WORDLIST] [-t THREADS] [--json JSON]

options:
  -d, --domain DOMAIN   Target domain
  -w, --wordlist WORDLIST   Custom wordlist (one subdomain per line)
  -t, --threads THREADS     Concurrent lookups
  --json JSON               Save JSON
```

### Examples

```bash
python3 subfinder.py -d example.com
python3 subfinder.py -d example.com -w my-wordlist.txt -t 30 --json subs.json
```

## Sample Output

```
[*] example.com | 25 words | 10 threads
[FOUND] www.example.com -> 93.184.216.34 [200]
[FOUND] staging.example.com -> 185.199.108.153 [404]
  -> Cek manual CNAME staging.example.com - potensi takeover (High)

[✓] Found 2 | Takeover hints: 1
[✓] JSON: subs.json
```

A takeover hint needs manual confirmation: check the CNAME target's dashboard actually shows an unclaimed state before reporting.

## Authorized Use Only

Enumeration is noisy — only against bug bounty scopes that permit subdomain brute-forcing, or hosts you own. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-Recon](https://github.com/TulungagungBlackHat/TBH-Recon) — lighter subdomain pass inside full recon
- [TBH-DirFinder](https://github.com/TulungagungBlackHat/TBH-DirFinder) — path discovery on found hosts

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
