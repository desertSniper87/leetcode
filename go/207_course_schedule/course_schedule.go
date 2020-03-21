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

// This function returns true if there is a cycle
// in directed graph, else returns false.
func isCycle(graph map[int][]int, inDegree map[int]int, numCourses int) bool {
	// Create an queue and enqueue all vertices with
	// indegree 0

	fmt.Println("inDegree: ", inDegree)
	queue := make([]int, 0)
	for i := 0; i < numCourses; i++ {
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}

	// Initialize count of visited vertices
	count := 0

	// One by one dequeue vertices from queue and enqueue
	// adjacents if indegree of adjacent becomes 0
	for len(queue) != 0 {

		// Extract front of queue (or perform dequeue)
		// and add it to topological order
		fmt.Printf("queue: %v \n", queue)
		u := queue[0]
		queue = queue[1:]

		// Iterate through all its neighbouring nodes
		// of dequeued node u and decrease their in-degree
		// by 1
		//list<int>::iterator itr;
		//for itr = adj[u].begin(); itr != adj[u].end(); itr++
		for _, elem := range graph[u] {
			inDegree[elem]--
			if inDegree[elem] == 0 {
				queue = append(queue, elem)
			}
		}

		// If in-degree becomes zero, add it to queue
		count++
	}

	// Check if there was a cycle
	fmt.Println("Count: ", count)
	fmt.Println("numCourses: ", numCourses)
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

	fmt.Println("adjList: ", adjList)
	fmt.Println("visited: ", visited)

	var inDegree = make(map[int]int, numCourses)

	for vertex_n, _ := range adjList {
		visited[vertex_n] = true
		for _, vertex_m := range adjList[vertex_n] {
			//fmt.Println("adjList[vertex_n]:", adjList[vertex_n])
			v_list := getIncomingEdges(adjList, vertex_m)
			//fmt.Println("vertex_m, v_list", vertex_m, v_list)
			inDegree[vertex_m] = len(v_list)
		}
	}

	canFinish := !(isCycle(adjList, inDegree, numCourses))

	return canFinish
}
