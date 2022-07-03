# Challenge 1
## Instruction
### 行列積のループ順序としては6種類の組合せがある。この6種類を実行速度が速いと思う方から順に並べてください。実際に実験してその予想が正しいかどうか確かめてください。
### i-j-k, i-k-j, j-i-k, j-k-i, k-i-j, k-j-i
注：この宿題はC/C++、Java、Go、Rustでやってください（理由は宿題2を参照）

### The loop order of the matrix multiplication has six patterns. Which one will be the fastest? Which one will be the slowest? Sort the six patterns from the fastest to the slowest based on your reasoning.

*Do this homework using C, C++, Java, Rust or Go. Don't use Python.

## My answer
### Estimate
I expect the six patterns to be sorted like this.

|  j-k-i,  k-j-i   | i-j-k, j-i-k,  | i-k-j, k-i-j |
|:----------------:|:-------------:|:-------------:|
| slowest          |               | fastest       |

Let me explain my reasoning.

`j-k-i` : `c[i][j]` causes a cache miss, so does `a[i][k]`.  I expect this pattern to be the slowest because there are two elements that cannot take the advantage of cache hit.

`k-j-i` : `c[i][j]` causes a cache miss, so does `a[i][k]`.

`i-j-k` :  `b[k][j]` causes a cache miss.

`j-i-k` : `b[k][j]` causes a cache miss.

`i-k-j` : None of the three elements does not cause a cache miss.

`k-i-j` : None of the three elements does not cause a cache miss.

### Experiment
I recorded the running time of the matrix multiplication of the six patterns in two ways. One is to record the running time where the number of columns in a matrix increments by one till 300. Another is to record the running time for 50 times where the number of columns is constantly 300.

### Experiment 1: columns in a matrix increments
Program:
```
matrix_increase_n.go
```
How to run: <br>
X-X-X should be the pattern you want to try.
```
go run matrix_increase_n.go > time_required-X-X-X.csv
```

According to the chart below, the six patterns can be grouped into three:
1. `j-k-i` and `k-j-i`
2. `i-j-k` and `j-i-k`
3. `i-k-j` and `k-i-j`

![chart x-asis is n where n incraeses from 2 to y](Matrix%20multiplication%20the%20num%20of%20cols%20increases%202%20to%20300.png)

Those three groups match the estimate I made in the beginning.

### Experiment 2: columns in a matrix always 300
Program:
```
matrix_constant_n.go
```
How to run: <br>
X-X-X should be the pattern you want to try.
```
go run matrix_constant_n.go > c_time_required_X-X-X.csv
```

I made a bar graph that represents the median of the 50 cases. The number of columns is always 300.
![chart x-axis is the six patterns](The%20median%20of%2050%20cases%20where%20the%20num%20of%20col%20is%20300.png)

According to the chart below, again, the six patterns can be grouped into three:
1. `j-k-i` and `k-j-i`
2. `i-j-k` and `j-i-k`
3. `i-k-j` and `k-i-j`

## Conclusion
According to the 1st experiment and the 2nd one, it is clear that the six patterns can be sorted like below, based on their runnning time. 

|  j-k-i,  k-j-i   | i-j-k, j-i-k,  | i-k-j, k-i-j |
|:----------------:|:-------------:|:-------------:|
| slowest          |               | fastest       |

This is the same as my estimate.