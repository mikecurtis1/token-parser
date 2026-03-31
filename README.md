# token-parser

## Usage

### Start Flask dev server

```bash
$ python3 app.py
```

### Browser request

```
http://localhost:8080/parse?q=su%3Alove+%2Bti%3Alife+-su%3A%22one+%2B+one%22
```

URL encoding for query operators

| char    | URL encoded |
| ------- | ----------- |
| +       | %2B         |
| :       | %3A         |
| "       | %22         |
| <space> | %20         |
