package course_schedule

import "fmt"

func getIncomingEdges(graph map[int][]int, vertex int) []int {
	v_list := []int{}
	for i, v := range graph {
		for _, out_vert := range v {
			if vertex == out_vert {
				v_list = append(v_list, i)
			}
		}
	}

	return v_list
}

func isCycle(graph map[int][]int, inDegree map[int]int, numCourses int) bool {

	fmt.Println("inDegree: ", inDegree)
	queue := make([]int, 0)
	for i := 0; i < numCourses; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	count := 0
	for len(queue) != 0 {

		u := queue[0]
		queue = queue[1:]

		for _, elem := range graph[u] {
			inDegree[elem]--
			if inDegree[elem] == 0 {
				queue = append(queue, elem)
			}
		}
		count++
	}

	if count != numCourses {
		return true
	} else {
		return false
	}
}

func canFinish(numCourses int, prerequisites [][]int) bool {
	var adjList = make(map[int][]int, len(prerequisites))
	var visited = make(map[int]bool, 0)

	for _, element := range prerequisites {
		src := element[1]
		dest := element[0]

		if len(adjList[src]) == 0 {
			adjList[src] = []int{dest}
		} else {
			adjList[src] = append(adjList[src], dest)
		}

		visited[src] = false
		visited[dest] = false
	}

	var inDegree = make(map[int]int, numCourses)

	for vertex_n, _ := range adjList {
		visited[vertex_n] = true
		for _, vertex_m := range adjList[vertex_n] {
			v_list := getIncomingEdges(adjList, vertex_m)
			inDegree[vertex_m] = len(v_list)
		}
	}

	canFinish := !(isCycle(adjList, inDegree, numCourses))

	return canFinish
}
