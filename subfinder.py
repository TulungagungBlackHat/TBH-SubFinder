#!/usr/bin/env python3
# TBH-SubFinder - Bug Bounty Subdomain Finder (Educational)
# Tulungagung Black Hat - uchil404 | Only Authorized Scope
import socket, requests, argparse, json
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-SubFinder \033[91m- Bug Bounty          \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

COMMON = ["www","mail","ftp","admin","api","blog","shop","m","mobile","dev","test","staging","beta","vpn","secure","portal","app","cdn","ns1","ns2","smtp","pop","imap","beta","demo"]

def check(sub, domain):
    host=f"{sub}.{domain}"
    try:
        ip=socket.gethostbyname(host)
        # Try HTTP check
        try:
            r=requests.get(f"https://{host}",timeout=3,headers={'User-Agent':'TBH-SubFinder/1.0'})
            status=r.status_code
        except:
            try: r=requests.get(f"http://{host}",timeout=3); status=r.status_code
            except: status="no-http"
        return {"host":host,"ip":ip,"status":status}
    except:
        return None

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope bug bounty yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="TBH-SubFinder - Bug Bounty")
    parser.add_argument("-d","--domain",required=True,help="Domain target (scope)")
    parser.add_argument("-w","--wordlist",help="Custom wordlist")
    parser.add_argument("-t","--threads",type=int,default=20)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    domain=args.domain
    wordlist=COMMON
    if args.wordlist:
        with open(args.wordlist) as f: wordlist=[l.strip() for l in f if l.strip()]
    print(f"[*] Target: {domain} | {len(wordlist)} subdomains | {args.threads} threads")
    found=[]
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        results=list(ex.map(lambda s: check(s,domain), wordlist))
    for r in results:
        if r:
            found.append(r)
            print(f"\033[92m[FOUND] {r['host']} -> {r['ip']} [{r['status']}]\033[0m")
    print(f"\n[✓] Found {len(found)} subdomains")
    print("-> Cek satu per satu untuk takeover / vuln, laporkan sesuai scope")
    if args.json:
        open(args.json,'w').write(json.dumps({"target":domain,"found":found},indent=2))
        print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
