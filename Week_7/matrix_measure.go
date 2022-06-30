package main

import (
	"fmt"
	"time"
	"encoding/csv"
	//"log"
	"os"
)


func main() {
	
	f, err := os.Create("matrix_multication_time_required.csv")
	if err != nil {
		fmt.Println(err)
	}
	writer := csv.NewWriter(f) 
	fmt.Println(writer)
	for n := 2; n <= 5; n++ {
		
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
		 
		timeRequired := make([][]int, n)
		startTime := time.Now()

		// Multiply metrices.
		for j := 0; j < n; j++ {
			for k := 0; k < n; k++ {
				for i := 0; i < n; i++ {
					c[i][j] += a[i][k] * b[k][j];
				}
			}
		}

		fmt.Println(c)

		timeRequired = append(timeRequired, n, time.Since(startTime))
		fmt.Println(timeRequired)
		//append(timeRequired, time.Since(startTime))
		//append(n_time, [n, timeRequired])
		//err = writer.Write(timeRequired)
		//if err != nil {
		//	log.Fatal("Error:", err)
		//}
	writer.Flush()
	}
}

// go run matrix_measure.go