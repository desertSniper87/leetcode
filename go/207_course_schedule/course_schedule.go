package course_schedule

import "fmt"

func getIncomingEdges(graph map[int][]int, vertex int) []int {
	v_list := []int{}
	for i, v := range graph {
		//fmt.Println("i: ", i, "v: ", v)
		for _, out_vert := range v {
			//fmt.Println("out_vert", out_vert, "vertex", vertex)
			if vertex == out_vert {
				v_list = append(v_list, i)
			}
		}
	}

	//fmt.Println(v_list)
	return v_list
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

	fmt.Println("adjList: ", adjList)
	fmt.Println("visited: ", visited)

	for vertex_n, _ := range adjList {
		visited[vertex_n] = true
		for _, vertex_m := range adjList[vertex_n] {
			fmt.Println(adjList[vertex_n])
			v_list := getIncomingEdges(adjList, vertex_m)
			fmt.Println(vertex_m, v_list)
		}
	}

	return true
}
