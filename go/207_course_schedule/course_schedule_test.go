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
 */
/*
 *func TestCanFinish_2(t *testing.T) {
 *    input := [][]int{{1, 0}, {0, 1}}
 *    result := canFinish(2, input)
 *    want := false
 *    if result != want {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, want)
 *    }
 *}
 *func TestCanFinish_3(t *testing.T) {
 *    input := [][]int{{1, 0}, {0, 1}}
 *    result := canFinish(2, input)
 *    if result != true {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, true)
 *    }
 *}
 */
/*
 *func TestIncomingEdges(t *testing.T) {
 *    graph := [][]int{{1, 0}, {2, 1}, {3, 1}, {3, 2}}
 *    vertex := 3
 *    result := getIncomingEdges(graph, vertex)
 *    want := [2]int{1, 2}
 *    if result != want {
 *        t.Errorf("incorrect, got: %v, want: %v.", result, want)
 *    }
 *}
 */
func TestCanFinish_4(t *testing.T) {
	input := [][]int{{1, 0}, {2, 1}, {3, 1}, {3, 2}}
	result := canFinish(4, input)
	want := true
	if result != want {
		t.Errorf("incorrect, got: %v, want: %v.", result, want)
	}
}
