from flask import Flask, request, jsonify

from token_parser import TokenParser

app = Flask(__name__)

@app.route('/parse', methods=['GET'])
def parse():
    # Get 'q' from query string, default to empty string
    q = request.args.get('q', '')

    tokenizer = TokenParser()
    tokens = tokenizer.tokenize(q)

    # Convert tokens to something JSON-serializable if needed
    # (assuming Token has a __str__ or simple structure)
    return jsonify([str(t) for t in tokens])


if __name__ == "__main__":
    app.run(port=8085, debug=True)
