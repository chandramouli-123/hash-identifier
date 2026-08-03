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
    ),
    Rule(
        algorithm="Argon",
        detail="Argon - Side Channel Resistant variant",
        confidence=100,
        reason="Matches Prefix",
        prefix="$argon2i$",
    ),
    Rule(
        algorithm="Argon",
        detail="Argon Hybrid variant",
        confidence=100,
        reason="Matches Prefix",
        prefix="$argon2id$",
    ),
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
    ],
    96: [
        ("SHA-384", "384-bit member of the SHA-2 family, derived from SHA-512."),
    ],
    128: [
        ("SHA-512", "512-bit member of the SHA-2 family, optimized for 64-bit processors."),
        ("SHA3-512", "512-bit member of the SHA-3 family, based on the Keccak algorithm."),
        ("BLAKE2b-512", "High-speed 512-bit hash optimized for 64-bit platforms."),
    ],
}
