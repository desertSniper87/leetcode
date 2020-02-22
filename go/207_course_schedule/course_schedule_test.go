package course_schedule

import (
    "testing"
)

/*
 *func TestCanFinish_1(t *testing.T) {
 *    input := [][]int {{1, 0}}
 *    result := canFinish(2, input)
 *    if result != true {
 *       t.Errorf("incorrect, got: %v, want: %v.", result, true)
 *    }
 *}
 */
func TestCanFinish_2(t *testing.T) {
    input := [][]int {{1, 0}, {0, 1}}
    result := canFinish(2, input)
    if result != true {
       t.Errorf("incorrect, got: %v, want: %v.", result, true)
    }
}
