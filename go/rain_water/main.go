package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}


func trap(height []int) int {
    if len(height) == 0 {
        return 0
    }
	var length = len(height)

    var left_max = make([] int, length)
    var right_max = make([] int, length)

    left_max[0] = height[0]
    right_max[length-1] = height[length-1]

    for i := 1; i < length; i++ {
        left_max[i] = max(height[i], left_max[i-1])
    }

    for i := length-2; i >= 0; i-- {
        right_max[i] = max(height[i], right_max[i+1])
    }

    var ans = 0

    for i := 0; i < length; i++ {
        ans += min(left_max[i], right_max[i]) - height[i]
    }
    return ans

}

func main() {
    height := []int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
    fmt.Println(trap(height))
}
