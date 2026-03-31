from flask import Flask, request, jsonify

from token_parser import TokenParser

app = Flask(__name__)

@app.route('/parse', methods=['GET'])
def parse():
    # Get 'q' from query string, default to empty string
    q = request.args.get('q', '')

    tokenizer = TokenParser()
    tokens = tokenizer.tokenize(q)

    return jsonify([
        {
            "prefix": t.get_prefix(),
            "index": t.get_index(),
            "text": t.get_text(),
            "phrase": t.get_phrase()
        }
        for t in tokens
    ])

if __name__ == "__main__":
    app.run(port=8080, debug=False)
