"""
Hash Identifier
Version: 0.1.0

Author: Chandra Mouli Baskaran

A lightweight CLI tool for identifying possible hash algorithms
using prefix detection and hexadecimal length heuristics.
"""

import argparse
from dataclasses import dataclass

@dataclass
class HashCandidate:
    algorithm : str
    detail : str
    confidence : str
    reason : str



PREFIX_RULES = [
    ("$2b$","bcrypt","Current bcrypt variant"),
    ("$2y$","bcrypt","Legacy bcrypt variant"),
    ("$argon2d$","Argon","Argon - GPU resistant variant"),
    ("$argon2i$","Argon","Argon - Side Channel Resistant variant"),
    ("$argon2id$","Argon","Argon Hybrid variant"),
]

HEX_LENGTH_RULES = {
    32  : [
        ("MD5","128-bit message digest, widely used for file integrity but cryptographically broken."),
        ("NTLM","Microsoft Windows password hash based on the MD4 algorithm."),
        ("MD4","Fast 128-bit hash function, now considered cryptographically broken."),
        ("RIPEMD-128","128-bit member of the RIPEMD family, designed as an alternative to MD4/MD5.")
    ],
    40  : [
        ("SHA-1","160-bit Secure Hash Algorithm, deprecated due to collision attacks."),
        ("RIPEMD-160","160-bit cryptographic hash designed as an alternative to SHA-1.")
    ],
    64  : [
        ("SHA-256","256-bit member of the SHA-2 family, widely used and currently considered secure.")
        ("SHA3-256", "256-bit member of the SHA-3 family, based on the Keccak sponge construction.")
        ("BLACKE2s-256", "Fast 256-bit hash optimized for software and smaller systems.")
        ("SM3","256-bit Chinese national cryptographic hash standard.")
    ],
    96  : [
        ("SHA-384","384-bit member of the SHA-2 family, derived from SHA-512.")
    ],
    128 : [
        ("SHA-512","512-bit member of the SHA-2 family, optimized for 64-bit processors."),
        ("SHA3-512","512-bit member of the SHA-3 family, based on the Keccak algorithm."),
        ("BLAKE2b-512","High-speed 512-bit hash optimized for 64-bit platforms.")
    ]
}


def _is_hex(text):
    hexchars = {
    '0','1','2','3','4','5','6','7','8','9',
    'a','b','c','d','e','f',
    'A','B','C','D','E','F'
    }
    for i in text:
        if i not in hexchars:
            return False
    return True

def identify(text):   
    result = []

    for prefix,algorithm,detail in PREFIX_RULES:
        if text.startswith(prefix):
            return [HashCandidate(algorithm,detail,"High","Matches Prefix")]
        
    hash_len = len(text)

    if _is_hex(text):
        if hash_len in HEX_LENGTH_RULES:
            for algo,detail in HEX_LENGTH_RULES[hash_len]:
                result.append(HashCandidate(algo,detail,"Possibility: Medium","Length Matches and contains only hexadecimal values")) 
    return result


def main():
# get input -> parse it -> call identify ->print result
    parser = argparse.ArgumentParser()
    parser.add_argument("hashval")
    args = parser.parse_args()
    print("The entered hash is "+ args.hashval)

    candidate = identify(args.hashval.strip())
    if len(candidate)!=0:
        for i in candidate:
            print(i)
    else:
        print("No matching algorithms found")


if __name__ == "__main__":
    main()