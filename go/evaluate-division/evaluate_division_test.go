package calcEquation

import (
	"testing"
)

func check(result []float64, want []float64, t *testing.T) {
	if len(result) != len(want) {
		t.Errorf("incorrect, got: %v, want: %v.", result, want)
	}

	for i, elem := range result {
		if want[i] != elem {
			t.Errorf("incorrect, got: %v, want: %v.", result, want)
		}
	}
}

func Test_eval_1(t *testing.T) {

	equations := [][]string{[]string{"a", "b"}, []string{"b", "c"}}
	values := []float64{2.0, 3.0}
	queries := [][]string{[]string{"a", "c"}, []string{"b", "c"}, []string{"a", "e"}, []string{"a", "a"}, []string{"x", "x"}}
	result := calcEquation(equations, values, queries)

	want := []float64{6.00000, 0.50000, -1.00000, 1.00000, -1.00000}

	check(result, want, t)

}
