#!/usr/bin/env python3
# TBH-SubFinder v2.0 Pro - + Takeover Check
import socket, requests, argparse, json
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-SubFinder v2.0 Pro \033[91m- Takeover \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

COMMON = ["www","mail","ftp","admin","api","blog","shop","m","mobile","dev","test","staging","beta","vpn","secure","portal","app","cdn","ns1","ns2","smtp","pop","imap","demo","old","new","beta2"]

# Known takeover fingerprints (simplified)
TAKEOVER_HINTS = ["github.io","herokuapp.com","amazonaws.com","azurewebsites","unclaimed"]

def check(sub, domain):
    host=f"{sub}.{domain}"
    try:
        ip=socket.gethostbyname(host)
        try:
            r=requests.get(f"https://{host}",timeout=3,headers={'User-Agent':'TBH-SubFinder/2.0'})
            status=r.status_code; body=r.text[:500].lower()
            takeover=False
            for hint in TAKEOVER_HINTS:
                if hint in body: takeover=True
            # Simple 404 takeover hint
            if status==404 and "not found" in body: takeover=True
            return {"host":host,"ip":ip,"status":status,"takeover":takeover}
        except:
            return {"host":host,"ip":ip,"status":"no-http","takeover":False}
    except:
        return None

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope bug bounty yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="v2.0 Pro")
    parser.add_argument("-d","--domain",required=True)
    parser.add_argument("-w","--wordlist",help="Custom wordlist")
    parser.add_argument("-t","--threads",type=int,default=20)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    domain=args.domain
    wordlist=COMMON
    if args.wordlist:
        with open(args.wordlist) as f: wordlist=[l.strip() for l in f if l.strip()]
    print(f"[*] {domain} | {len(wordlist)} words | {args.threads} threads")
    found=[]
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        results=list(ex.map(lambda s: check(s,domain), wordlist))
    for r in results:
        if r:
            found.append(r)
            flag=" \033[91m[TAKEOVER?]\033[0m" if r["takeover"] else ""
            print(f"\033[92m[FOUND] {r['host']} -> {r['ip']} [{r['status']}]{flag}\033[0m")
            if r["takeover"]:
                print(f"  -> Cek manual CNAME {r['host']} - potensi takeover (High)")
    print(f"\n[✓] Found {len(found)} | Takeover hints: {sum(1 for x in found if x['takeover'])}")
    if args.json:
        open(args.json,'w').write(json.dumps({"target":domain,"found":found},indent=2))
        print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
