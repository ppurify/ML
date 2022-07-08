# 1. Handling shape
## 1.1 reshape
: Array의 shape의 크기를 변경, `element/size의 갯수는 동일`
### EX) (2,4) -> (8,)
```
test_matrix = [[1,2,3,4],[1,2,5,8]]
np.array(test_matrix).shape
```
```
> (2,4)
```
```
np.array(test_matrix).reshape(8,)
```
```
> array([1,2,3,4,1,2,5,8])
```
```
np.array(test_matrix).reshape(8,).shape
```
```
> (8,)
```
하나의 값만 지정하고 다른 나머지의 하나의 값을 지정안할 때 `지정안하는 값을 -1로 설정`<br>
EX) 
```
np.array(test_matrix).reshape(2,4).shape
> (2,4)

# 뒤에 2가 고정 => -1은 자동으로 4
np.array(test_matrix).reshape(-1,2).shape
> (4,2) 
```
## 1.2 flatten
: 다차원 array를 1차원 array로 변환, reshape의 하나의 기능이라고 봐도 됨
```
test_matrix = [ [[1,2,3,4],[1,2,5,8]], [[1,2,3,4],[1,2,5,8] ]
np.array(test_matrix).flatten()
```
```
> array([1,2,3,4,1,2,5,8,1,2,3,4,1,2,5,8])
```

# 2. Indexing & Slicing
## 2.1 indexing for numpy array
- list와 달리 2차원 배열에서 [0,0] 표기법을 제공함
- matrix일 경우 앞은 row, 뒤는 column을 의미
```
import numpy as np

a = np.array([[1, 2, 3] ,[4.5, 5, 6]], int)
print(a)
> array([[1, 2, 3] ,[4, 5, 6]])

print(a[0,0]) # Two dimensional array representation #1
> 1

print(a[0][0]) # Two dimensional array representation #2
> 1

a[0,0] = 12 # Matrix 0,0에 12 할당
print(a)
> array([[12, 2, 3] ,[4, 5, 6]])

a[0][0] = 5 # Matrix 0,0에 5 할당
a[0,0]
> 5
```
## 2.2 slicing for numpy array
- list와 달리 `행과 열 부분을 나눠서 slicing 가능`
- matrix의 부분 집합을 추출할 때 유용
EX) [:2, :] => Row 0 ~ 1까지, column 전체 <br>
`값만 추출한 것이기 때문에 a의 자체가 변하지는 않음`
```
a = np.array([[1,2,3,4,5], [6,7,8,9,10]], int)
# 전체 Row의 2열 이상
a[:, 2:]
```
```
> array([[3,4,5],[3,4,5]]) 
```
```
# 1 Row ~ 2 Row의 전체
a[1:3]
```
```
> array([[6,7,8,9,10]])
```

```
test_example = [ [1,2,5,8], [1,2,5,8], [1,2,5,8], [1,2,5,8] ]
# 1~2 Row로 2차원이지만 2Row제외, 1 Column까지
test_example[1:2, :2]
```
```
> array([[1,2]])
```

```
# Row 전체, Column 처음부터 끝까지 가는데 2칸씩 띄어라
arr = [[0,1,2,3,4], 
       [5,6,7,8,9], 
       [10,11,12,13,14]]
```

```
arr[:, ::2]
```
```
> [[0,2,4],
   [5,7,9],
   [10,12,14]]
```

```
# Row 2칸씩, Column 3칸씩
arr[::2,::3]
```
```
> [[0,3],
   [10,13]]
```

# 3. Creation function
: Array 수정하는 함수
## 3.1 arange
- array range를 지정하여 value의 list를 생성하는 명령어
```
# range : List의 range와 같은 효과, integer로 0 ~ 29까지 배열 추출
np.arange(30)
```
```
> array([0,1,2,3,4,5,6,7,8,9, ... , 29])
```

