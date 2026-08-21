import pytest
import sys
from pathlib import Path

# Add the parent directory to sys.path to allow importing hash_identifier
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hash_identifier.detector import identify
from hash_identifier.models import HashCandidate


@pytest.mark.parametrize(
    "input_hash,expected_output",
    [
        # --- Edge Cases ---
        ("", []),  # Empty input
        ("g" * 32, []),  # Correct length (32) but invalid hex characters
        ("a" * 35, []),  # Correct characters but invalid length
        
        # --- Bcrypt Prefix Variants ---
        (
            "$2b$12$" + "a" * 53,
            [HashCandidate("bcrypt", "Current bcrypt variant", 100, "Matches Prefix")],
        ),
        (
            "$2y$12$" + "a" * 53,
            [HashCandidate("bcrypt", "Legacy bcrypt variant", 100, "Matches Prefix")],
        ),
        
        # --- Argon Variants (Length 96 matches your custom rules.py) ---
        (
            "$argon2d$" + "a" * 87,
            [HashCandidate("Argon", "Argon - GPU resistant variant", 100, "Matches Prefix")],
        ),
        (
            "$argon2i$" + "a" * 87,
            [HashCandidate("Argon", "Argon - Side Channel Resistant variant", 100, "Matches Prefix")],
        ),
        (
            "$argon2id$" + "a" * 86,
            [HashCandidate("Argon", "Argon Hybrid variant", 100, "Matches Prefix")],
        ),
        
        # --- Hex Length Rules (Lowercase) ---
        (
            "a" * 32,
            [
                HashCandidate("MD5", "128-bit message digest, widely used for file integrity but cryptographically broken.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("NTLM", "Microsoft Windows password hash based on the MD4 algorithm.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("MD4", "Fast 128-bit hash function, now considered cryptographically broken.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("RIPEMD-128", "128-bit member of the RIPEMD family, designed as an alternative to MD4/MD5.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 40,
            [
                HashCandidate("SHA-1", "160-bit Secure Hash Algorithm, deprecated due to collision attacks.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("RIPEMD-160", "160-bit cryptographic hash designed as an alternative to SHA-1.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 64,
            [
                HashCandidate("SHA-256", "256-bit member of the SHA-2 family, widely used and currently considered secure.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("SHA3-256", "256-bit member of the SHA-3 family, based on the Keccak sponge construction.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("BLAKE2s-256", "Fast 256-bit hash optimized for software and smaller systems.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("SM3", "256-bit Chinese national cryptographic hash standard.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("Keccak-256", "Original Keccak-256 Algorithm", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("BLAKE3-256", "Fast 256-bit hash optimized for software and smaller systems.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("Skein-256", "Fast 256-bit hash optimized for software and smaller systems.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("RIPEMD-256", "256-bit member of the RIPEMD family, designed as an alternative to SHA-1 and SHA-256.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("GOST-R 34.11-94", "256-bit Russian national cryptographic hash standard.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("GOST-R 34.11-2012", "256-bit Russian national cryptographic hash standard.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 96,
            [
                HashCandidate("SHA-384", "384-bit member of the SHA-2 family, derived from SHA-512.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 48,
            [
                HashCandidate("Tiger-192", "192-bit cryptographic hash function designed for efficiency on 64-bit platforms.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 56,
            [
                HashCandidate("SHA-224", "224-bit member of the SHA-2 family, derived from SHA-256.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("SHA3-224", "224-bit member of the SHA-3 family, based on the Keccak sponge construction.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 80,
            [
                HashCandidate("RIPEMD-320", "320-bit member of the RIPEMD family.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        (
            "a" * 128,
            [
                HashCandidate("SHA-512", "512-bit member of the SHA-2 family, optimized for 64-bit processors.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("SHA3-512", "512-bit member of the SHA-3 family, based on the Keccak algorithm.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("BLAKE2b-512", "High-speed 512-bit hash optimized for 64-bit platforms.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("Keccak-512", "Original Keccak-512 algorithm (pre-standardization version of SHA3-512).", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("Whirlpool", "512-bit cryptographic hash function based on a modified Advanced Encryption Standard (AES)", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("GOST-Streebog", "Streebog Russian national standard cryptographic hash function", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
        
        # --- Uppercase Hexadecimal Validation ---
        (
            "A" * 32,
            [
                HashCandidate("MD5", "128-bit message digest, widely used for file integrity but cryptographically broken.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("NTLM", "Microsoft Windows password hash based on the MD4 algorithm.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("MD4", "Fast 128-bit hash function, now considered cryptographically broken.", 50, "Length matches and contains only hexadecimal values"),
                HashCandidate("RIPEMD-128", "128-bit member of the RIPEMD family, designed as an alternative to MD4/MD5.", 50, "Length matches and contains only hexadecimal values"),
            ]
        ),
    ],
)
def test_identify(input_hash, expected_output):
    assert identify(input_hash) == expected_output