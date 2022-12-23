from pandas.io.parsers.base_parser import isna
import numpy as np

def replace_nans(X:np.ndarray) -> np.ndarray:
    return np.where(np.isnan(X), np.ma.array(X, mask=np.isnan(X)).mean(axis=0), X)
from numpy.testing import assert_array_equal, assert_array_almost_equal
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [np.nan],  [np.nan]])),
    np.array([[0. ],[ 0. ],[ 0. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[0, 42,  42]])),
    np.array([[0, 42 , 42]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan], [1], [np.nan]])),
    np.array([[1.] ,[ 1.] ,[ 1. ]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[4], [1],  [np.nan]])),
    np.array([[4 ], [1] ,[ 2.5]])
)
######################################################
assert_array_equal(replace_nans(
    np.array([[np.nan, np.nan,  np.nan],
              [     4, np.nan,       5],
              [np.nan,      8,  np.nan]]).T),
    np.array([[0. , 0. , 0. ],
              [4. , 4.5, 5. ],
              [8. , 8. , 8. ]]).T
)
######################################################
