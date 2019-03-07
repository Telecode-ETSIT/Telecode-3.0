package main

import (
	"encoding/base32"
	"fmt"
)

func main() {
	var N int
	var s string

	fmt.Scan(&N)
	for i := 0; i < N; i++ {
		fmt.Scan(&s)
		sol, _ := base32.StdEncoding.DecodeString(s)
		fmt.Println(string(sol))
	}
}
