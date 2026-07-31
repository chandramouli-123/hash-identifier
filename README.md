# Hash Identifier

A lightweight command-line tool written in Python that identifies possible hash algorithms using prefix detection and hexadecimal length heuristics.

> ⚠️ This tool provides **possible matches**, not guaranteed identification. Many hash algorithms share the same output length.

## Features

- Prefix-based detection
  - bcrypt (`$2b$`, `$2y$`)
  - Argon2 (`$argon2d$`, `$argon2i$`, `$argon2id$`)
- Hexadecimal validation
- Hash length detection
- Multiple candidate results
- Simple command-line interface

## Supported Algorithms

- bcrypt
- Argon2
- MD5
- NTLM
- MD4
- RIPEMD-128
- SHA-1
- RIPEMD-160
- SHA-256
- SHA3-256
- BLAKE2s-256
- SM3
- SHA-384
- SHA-512
- SHA3-512
- BLAKE2b-512

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/hash-identifier.git
cd hash-identifier
```

Create a virtual environment (optional):

```bash
python -m venv venv
```

Activate it:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Prefix example:

```bash
python hash_identifier.py '$2b$abcdefghijklmnopqrstuv'
```

Hexadecimal example:

```bash
python hash_identifier.py 5f4dcc3b5aa765d61d8327deb882cf99
```
## Documentation

- 📖 [Architecture](docs/architecture.md)

The architecture document explains the internal design, decision pipeline,
data-driven rule engine, and reasoning behind the implementation.

## Roadmap

- Rich table output
- More hash algorithms
- Better confidence scoring
- Unit tests
- Base64 and JWT detection
- Improved CLI

## License

This project is licensed under the MIT License.