```
# floating point 표시 가능
# np.arange(start, end, step)
np.arange(0, 5, 0.5) # 0.5단위로 0부터 시작
```
```
> array([0. , 0.5, 1. , 1.5, 2. , 2.5, ..., 4.5])
```

```
np.arange(30).reshape(5,6)
# 0~29까지의 숫자를 5X6형태로
```
```
> array([[0,1,2,3,4,5],
         [6,7,8,9,10,11],
         [12,13,14,15,16,17],
         [18,19,20,21,22,23],
         [24,25,26,27,28,29]])
```

## 3.2 ones,zeros and empty
- zeros : 0으로 가득찬 ndarray 생성
>np.zeros(shape, dtype, order)
```
# 10개의 0으로 가득찬 zero vector 
np.zeros(shape=(10,), dtype=np.int8) 생성
```
```
> array([0,0,0,0,0,0,0,0,0,0], dtype = int8)
```

```
#2X5의 zero matrix 생성>
np.seros((2,5))
```
```
> array([[0., 0., 0., 0., 0. ],
         [0., 0., 0., 0., 0. ]])
```

- ones : 1로 가득찬 ndarray 생성
>np.ones(shape, dtype, order)
```
np.ones(shape=(10,), dtype = np.int8)
```
```
> array([1,1,1,1,1,1,1,1,1,1], dtype =int8)
```
```
np.ones((2,5))
```
```
> array([[1. , 1. , 1. , 1. , 1.],
         [1. , 1. , 1. , 1. , 1.]])
```

- empty : shape만 주어지고 `비어있는 ndarray생성`<br>
(memory initialization이 되지 X) 빈공간을 잡아줌<br>
실행할 때 마다 값이 계속 바뀜
```
np.empty(shape=(10,), dtype = np.int8)
```
```
> array([0, 0, 0, 0, 0, 0, 0, 64, -74, 105], dtype =int8)
```
## 3.3 something_like
- 기존 ndarray의 shape size만큼 1,0 또는 empty array를 반환
>np.zeros_like<br>
np.ones_like<br>
np.empty_like
```
test_matrix = np.arange(30).reshape(5,6)
np.ones_like(test_matrix)
```
```
> array([[1,1,1,1,1,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1],
         [1,1,1,1,1,1]])
```
## 3.4 identity
: 단위행렬(i 행렬)을 생성
- 대각행렬이 1
- matrix 형태 기준
```
np.identity(n=3, dtype = np.int8)
```
```
> array([[1,0,0],
         [0,1,0],
         [0,0,1]], dtype = int8)
```

```
np.identity(5)
```
```
> array([[1., 0., 0., 0., 0.],
         [0., 1., 0., 0., 0.],
         [0., 0., 1., 0., 0.],
         [0., 0., 0., 1., 0.],
         [0., 0., 0., 0., 1.]])
```
## 3.5 eye
: 대각선이 1인 행렬
- k값의 시작 index의 변경 가능
```
np.eye(3)
```
```
> array([[1. ,0. ,0. ],
         [0. ,1. ,0. ],
         [0. ,0. ,1. ]])
```

```
# 3X5의 Matrix, 2번째 Column에서 1시작
np.eye(3,5,k=2)
```
```
> array([[0., 0., 1., 0., 0.].
         [0., 0., 0., 1., 0.],
         [0., 0., 0., 0., 1.]])
```

```
# 3X5의 대각 행렬
np.eye(N=3, M=5, dtype = np.int8)
```
```
> array([[1,0,0,0,0],
         [0,1,0,0,0],
         [0,0,1,0,0]], dtype=int8)
```

## 3.6 diag
- `대각 행렬`의 value 추출
```
matrix = np.arange(9).reshape(3,3)
np.diag(matrix)
```
```
> array([0,4,8])
```

```
matrix = ([[0,1,2],
           [3,4,5],
           [6,7,8]])
```

```
# k is start index
np.diag(matrix, k=1)
```
```
> array([1,5])
```

