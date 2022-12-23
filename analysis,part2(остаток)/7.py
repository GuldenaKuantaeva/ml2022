import numpy as np
import pandas as pd
import dateutil.relativedelta as relativedelta
import datetime
from pandas.testing import assert_frame_equal

rus_months = {
    'января': 1,
    'февраля' : 2,
    'марта' : 3,
    'апреля' : 4,
    'мая' : 5,
    'июня' : 6,
    'июля' : 7,
    'августа' : 8,
    'сентября' : 9,
    'октября' : 10,
    'ноября' : 11,
    'декабря' : 12
}


def parse_date(s_date: str) -> datetime:
    date = s_date.split(' ')
    return datetime.date(int(date[2]), rus_months[date[1]], int(date[0]))

def count_years(df):
    return relativedelta.relativedelta(parse_date(df['Дата смерти']), parse_date(df['Дата рождения'])).years

def rus_feature(df: pd.DataFrame) -> pd.DataFrame:
    df['Полных лет'] = df.apply(lambda data: count_years(data), axis=1)
    return df


######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                      'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                      'Дата смерти': ['7 января 1943 г.', '18 апреля 1955 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла', 'Альберт Эйнштейн'],
                       'Дата рождения': ['10 июля 1856 г.', '14 марта 1879 г.'],
                       'Дата смерти': ['7 января 1943 г.', '18 апреля 1955 г.'],
                       'Полных лет': [86, 76]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['10 июля 1856 г.'],
                      'Дата смерти': ['7 января 1857 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['10 июля 1856 г.'],
                       'Дата смерти': ['7 января 1857 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)
######################################################
names = pd.DataFrame({'Имя': ['Никола Тесла'],
                      'Дата рождения': ['1 января 2000 г.'],
                      'Дата смерти': ['31 декабря 2000 г.']})
answer = pd.DataFrame({'Имя': ['Никола Тесла'],
                       'Дата рождения': ['1 января 2000 г.'],
                       'Дата смерти': ['31 декабря 2000 г.'],
                       'Полных лет': [0]})
assert_frame_equal(
    rus_feature(names),
    answer
)
