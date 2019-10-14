import pandas as pd


class EvaluateAbstractSyntacticTree:
    def __init__(self, loadings_df):
        self.loadings_df = loadings_df

    def get_df(self, factor):
        factor_df = self.loadings_df.loc[self.loadings_df.ftag == factor][['iftag', 'loading']].set_index(keys='iftag')
        return factor_df

    # NOTE: The parser guaranties:  1.) MULTIPLY happens between NUMBER {INT, FLOAT} and FACTOR (Terminals)
    #                               2.) ADD happens between evaluated FACTORS (Non-terminals)
    def eval(self, tree):
        if tree[0] == '*':
            return tree[1]*self.get_df(tree[2])

        # '+' case
        left_df = self.eval(tree[1])
        right_df = self.eval(tree[2])
        combined_df = pd.merge(left=left_df, right=right_df, how='outer',
                               left_index=True, right_index=True).fillna(0.0).sum(axis=1).to_frame()
        combined_df.columns = ['iftag']
        return combined_df
