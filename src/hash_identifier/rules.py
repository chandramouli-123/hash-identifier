from .models import Rule

PREFIX_RULES = [
    Rule(
        algorithm="bcrypt",
        detail="Current bcrypt variant",
        confidence=100,
        reason="Matches Prefix",
        regex=r"\$2b\$[0-9]{2}\$[A-Za-z0-9./]{53}",
        prefix="$2b$",
        length=60,
    ),
    Rule(
        algorithm="bcrypt",
        detail="Legacy bcrypt variant",
        confidence=100,
        reason="Matches Prefix",
        regex=r"\$2y\$[0-9]{2}\$[A-Za-z0-9./]{53}",
        prefix="$2y$",
        length=60,
    ),
    Rule(
        algorithm="Argon",
        detail="Argon - GPU resistant variant",
        confidence=100,
        reason="Matches Prefix",
        prefix="$argon2d$",
        length=96
    ),
    Rule(
        algorithm="Argon",
        detail="Argon - Side Channel Resistant variant",
        confidence=100,
        reason="Matches Prefix",
        prefix="$argon2i$",
        length=96
    ),
    Rule(
        algorithm="Argon",
        detail="Argon Hybrid variant",
        confidence=100,
        reason="Matches Prefix",
        prefix="$argon2id$",
        length=96
    )
]

HEX_LENGTH_RULES = {
    32: [
        ("MD5", "128-bit message digest, widely used for file integrity but cryptographically broken."),
        ("NTLM", "Microsoft Windows password hash based on the MD4 algorithm."),
        ("MD4", "Fast 128-bit hash function, now considered cryptographically broken."),
        ("RIPEMD-128", "128-bit member of the RIPEMD family, designed as an alternative to MD4/MD5."),
    ],
    40: [
        ("SHA-1", "160-bit Secure Hash Algorithm, deprecated due to collision attacks."),
        ("RIPEMD-160", "160-bit cryptographic hash designed as an alternative to SHA-1."),
    ],
    64: [
        ("SHA-256", "256-bit member of the SHA-2 family, widely used and currently considered secure."),
        ("SHA3-256", "256-bit member of the SHA-3 family, based on the Keccak sponge construction."),
        ("BLAKE2s-256", "Fast 256-bit hash optimized for software and smaller systems."),
        ("SM3", "256-bit Chinese national cryptographic hash standard."),
        ("Keccak-256","Original Keccak-256 Algorithm"),
        ("BLAKE3-256", "Fast 256-bit hash optimized for software and smaller systems."),
        ("Skein-256", "Fast 256-bit hash optimized for software and smaller systems."),
        ("RIPEMD-256", "256-bit member of the RIPEMD family, designed as an alternative to SHA-1 and SHA-256."),
        ("GOST-R 34.11-94", "256-bit Russian national cryptographic hash standard."),
        ("GOST-R 34.11-2012", "256-bit Russian national cryptographic hash standard."),
    ],
    96: [
        ("SHA-384", "384-bit member of the SHA-2 family, derived from SHA-512."),
    ],
    128: [
        ("SHA-512", "512-bit member of the SHA-2 family, optimized for 64-bit processors."),
        ("SHA3-512", "512-bit member of the SHA-3 family, based on the Keccak algorithm."),
        ("BLAKE2b-512", "High-speed 512-bit hash optimized for 64-bit platforms."),
        ("Keccak-512","Original Keccak-512 algorithm (pre-standardization version of SHA3-512)."),
        ("Whirlpool","512-bit cryptographic hash function based on a modified Advanced Encryption Standard (AES)"),
        ("GOST-Streebog","Streebog Russian national standard cryptographic hash function")
    ],
    48: [
        ("Tiger-192", "192-bit cryptographic hash function designed for efficiency on 64-bit platforms.")
    ],
    56: [
        ("SHA-224", "224-bit member of the SHA-2 family, derived from SHA-256."),
        ("SHA3-224", "224-bit member of the SHA-3 family, based on the Keccak sponge construction."),
    ],
    80: [
        ("RIPEMD-320", "320-bit member of the RIPEMD family."),
    ],
}
