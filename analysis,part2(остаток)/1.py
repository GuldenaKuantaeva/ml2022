import numpy as np
import numpy.testing as test


def nearest_value(X: np.array, a: float) -> float:
    X = X.flatten()
    X.sort()
    return X.flat[np.abs(a - X).argmin()]  # вернет число из инд


def main():
    ######################################################
    test.assert_equal(
        nearest_value(np.array([1, 2, 13]), 10),
        13)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([-1, 0]), -0.5),
        -1)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[[1], [2], [3]], [[4], [5], [6]]]), 4.5),
        4)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[1, 2, 13],
                                [15, 6, 8],
                                [7, 18, 9]]), 7.2),
        7)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[-1, -2],
                                [-15, -6]]), -100),
        -15)
    ######################################################
    test.assert_equal(
        nearest_value(np.array([[2, 2],
                                [12, 12]]), 7),
        2)
    #####################################################
    test.assert_equal(
        nearest_value(np.array([[-2, -2],
                                [-12, -12]]), -7),
        -12)
    #####################################################


if __name__ == "__main__":
    main()
