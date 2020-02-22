package course_schedule

import (
    "testing"
)

func TestCanFinish(t *testing.T) {
    input := [][]int {{1, 0}}
    result := canFinish(2, input)
    if result != true {
       t.Errorf("incorrect, got: %v, want: %v.", result, true)
    }
}