## 3.7 random sampling
- 데이터 분포에 따른 sampling으로 array를 생성
>np.random.uniform(start, end, data size).reshape <br>
모수값 두개(start, end)<br>
균등분포 : uniform / 정규분포 : normal / 지수분포 : exponential
```
# 균등분포
np.random.uniform(0,1,10).reshape(2,5)
```
```
> array([[0.67406593,0.73858,0.03686489,0.38748,0.39489],
         [0.1343434,0.9641029,0.34978,0.387428,0.385927]])
```

# 4. Operation Functions
## 4.1 sum
- ndarray의 element들 간의 합을 구함
- list의 sum 기능과 동일
```
# 1부터 10까지 
test_array = np.arange(1,11)
test_array
```
```
> array([1,2,3,4,...,10])
```

```
test_array.sum()
```
```
> 55
```
```
test_array.sum(dtype=np.float)
```
```
> 55.0
```

## 4.2 axis
- All operation function을 실행할 때 기준이 되는 dimension 축 <br>
axis = 0 : Column단위에서의 합 <br>
axis = 1 : Row단위에서의 합
```
# (3,4) => 3 : axis = 0, 4 : axis = 1
test_array = np.arange(1,13).reshape(3,4)
test_array
```
```
> array([[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]])
```
```
test_array.sum(axis=1), test_array.sum(axis=0)
```
```
> (array([10,26,42]), array(15,18,21,24))
```

> ex) (3,3,4) <- (dimension, Row, Column) <br>
(axis = 0, axis = 1 , axis = 2) <br>
axis = 0 : 각 dimension의 같은 위치 숫자의 합 <br>
axis = 1 : Column단위에서의 합 <br>
axis = 2 : Row단위에서의 합

```
third_order_tensor.sum(axis = 2)
```
```
> array([[10,26,42],
         [10,26,42],
         [10,26,42]])
```
```
third_order_tensor.sum(axis = 1)
```
```
> array([[15,18,21,24],
         [15,18,21,24],
         [15,18,21,24]])
```
```
third_order_tensor.sum(axis = 0)
```
```
> array([[3,6,9,12],
         [15,18,21,24],
         [27,30,33,36]])
```
`새로 생성된 축이 Always axis = 0`이 된다.

## 4.3 mean & std
- ndarray의 element들 간의 평균 또는 표준편차를 반환
```
test_array = np.arange(1,13).reshape(3,4)
test_array
```
```
> array([[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]])
```

```
test_array.mean(), test_array.mean(axis=0)
```
```
> (6.5, array([5. , 6. , 7. , 8.]))
```
```
test_array.std(), test_array.std(axis=0)
```
```
> (3.4520525295346629, 
array([3.26598632 , 3.26498632 , 3.26598632 , 3.26598632]))
```

## 4.4 mathematical functions
- 그 외에도 다양한 수학 연산자를 제공함 (np.something 호출)

## 4.5 concatenate
- numpy array를 합치는(붙이는) 함수
> vstack <br>
ex) <br> 
1 2 3 <br>  
2 3  4 <br>  
vstack 후 <br>
1 2 3 <br>
2 3 4
```
a = np.array([1,2,3])
b = np.array([2,3,4])
np.vstack((a,b)) # vector형태가 matrix로
```
```
> array([[1,2,3],
         [2,3,4]])
```

> hstack
```
a = np.array([[1],[2],[3]])
b = np.array([[2],[3],[4]])
np.hstack((a,b))
```
```
> array([[1,2],
         [2,3],
         [3,4]])
```

> concatenate : axis 기준으로 붙임
```
a = np.array([[1,2,3]])
b = np.array([[2,3,4]])
np.concatenate((a,b), axis = 0) # 각 Row를 붙임 => 위아래 붙임
```
```
> array([[1,2,3],
         [2,3,4]])
```
```
a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])
np.concatenate((a,b.T), axis = 1)
```
```
> array([[1,2,5],
         [3,4,6]])
```
- `차원 추가하기!`
```
b[np.newaxis, :]
```
```
array([[5,6]])
```