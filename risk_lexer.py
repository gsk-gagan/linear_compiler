import ply.lex as lex


class RiskLexer:
    tokens = [
        'INT',
        'FLOAT',
        'PLUS',
        'MINUS',
        'MULTIPLY',
        'L_BRACKET',
        'R_BRACKET',
        'FACTOR'
    ]

    t_PLUS = r'\+'
    t_MINUS = r'\-'
    t_MULTIPLY = r'\*'

    t_L_BRACKET = r'\('
    t_R_BRACKET = r'\)'

    t_ignore = r'[ =@]'

    def t_FLOAT(self, t):
        r'\d*\.\d+'
        t.value = float(t.value)
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_FACTOR(self, t):
        r'[a-zA-Z0-9_]+'
        t.type = 'FACTOR'
        return t

    # Error handling rule
    def t_error(self, t):
        raise Exception("Illegal character '%s'" % t.value[0])
        # t.lexer.skip(1)           # This should be used if we aren't raising exception on illegal character

    # Build the lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Get tokens of specific type
    def get_tokens(self, data, type=None):
        tokens = []
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            if type is not None and tok.type != type:
                continue
            tokens.append(tok)
        return tokens

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
