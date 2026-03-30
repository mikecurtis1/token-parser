import re

class TokenParser:
    def __init__(self):
        self.op_escape = '\\'
        self.op_prefix = ['+', '-', '|']
        self.op_index_separator = ':'
        self.op_phrase_quote = '"'
        self.op_token_delimiter = ' '
        self.token_delimiter_replacement = chr(31)
        self.tokens = []

    def tokenize(self, q=''):
        normalized = self.normalize_whitespace(q)
        tokenized = self.tokenize_quoted_phrases(normalized)
        self.set_tokens(tokenized)
        self.parse_tokens()
        self.clean_tokens_index()
        self.clean_tokens_text()
        return self.tokens

    def normalize_whitespace(self, string=''):
        string = re.sub(r'\s{2,}', ' ', string)
        return string.strip()

    def is_escaped(self, i, array):
        return self.count_escape_chars(i, array) % 2 != 0

    def count_escape_chars(self, i, array):
        pi = i - 1
        count = 0
        while pi >= 0 and array[pi] == self.op_escape:
            count += 1
            pi -= 1
        return count

    def tokenize_quoted_phrases(self, string):
        array = list(string)
        quoted = False

        for i, char in enumerate(array):
            if char == self.op_phrase_quote and not quoted and not self.is_escaped(i, array):
                quoted = True
            elif char == self.op_phrase_quote and quoted and not self.is_escaped(i, array):
                quoted = False

            if quoted and char == self.op_token_delimiter:
                array[i] = self.token_delimiter_replacement

        return ''.join(array)

    def set_tokens(self, string):
        parts = string.split(self.op_token_delimiter)
        self.tokens = [Token('', '', v, False) for v in parts]

    def update_token(self, i, prefix=None, index=None, text=None, phrase=False):
        if i < len(self.tokens):
            t = self.tokens[i]
            t.set_prefix(prefix)
            t.set_index(index)
            t.set_text(text)
            t.set_phrase(phrase)

    def parse_tokens(self):
        for i, token in enumerate(self.tokens):
            prefix, index, text, phrase = self.parse_token(token)
            self.update_token(i, prefix, index, text, phrase)

    def parse_token(self, token):
        string = token.get_text()
        prefix = self.get_token_prefix(string)
        index = self.get_token_index(string)
        text = self.get_token_text(string)
        phrase = self.get_token_phrase(text)
        return prefix, index, text, phrase

    def get_token_prefix(self, string):
        prefix = string[:1]
        return prefix if self.is_prefix_operator(prefix) else None

    def get_token_index(self, string):
        index, _ = self.split_on_index_op(string)
        return index

    def get_token_text(self, string):
        _, text = self.split_on_index_op(string)
        return text

    def get_token_phrase(self, text):
        return self.is_quoted_phrase(text)

    def is_prefix_operator(self, string):
        return string in self.op_prefix

    def is_quoted_phrase(self, string):
        return string.startswith(self.op_phrase_quote) and string.endswith(self.op_phrase_quote)

    def split_on_index_op(self, string):
        array = list(string)
        for i, char in enumerate(array):
            if char == self.op_index_separator and not self.is_escaped(i, array):
                return string[:i], string[i + 1:]
        return '', string

    def clean_tokens_index(self):
        for i, token in enumerate(self.tokens):
            index = token.get_index()
            index = self.remove_prefix_operators(index)
            index = self.remove_escape_chars(index)
            self.update_token(i, token.get_prefix(), index, token.get_text(), token.get_phrase())

    def clean_tokens_text(self):
        for i, token in enumerate(self.tokens):
            text = token.get_text()
            text = self.remove_prefix_operators(text)
            text = self.remove_token_delimiter_replacement(text)
            text = self.remove_phrase_quotes(text)
            text = self.remove_escape_chars(text)
            self.update_token(i, token.get_prefix(), token.get_index(), text, token.get_phrase())

    def remove_token_delimiter_replacement(self, string):
        return string.replace(self.token_delimiter_replacement, self.op_token_delimiter)

    def remove_prefix_operators(self, string):
        if string and self.is_prefix_operator(string[0]):
            return string[1:]
        return string

    def remove_phrase_quotes(self, string):
        if self.is_quoted_phrase(string):
            string = string[1:-1]
        return string.strip()

    def remove_escape_chars(self, string):
        array = list(string)
        result = []
        for i, char in enumerate(array):
            if char == self.op_escape and not self.is_escaped(i, array):
                continue
            result.append(char)
        return ''.join(result)
