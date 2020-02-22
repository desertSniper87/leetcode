package course_schedule

import "fmt"

// Graph : represents a Graph
//type Graph struct {
    //nodes []*GraphNode
//}

 ////GraphNode : represents a Graph node
//type GraphNode struct {
    //id    int
    //edges map[int]int
//}

//func newNode (id int) *GraphNode {
    //return &GraphNode{
        //id: id,
        //edges: make(map[int]int),
    //}
//}

//func NewGraph() *Graph {
    //return &Graph{
        //nodes: []*GraphNode{},
    //}
//}

//func (g *Graph) AddNode(id int) () {
    //id = len(g.nodes)
    //g.nodes = append(g.nodes, &GraphNode{
        //id:    id,
        //edges: make(map[int]int),
    //})
    //return
//}

//func (g *Graph) GetNodeFromValue(val int) (node *GraphNode, is_found bool) {
    //for _, element := range g.nodes {
        //if element.id == val{
            //return element, true
        //}
    //}
    //return node, false
//}

//func (g* Graph) printGraph() {
    //for _, element := range g.nodes {
        //fmt.Println(element.id, element.edges)
    //}
    //return
//}

func toposort (adjList map[int][]int, visited map[int]bool, src int) map[int]bool {
    visited[src] = true
    for _, i := range adjList[src] {
        if visited[i] == false{
            visited = toposort(adjList, visited, i)
        }
    }
    return visited
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    var adjList = make(map[int][]int, len(prerequisites))
    var visited = make(map[int]bool, 0)

    fmt.Println(adjList[1])
    for _, element := range prerequisites {
        src := element[1]
        dest := element[0]

        if len(adjList[src]) == 0{
            adjList[src] = []int{dest}
        } else {
            adjList[src] = append(adjList[src], dest)
        }

        visited[src] = false
        visited[dest] = false
    }

    visited = toposort(adjList, visited, 0)

    fmt.Println(visited)
    return false
}
