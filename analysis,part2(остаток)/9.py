import numpy as np
import pandas as pd


def age_stat(df: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(df, values='Age', index=['Sex', 'Pclass'], aggfunc=np.median)


def main():
    print(age_stat(pd.read_csv('titanic_train.csv', index_col='PassengerId')))


if __name__ == "__main__":
    main()
