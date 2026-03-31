# Token Parser

A lightweight Python utility for parsing structured query strings into discrete tokens.
Originally developed as a PHP tokenizer, this project provides a Python implementation with both CLI-style parsing logic and an HTTP API via Flask.

---

## Features

* Parse structured query strings (e.g., fielded search syntax)
* Support for operators (`+`, `-`, quoted phrases, etc.)
* Simple Flask API endpoint
* Clean, modular Python package (`token_parser`)

---

## Project Structure

```
token-parser/
├─ app.py                  # Flask entry point
├─ token_parser/           # Core parsing package
│   ├─ __init__.py
│   ├─ parser.py           # TokenParser class
│   └─ token.py            # Token object
├─ README.md
```

---

## Requirements

* Python 3.x
* Flask

Install dependencies:

```bash
$ pip install flask
```

---

## Usage

### Start Flask Development Server

```bash
$ python3 app.py
```

You should see:

```
* Running on http://127.0.0.1:8080/
```

---

### Browser Request

```
http://localhost:8080/parse?q=su%3Alove+%2Bti%3Alife+-su%3A%22one+%2B+one%22
```

---

### Example Response

```json
[
  "su:love",
  "+ti:life",
  "-su:\"one + one\""
]
```

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

## Development Notes

* The Flask server (`app.py`) is intended for **development use only**
* It runs a local web server on port `8080`
* In production, this app should be served via a WSGI server (e.g., Apache + mod_wsgi or Gunicorn)

---

## Future Work

* Docker containerization
* Apache (mod_wsgi) deployment
* JSON-structured token output
* Expanded parsing rules and validation
* Test suite

---

## License

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

This project is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

---
