# Token Parser

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Docker](https://img.shields.io/badge/docker-29.2-blue.svg)](https://www.docker.com/)

A lightweight Python utility for parsing structured query strings into discrete tokens. This project is a Python port of the [original PHP Tokenizer](https://github.com/mikecurtis1/Tokenizer) and provides a modular `TokenParser` class for handling fielded search syntax and operators. It exposes an HTTP API via Flask, allowing web clients to submit queries and receive JSON-formatted tokenized results.

---

## Features

- Tokenizes input strings into structured `Token` objects.
- Handles:
  - Prefix operators (`+`, `-`, `|`)
  - Index separators (`:`)
  - Quoted phrases (`"..."`)
  - Escaped characters (`\`)
- Returns JSON with fields:
  - `prefix`
  - `index`
  - `text`
  - `phrase` (boolean)
- Ready for containerized deployment with Apache reverse proxy.

---

## Project Structure

```
token-parser/
├─ app/
│ ├─ app.py            ← Flask API entry point
│ ├─ token_parser/     ← Core parsing package
│ │ ├─ __init__.py
│ │ ├─ parser.py
│ │ └─ token.py
│ ├─ requirements.txt
│ └─ Dockerfile        ← Flask container
│
├─ apache/             ← Apache reverse proxy
│ ├─ proxy.conf
│ └─ Dockerfile        ← Apache container
│
├─ docker-compose.yml
```

---

## Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.11
- Git

---

### Local Development

1. Clone the repository:

```bash
git clone https://github.com/mikecurtis1/token-parser.git
```

---

## Docker Deployment

This project uses two containers:

* tokenizer_app → Flask API
* tokenizer_apache → Apache reverse proxy

### Build & Start Containers

From the root of the project:

```bash
docker-compose up --build
```

* Flask container is exposed internally on 8080.
* Apache container forwards external requests on 8085 → Flask API.

### Test the API

```Bash
curl http://localhost:8085/parse?q=su%3Alove+%2Bti%3Alife+-su%3A%22one+%2B+one%22
```

Expected output:

```
[
    {"prefix": "", "index": "su", "text": "love", "phrase": false},
    {"prefix": "+", "index": "ti", "text": "life", "phrase": false},
    {"prefix": "-", "index": "su", "text": "one + one", "phrase": true}
]
```

---

## Token Structure

Each token returned has the following elements:

| Field  | Type   | Description                                |
| ------ | ------ | ------------------------------------------ |
| prefix | string | Prefix operator if present (`+`, `-`, `\|`) |
| index  | string | Index portion of the token before `:`      |
| text   | string | The main token text                        |
| phrase | bool   | `True` if token was a quoted phrase        |


---

## Query Syntax Notes

The parser supports structured input such as:

```
su:love +ti:life -su:"one + one"
```

When sending via HTTP, special characters must be URL-encoded.

### Common Encodings

| Character | URL Encoded  |
| --------- | ------------ |
| `+`       | `%2B`        |
| `:`       | `%3A`        |
| `"`       | `%22`        |
| space     | `%20` or `+` |

> Note: `%2B` is required to preserve a literal `+` (otherwise it may be interpreted as a space).

---

## License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

---
