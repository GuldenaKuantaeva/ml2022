import pandas as pd


def men_stat(df: pd.DataFrame) -> (float, float, float, float):
    df = df[(df['Survived']==0) & (df['Sex']=='male')]
    ages = df['Age']
    return (ages.mean(), ages.median(), ages.max(), ages.min())

df = pd.read_csv('titanic_train.csv', index_col='PassengerId')
men_stat(df)