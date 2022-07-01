# Challenge 1
## Instruction
### 行列積のループ順序としては6種類の組合せがある。この6種類を実行速度が速いと思う方から順に並べてください。実際に実験してその予想が正しいかどうか確かめてください。
### i-j-k, i-k-j, j-i-k, j-k-i, k-i-j, k-j-i
注：この宿題はC/C++、Java、Go、Rustでやってください（理由は宿題2を参照）

### The loop order of the matrix multiplication has six patterns. Which one will be the fastest? Which one will be the slowest? Sort the six patterns from the fastest to the slowest based on your reasoning.

*Do this homework using C, C++, Java, Rust or Go. Don't use Python.

## My answer

I expect the six patterns to be sorted like this.

|  j-k-i,  k-j-i   | i-j-k, j-i-k,  | i-k-j, k-i-j |
|:----------------:|:-------------:|:-------------:|
| slowest          |               | fastest       |

Let me explain my reasoning behind the sorting.

`j-k-i` : `c[i][j]` causes a cache miss, so does `a[i][k]`.  I expect this pattern to be the slowest because there are two elements that cannot take the advantage of cache hit.

`k-j-i` : `c[i][j]` causes a cache miss, so does `a[i][k]`.

`i-j-k` :  `b[k][j]` causes a cache miss.

`j-i-k` : `b[k][j]` causes a cache miss.

`i-k-j` : None of the three elements does not cause a cache miss.

`k-i-j` : None of the three elements does not cause a cache miss.

