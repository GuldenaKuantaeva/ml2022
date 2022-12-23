import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal


def ZOOtable(zoo: dict) -> pd.DataFrame:
    table = pd.DataFrame.from_dict(zoo, orient='index')
    table.reset_index(drop=True, inplace=True)
    table.insert(loc=0, column='Type', value=np.array(zoo.keys()))
    table = table.loc[:, table.notna().all(axis=0)]  # только с непропущенными
    table.sort_values(by=['Type'])
    new_columns = list(table.columns)
    new_columns[1:] = sorted(new_columns[1:])  #  первый столб -> sort остальных
    table = table.reindex(new_columns, axis=1)
    #табл с новыми столбцами, которые уже sort
    return table


def main():
    ######################################################
    ZOO = {
        'cat': {'color': 'black', 'tail_len': 50.0, 'injured': False},
        'dog': {'age': 6, 'tail_len': 30.5, 'injured': True}
    }
    answer = pd.DataFrame(
        {
            'Type': ['cat', 'dog'],
            'injured': [False, True],
            'tail_len': [50.0, 30.5]
        }
    )
    df = ZOOtable(ZOO)

    assert_frame_equal(
        df.reset_index(drop=True),
        answer
    )
    ######################################################
    ZOO = {
        'cat': {'color': 'black'},
        'dog': {'age': 6}
    }
    answer = pd.DataFrame(
        {
            'Type': ['cat', 'dog']
        }
    )

    df = ZOOtable(ZOO)

    assert_frame_equal(
        df.reset_index(drop=True),
        answer
    )
    ######################################################


if __name__ == "__main__":
    main()