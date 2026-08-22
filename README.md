# Hash Identifier

A lightweight command-line tool written in Python that identifies possible hash algorithms using prefix detection and hexadecimal length heuristics.

> ⚠️ This tool provides **possible matches**, not guaranteed identification. Many hash algorithms share the same output length.

## Features

- Prefix-based detection
  - bcrypt (`$2b$`, `$2y$`)
  - Argon2 (`$argon2d$`, `$argon2i$`, `$argon2id$`)
- Hexadecimal validation and length detection
- Multiple candidate results with confidence scoring
- Rich terminal table output
- **JSON output formatting (`--json` / `-j`)** for easy scripting and tool integration

## Supported Algorithms

- **bcrypt** (`$2b$`, `$2y$`)
- **Argon2** (`$argon2d$`, `$argon2i$`, `$argon2id$`)
- **Tiger-192**
- **SHA-224**, **SHA3-224**
- **MD5**, **NTLM**, **MD4**, **RIPEMD-128**
- **SHA-1**, **RIPEMD-160**
- **SHA-256**, **SHA3-256**, **BLAKE2s-256**, **SM3**, **Keccak-256**, **BLAKE3-256**, **Skein-256**, **RIPEMD-256**, **GOST-R 34.11-94**, **GOST-R 34.11-2012**
- **RIPEMD-320**
- **SHA-384**
- **SHA-512**, **SHA3-512**, **BLAKE2b-512**, **Keccak-512**, **Whirlpool**, **GOST-Streebog**

## Installation

Clone the repository:

```bash
git clone https://github.com/chandramouli-123/hash-identifier.git
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

### Standard Rich Table Output

Prefix match example:

```bash
hash-identifier '$2b$12$aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
```

Hexadecimal length match example:

```bash
hash-identifier 5f4dcc3b5aa765d61d8327deb882cf99
```

### JSON Output (`--json` / `-j`)

Output results directly as JSON formatted text:

```bash
hash-identifier --json 5f4dcc3b5aa765d61d8327deb882cf99
```

Save JSON output to a file using redirection:

```bash
hash-identifier --json 5f4dcc3b5aa765d61d8327deb882cf99 > results.json
```

Pipe JSON output into `jq` or another tool:

```bash
hash-identifier --json 5f4dcc3b5aa765d61d8327deb882cf99 | jq .candidates[0].algorithm
```

## Running Tests

Run the test suite using `pytest`:

```bash
pytest
```

## Documentation

- 📖 [Architecture](docs/architecture.md)

The architecture document explains the internal design, decision pipeline, data-driven rule engine, and reasoning behind the implementation.

## License

This project is licensed under the MIT License.
