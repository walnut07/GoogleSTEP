package main
// go run matrix_constant_n.go > c_time_required_k-i-j.csv
import (
	"fmt"
	"time"
)

func main() {
	i := 0
	n := 50

	for i < 1000 {

		a := make([][]int, n)
		for i := range a {
				a[i] = make([]int, n)
		}
		b := make([][]int, n)
		for i := range b {
				b[i] = make([]int, n)
		}
		c := make([][]int, n)
		for i := range c {
				c[i] = make([]int, n)
		}
		
		// Initialize the matrices to some values.
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				a[i][j] = i * n + j
				b[i][j] = j * n + i
				c[i][j] = 0
			}
		}

		startTime := time.Now()

		// Multiply metrices.
		for k := 0; k < n; k++ {
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					c[i][j] += a[i][k] * b[k][j];
				}
			}
		}

		endTime := time.Now()
		runningTime := endTime.Sub(startTime) // μs represents microsecond 
		fmt.Println(n, runningTime.Seconds())

		i++
	}

}