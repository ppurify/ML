# 1. How 행렬과 Matrix를 코드로 표현할 것인가?
## 1.1 코드로 방정식 표현하기
- 가장 간단한 방법 : list로 표현하기
### Ex) 
    2x1 + 2x2 + x3 = 9 
    2x1 - x2 +2x3 = 6
    x1 - x2 +2x3 = 5
```
coefficient_matrix = [[2,2,1], [2,-1,2], [1,-1,2]]
constatnt_vector =[9,6,5]
```
# 2. Numpy (Numerical Python)
## 2.1 파이썬의 고성능 과학 계산용 Package
- Natrix와 Vector와 같은 Array 연산의 사실상의 표준
- 다양한 Matrix 계산
- 굉장히 큰 Matrix에 대한 표현
- 처리 속도 문제 -> python은 Interpreter 언어
## 2.2 Numpy의 특징
- 일반 List에 비해 Fast, Memory efficient
- 반복문 없이 데이터 배열에 대한 처리 지원
- 선형대수와 관련된 다양한 기능 제공
- C, C++ 포트란 등의 언어와 통합 기능
## 2.3 numpy Install
- Windows 환경에선 conda로 package 관리 필요 (C Package Handling 등)
- jupyter 등을 설치한 상태에서는 추가 설치 필요 X
### 2.3.1 가상환경 만들기 및 Install numpy, jupyter
```
conda create -n ml python = 3.10
conda activate ml
conda install numpy
conda install jupyter
```

```
cd codes
cd numpy
jupyter notebook
```

# 3. ndarray (numpy dimesion array)

## 3.1 import
- numpy의 호출 방법
- generally numpy는 np라는 alias(별칭) 이용해서 호출
- 특별한 이유 X, 세계적인 약속 같은 것 
```
import numpy as np
```

## 3.2 array creation
- numpy는 np.array함수를 활용하여 배열을 생성 -> ndarray 객체
- numpy는 [**only one data type**](http://whatismarkdown.com/)만 배열에 넣을 수 있음
- List와 가장 큰 차이점 -> dynamic typing not supported
- C의 Array를 사용하여 배열 생성
### EX)
```
# numpy module 호출
import numpy as np
# array 생성
a = [1,2,3,4,5]
a = np.array(a, int)
a
```
```
> array([1,2,3,4,5])
```
* 함수 구성 어떻게 이루어 져있는지 -> shift + tab
### EX)
```
# numpy module 호출
import numpy as np
# array 생성
test_array = np.array(["1","4",5.0,8], float)
test_array
```
```
> array([1., 4., 5., 8.])
```
```
type(test_array)
```
```
> numpy.ndarray
```
```
type(test_array[3])
```
```
> numpy.float64
```
### 3.2.1 Numpy & Python List
- Numpy Array : 1 2 3 4 5 6 7 처럼 차례대로 값이 들어감 <br>
=> Python List보다 memory의 접근성이 좋다, memory의 size가 일정하기 때문에 data 공간 잡기 efficient
- Python List : memory 구조를 가짐 <br>
=> -5 ~ 256 값이 memory 어딘가에 static한 공간에 존재
ex ) 1 2 3 4 5 6 7 값 자체가 저장되는 것이 아닌 그 숫자의 주소값을 List에 차례대로 저장
### 3.2.2 Memory 위치 비교 : is 
```
a = [1,2,3,4,5]
b = [5,4,3,2,1] 

# 메모리 주소가 같음
a[0] is b[-1]
> True

# 메모리 위치 비교
a is b
> False

a = np.array(a)
b= np.array(b)

# 메모리 주소 다름
a[0] is b[-1]
> False
```

## 3.3 Array shape (vector)
- shape <br>
#### - numpy array의 dimension 구성을 반환 <br>
#### - array의 크기, 형태 등에 대한 정보
- dtype : numpy array의 data type을 반환
```
# String Type의 Data를 입력해도
test_array = np.array([1, 4, 5, "8"], float)
print(test_array)
> array([1., 4., 5., 8.])

# Float Type으로 자동 형변환 실시
print(type(test_array[3]))
> numpy.float64

# Array(배열) 전체의 Data Type을 반환 
print(test_array.dtype)
> dtype('float64')

a = [[1,2,3],[4,5,6],[7,8,9]]
# Array(배열)의 Shape을 튜플 형태로 반환
print(np.array(a).shape)
> (3,3)

print(test_array.shape)
> (4,)
```

## 3.4 Array shape (matrix)
```
matrix = [[1,2,5,8],[1,2,5,8],[1,2,5,8]]
np.array(matrix, int).shape
```
```
> (3,4) #(행,열)
```

## 3.5 Array shape (3rd order tensor)
```
tensor = [[[1,2,5,8],[1,2,5,8],[1,2,5,8]],
[[1,2,5,8],[1,2,5,8],[1,2,5,8]],
[[1,2,5,8],[1,2,5,8],[1,2,5,8]],
[[1,2,5,8],[1,2,5,8],[1,2,5,8]]]
np.array(tensor, int).shape
```
```
> (4,3,4) # (차원,행,열)
```

## 3.6 Array ndim
number of dimensions
```
np.array(tensor, int).ndim
```
```
> 3
```
```
# 데이터의 개수
np.array(tensor, int).size 
# 4X3X4 = 48
```
```
> 48 
```

## 3.7 Array dtype
- ndarray의 single element가 가지는 data type
- 각 element가 차지하는 memory의 크기가 결정됨
```
# data type을 integer로 선언
np.array([[1, 2, 3], [4.5, 5, 6]], dtype =int)
```
```
> array([[1,2,3],[4,5,6]])
```
```
# data type을 float로 선언
np.array([[1, 2, 3], [4.5, "5", "6"]], dtype = np.float32)
```
```
> array([[1., 2., 3. ],[4.5 ,5. ,6. ]], dtype = float32)
```

## 3.8 Array nbytes
- nbytes - ndarray object의 memory 크기를 반환
```
np.array([[1,2,3], [4.5 ,"5", "6"]], dtype = np.float32).nbytes
# 32bits = 4bytes => 6(숫자 개수)* 4bytes 
```
```
> 24
```
```
np.array([[1,2,3], [4.5 ,"5", "6"]], dtype = np.int8).nbytes
# 8bits = 1bytes => 6(숫자 개수)* 1bytes 
```
```
> 6
```