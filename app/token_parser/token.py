class Token:
    def __init__(self, prefix='', index='', text='', phrase=False):
        self.set_prefix(prefix)
        self.set_index(index)
        self.set_text(text)
        self.set_phrase(phrase)

    def set_prefix(self, value):
        self.prefix = value if isinstance(value, str) else ''

    def set_index(self, value):
        self.index = value if isinstance(value, str) else ''

    def set_text(self, value):
        self.text = value if isinstance(value, str) else ''

    def set_phrase(self, value):
        self.phrase = value if isinstance(value, bool) else False

    def get_prefix(self):
        return self.prefix

    def get_index(self):
        return self.index

    def get_text(self):
        return self.text

    def get_phrase(self):
        return self.phrase

    def __repr__(self):
        return f"Token(prefix={self.prefix!r}, index={self.index!r}, text={self.text!r}, phrase={self.phrase})"
