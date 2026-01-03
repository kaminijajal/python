#!/usr/bin/env python3
"""
wifi_strength.py
Simple passphrase strength checker for Wi-Fi passphrases you own.
"""
import math
import sys
import re

def estimate_entropy(password):
    # Estimate pool size:
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"[0-9]", password): pool += 10
    if re.search(r"[!@#\$%\^&\*\(\)_\-\+=\[\]\{\}\|\\:;\"'<>,\.\?/`~]", password): pool += 32
    # if none of the above, fallback to full ascii printable
    if pool == 0:
        pool = 95
    entropy = math.log2(pool) * len(password)
    return entropy

def score_password(pw):
    length = len(pw)
    entropy = estimate_entropy(pw)
    checks = {
        "length>=12": length >= 12,
        "has_lower": bool(re.search(r"[a-z]", pw)),
        "has_upper": bool(re.search(r"[A-Z]", pw)),
        "has_digit": bool(re.search(r"\d", pw)),
        "has_symbol": bool(re.search(r"[^\w\s]", pw)),
        "not_common_short": length >= 8
    }
    # basic score
    score = 0
    if checks["length>=12"]: score += 2
    elif checks["not_common_short"]: score += 1
    for k in ("has_lower","has_upper","has_digit","has_symbol"):
        if checks[k]: score += 1
    # classify
    if entropy >= 80 and score >= 6:
        strength = "Very strong"
    elif entropy >= 60 and score >= 4:
        strength = "Strong"
    elif entropy >= 40:
        strength = "Moderate"
    else:
        strength = "Weak"
    return {"password": pw, "length": length, "entropy_bits": round(entropy,1), "score": score, "strength": strength, "checks": checks}

def main():
    if len(sys.argv) >= 2:
        pw = sys.argv[1]
    else:
        pw = input("Enter the passphrase to check (it will not be stored): ").strip()
    result = score_password(pw)
    print("\nPassphrase analysis:")
    print(f" Length: {result['length']}")
    print(f" Entropy (bits): {result['entropy_bits']}")
    print(f" Score: {result['score']} / 8")
    print(f" Strength: {result['strength']}")
    print(" Checks:")
    for k,v in result["checks"].items():
        print(f"  - {k}: {'OK' if v else 'NO'}")
    print("\nRecommendations:")
    if result["strength"] in ("Weak","Moderate"):
        print(" - Use a longer passphrase (≥12 characters).")
        print(" - Mix upper/lower case, digits and symbols.")
        print(" - Prefer a long passphrase made of multiple random words (diceware style) or a random 16+ char string.")
    else:
        print(" - Your passphrase looks good. Keep it private and unique.")

if __name__ == "__main__":
    main()

