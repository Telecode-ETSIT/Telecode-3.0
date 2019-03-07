package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Matrix [][]int
type Data struct {
	a, b int
	m    Matrix
}

var T int

func main() {
	fmt.Scan(&T)
	do := make(chan Data)
	go input(do)
	for i := 0; i < T; i++ {
		d := <-do
		done := false
		for tmp, i := d.m, 0; i < len(d.m); i++ {
			if tmp[d.a][d.b] != 0 {
				done = true
				break
			}
			tmp, _ = mul(tmp, d.m)
		}
		if done {
			fmt.Println("SI!")
		} else {
			fmt.Println("NO!")
		}
	}
}

func mul(m1, m2 Matrix) (m3 Matrix, ok bool) {
	rows, cols, extra := len(m1), len(m2[0]), len(m2)
	if len(m1[0]) != extra {
		return nil, false
	}
	m3 = make(Matrix, rows)
	for i := 0; i < rows; i++ {
		m3[i] = make([]int, cols)
		for j := 0; j < cols; j++ {
			for k := 0; k < extra; k++ {
				m3[i][j] += m1[i][k] * m2[k][j]
			}
		}
	}
	return m3, true
}

func input(do chan Data) {
	sc := bufio.NewScanner(os.Stdin)
	for n := 0; n < T; n++ {
		sc.Scan()
		N, _ := strconv.Atoi(sc.Text())

		sc.Scan()
		ab := strings.Split(sc.Text(), " ")

		m := make(Matrix, N)

		for i := 0; i < N && sc.Scan(); i++ {
			str := strings.Split(sc.Text(), " ")
			nod := make([]int, N)
			for j := 0; j < len(str); j++ {
				k, _ := strconv.Atoi(str[j])
				nod[k] = 1
			}
			m[i] = nod
		}
		a, _ := strconv.Atoi(ab[0])
		b, _ := strconv.Atoi(ab[1])
		do <- Data{
			a: a,
			b: b,
			m: m,
		}
	}
}
