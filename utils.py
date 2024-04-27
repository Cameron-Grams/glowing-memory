"""
Helper functions for set creation

"""


def test_tuple(tup, df):
    output = []
    for i in tup:
        for j in tup:
            if df.loc[i, j] == True:
                output.append(True)
            else:
                output.append(False)
    if False in output:
        return False
    else:
        return True
         



def produce_sets(df):
    """
    Given a dataframe find the subsets in the dataframe
    """

    columns = df.columns
    value_tuples = df.apply(lambda x: list(zip(columns, x)), axis=1)

    groups = []

    for c in columns:
        row_match = sorted(value_tuples[c])
        for d in columns:
            row_subject = sorted(value_tuples[d])
            intr = set(row_match).intersection(set(row_subject))
            intr = [x[0] for x in intr if x[1] == True]
            intr = tuple(intr)
            if intr in groups:
                continue
            else:
                groups.append(intr)

    good_groups = [x for x in groups if test_tuple(x, df) == True]

    return good_groups
