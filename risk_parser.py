import ply.yacc as yacc

from risk_lexer import RiskLexer


class RiskParser:
    def __init__(self):
        self._latest_tree = None

    tokens = RiskLexer.tokens
    precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'MULTIPLY'),
        ('right', 'UMINUS')
    )

    def p_statement(self, p):
        'statement : expression'
        self._latest_tree = p[1]

    def p_expression(self, p):
        '''
        expression : expression PLUS expression
                   | expression MINUS expression
        '''
        if p[2] == '-':
            p[0] = ('+', p[1], ('*', -1.0, p[3]))
        else:
            p[0] = (p[2], p[1], p[3])

    def p_expression_multiply(self, p):
        '''
        expression : INT MULTIPLY FACTOR
                   | FLOAT MULTIPLY FACTOR
        '''
        p[0] = ('*', p[1], p[3])

    def p_expression_uminus(self, p):
        'expression : MINUS expression %prec UMINUS'
        p[0] = ('*', -1.0, p[2])

    def p_expression_group(self, p):
        'expression : L_BRACKET expression R_BRACKET'
        p[0] = (p[2])

    def p_expression_number(self, p):
        '''
        expression : INT
                   | FLOAT
        '''
        p[0] = p[1]

    def p_expression_factor(self, p):
        'expression : FACTOR'
        p[0] = ('*', 1.0, p[1])

    def p_error(self, p):
        raise Exception(f'Syntax error at {p.value}')

    def build(self,  **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def get_parsed_tree(self, statement):
        self.parser.parse(statement)
        return self._latest_tree
