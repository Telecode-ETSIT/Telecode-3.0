package main

import "fmt"

func main() {
	var s string
	var N, n, c int
	fmt.Scan(&N)

	for i := 0; i < N; c++ {
		fmt.Scan(&n)
		if n > 0 {
			row, cols := c%6, colums(n)
			for _, col := range cols {
				s += encrypt(row, col)
				i++
			}
		}
	}
	fmt.Println(pretty(s))
}

func colums(cols int) []int {
	mask := []int{32, 16, 8, 4, 2, 1}
	pres := make([]int, 0)

	for i, m := range mask {
		if cols&m > 0 {
			pres = append(pres, i)
		}
	}
	return pres
}

func encrypt(f, c int) string {
	abc := []string{"A", "D", "F", "G", "V", "X"}
	return abc[f] + abc[c]
}

func pretty(s string) (sol string) {
	var w, rest string
	for w, rest = s[:5], s[5:]; len(rest) > 5; w, rest = rest[:5], rest[5:] {
		sol += w + " "
	}
	sol += w + " " + rest
	return
}
