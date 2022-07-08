import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    X = np.array(np.arange(n^2).reshape(n,n))
    return X


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    # type = 0 -> element = 0
    if type == 0 :
        X = np.zeros(shape, dtype)
    # type = 1 -> element = 1
    elif type == 1 :
        X = np.ones(shape, dtype)
    # type = 99 -> element = empty
    else :
        X = np.empty(shape, dtype)
        
    return X


def change_shape_of_ndarray(X, n_row):
    # n_row : 생성하려는 matrix row의 개수
    # n_row가 1일 경우 Vector 값을 반환
    if n_row == 1:
        X = X.flatten()
    else :
        X = X.reshape(n_row, -1)
    return X


def concat_ndarray(X_1, X_2, axis):

    n_1 = X_1.ndim #X_1의 차원
    n_2 = X_2.ndim #X_2의 차원
    
    # axis를 기준으로 통합할 때, 통합이 불가능하면 False가 반환됨.
    # 1차원일 때 열의 개수 = X_1.size
    if axis == 0 : 
        # X_1, X_2의 차원이 2차원인 경우
        if n_1 == n_2 and n_1 == 2 : 
            if X_1.shape[1] == X_2.shape[1]:  # X_1, X_2의 열이 동일할 때 
                return np.vstack((X_1,X_2))
            else: # X_1, X_2의 열이 동일하지 않을 때
                return False

        # X_1, X_2의 차원이 1차원인 경우
        elif n_1 == n_2 and n_1 == 1: 
            if X_1.size == X_2.size : # X_1, X_2의 열이 동일할 때 
                return np.vstack((X_1,X_2))
            else:
                return False

        else:
            if n_1 == 1:
                if X_1.size == X_2.shape[1] :
                    return np.vstack((X_1,X_2))
                else:
                    return False
            else:
                if X_1.shape[1] == X_2.size :
                    return np.vstack((X_1,X_2))
                else:
                    return False
                    
    else : # axis = 1인 경우
        if n_1 == n_2 and n_1 == 2 : # X_1, X_2의 차원이 2차원인 경우
            if X_1.shape[0] == X_2.shape[0]:  # X_1, X_2의 행이 동일할 때 
                return np.hstack((X_1,X_2))
            else: # X_1, X_2의 행이 동일하지 않을 때
                return False
                
        elif n_1 == n_2 and n_1 == 1: # X_1, X_2의 차원이 1차원인 경우
            return np.hstack((X_1,X_2))
            
        else:
            return False
          


def normalize_ndarray(X, axis=99, dtype=np.float32):
    #X의 평균과 표준편차는 axis를 기준으로 axis 별로 산출됨.

    #Matrix의 경우 axis가 0 또는 1일 경우, row 또는 column별로 Z value를 산출함.
    if axis == 0:
        X_m = np.mean(X, axis = axis)
        X_s = np.std(X, axis = axis)
        z = (X - X_m) / X_s
        return z

    elif axis == 1:
        X_m = np.mean(X, axis = axis)
        X_s = np.std(X, axis = axis)
        X_m = X_m[np.newaxis, :].T
        X_s = X_s[np.newaxis, :].T
        z = (X - X_m)/X_s
        return z

    #axis가 99일 경우 전체 값에 대한 normalize 값을 구함.
    else:
        z = (X - np.mean(X)) / np.std(X)
        return z


def save_ndarray(X, filename="test.npy"):
    np.save(filename, arr = X)


def boolean_index(X, condition):
    condition = eval(str("X") + condition)
    return np.where(condition)


def find_nearest_value(X, target_value):
    X_t = np.abs(X - target_value)
    i = np.argmin(X_t)
    return X[i]


def get_n_largest_values(X, n):
    large_X = X[X.argsort()[::-1][:n]]
    return large_X