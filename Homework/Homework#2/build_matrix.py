import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    data = filename
    # csv file read
    df = pd.read_csv(data, sep = ",")
    # df의 source와 target을 기준으로 rating의 합이 element가 되는 df생성
    df1 = df.groupby(["source", "target"])["rating"].sum()
    # Nan change to 0, change to matrix shape
    df_matrix = df1.unstack(fill_value=0)
    # matrix의 element => value 추출
    df_v = df_matrix.values
    return df_v


def get_frequent_matrix(filename):
    data = filename
    # Read the Data
    df = pd.read_csv(data, sep = ",")
    # source, target의 그룹별 빈도
    df_count = df.groupby(["source","target"]).value_counts()
    # data type int change to float
    df_float = df_count.astype(np.float32)
    # change to matrix shape, return value
    df_value = df_float.unstack().values
    return df_value
