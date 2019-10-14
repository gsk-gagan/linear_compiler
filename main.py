import pandas as pd
from sympy import simplify

import risk_lexer
import risk_parser


class RiskCompiler:
    def __init__(self, loadings_df, mappings_df):
        self.loadings_df = loadings_df      # ftag, iftag, loadings
        self.mappings_df = mappings_df      # ftag, mapping
        self._verify_mappings_df()
        self.mappings_df.set_index(keys='ftag', inplace=True)

        self.lexer = risk_lexer.RiskLexer()
        self.lexer.build()
        self.parser = risk_parser.RiskParser()
        self.parser.build()

    def _verify_mappings_df(self):
        if len(self.mappings_df) != len(self.mappings_df['ftag'].unique()):
            raise Exception('ERROR: 1-to-many mapping exist in mappings_df')

    # Expanded equations to non-mapped aladdin factors
    def expand_equation(self, eq):
        # Get all tokens using the lexer and keep on replacing each token with its expanded version
        factors = self.lexer.get_tokens(eq, type='FACTOR')
        factors_map = {}
        for factor in factors:
            if factor.value in self.mappings_df.index:
                factors_map[factor.value] = self.expand_equation(self.mappings_df.loc[factor.value]['mapping'])

        for factor in factors_map.keys():
            eq = eq.replace(factor, f'({factors_map[factor]})')

        return eq

    def _get_non_sparse_mapped_factors(self, eq):
        eq_factors = set([factor.value for factor in self.lexer.get_tokens(eq, type='FACTOR')])
        sparse_mapped_factors = set(self.loadings_df['ftag'])
        return eq_factors - sparse_mapped_factors

    def _get_sparse_loadings_from_expanded(self, eq):
        # Get the parsed tree from the equation
        abstract_syntactic_tree = self.parser.get_parsed_tree(eq)
        print(abstract_syntactic_tree)
        # Select the rows from loadings dataframe and operate

    def get_sparse_loadings(self, eq):
        exp_eq = self.expand_equation(eq)
        exp_eq = str(simplify(exp_eq)).replace(' ', '')
        unmapped_factors = self._get_non_sparse_mapped_factors(exp_eq)
        if len(unmapped_factors) != 0:
            raise Exception(f'Equation: {eq} expands to {exp_eq}, has unmapped factors: {unmapped_factors}')
        return self._get_sparse_loadings_from_expanded(exp_eq)


def main():
    inp = '(.1*FACTOR1+.2*FACTOR2-FACTOR3-FACTOR5)'
    inp = 'FACTOR1-FACTOR5'
    loadings_df = pd.read_csv('data/input/loadings.csv')
    mappings_df = pd.read_csv('data/input/factors_mapping.csv')

    risk_compiler = RiskCompiler(loadings_df, mappings_df)
    risk_compiler.get_sparse_loadings(inp)

    # import importlib
    # importlib.reload(risk_parser)

    # sim_eq = simplify('(.1*(10*(2*(4*FACTOR3)+3*(FACTOR4))+5*FACTOR3)+.2*(2*(4*FACTOR3)+3*(FACTOR4))-FACTOR3)')
    # str(sim_eq).replace(' ', '')

    # parser = risk_parser.RiskParser()
    # parser.build()
    #
    # x = parser.get_parsed_tree(inp)


if __name__ == '__main__':
    main()
