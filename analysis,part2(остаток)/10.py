import pandas as pd


def fename_stat(df: pd.DataFrame) -> pd.DataFrame:
    female = df.loc[df['Sex'] == 'female', 'Name']
    female = female.where(lambda e: e.str.split(',', expand=True)[1].str.startswith(' Miss.')).dropna()
    female = female.map(lambda e: e.split('Miss. ')[1].split(' ')[0])
    female = female.to_frame()  # созд DataFrame
    female = female['Name'].value_counts()
    female = female.reset_index(drop=False)  # новые столбцы
    female.rename(columns={'index': 'Name', 'Name': 'Popularity'}, inplace=True)  # присваивание имен для новых столб
    female = female.sort_values(by=['Popularity', 'Name'], ascending=[False, True])  # sort по популярности
    female = female.reset_index(drop=True)
    return female


def main():
    print(fename_stat(pd.read_csv('titanic_train.csv', index_col='PassengerId')))


if __name__ == "__main__":
    main()