package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
	fmt.Println(trap(height))
}

func trap(height []int) int {
	length := len(height)

	var left_max, right_max [length]int

	//left_max[0] = height[0]
	//fmt.Println(max(1, 2))

	//for i := 1; i < length; i++ {
	////left_max[i] = max(left_max[i], height[i])
	//}

	return length
}
