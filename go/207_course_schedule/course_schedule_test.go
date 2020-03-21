package course_schedule

import (
	"testing"
)

/*
 *func TestCanFinish_1(t *testing.T) {
 *    input := [][]int{{1, 0}}
 *    result := canFinish(2, input)
 *    if result != true {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, true)
 *    }
 *}
 *
 *func TestCanFinish_2(t *testing.T) {
 *    input := [][]int{{1, 0}, {0, 1}}
 *    result := canFinish(2, input)
 *    want := false
 *    if result != want {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, want)
 *    }
 *}
 */
func TestCanFinish_4(t *testing.T) {
	input := [][]int{{1, 0}, {2, 1}, {1, 3}, {3, 2}}
	result := canFinish(4, input)
	want := false
	if result != want {
		t.Errorf("incorrect, got: %v, want: %v.", result, want)
	}
}

/*
 *func TestCanFinish_5(t *testing.T) {
 *    input := [][]int{{1, 0}, {2, 1}, {3, 1}, {3, 2}}
 *    result := canFinish(4, input)
 *    want := true
 *    if result != want {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, want)
 *    }
 *}
 */
