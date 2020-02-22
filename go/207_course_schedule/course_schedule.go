package course_schedule

import "fmt"

// Graph : represents a Graph
type Graph struct {
    nodes []*GraphNode
}

 //GraphNode : represents a Graph node
type GraphNode struct {
    id    int
    edges map[int]int
}

func NewGraph() *Graph {
    return &Graph{
        nodes: []*GraphNode{},
    }
}

func (g *Graph) AddNode(id int) () {
    id = len(g.nodes)
    g.nodes = append(g.nodes, &GraphNode{
        id:    id,
        edges: make(map[int]int),
    })
    return
}

func (g *Graph) GetNodeFromValue(val int) (node *GraphNode, is_found bool) {
    for _, element := range g.nodes {
        if element.id == val{
            return element, true
        }
    }
    return node, false
}

func canFinish(numCourses int, prerequisites [][]int) bool {
    crsPreReqGraph := NewGraph()

    for _, element := range prerequisites{
        src := element[0]
        dest := element[1]
        fmt.Println(src, dest)

        node, is_found := crsPreReqGraph.GetNodeFromValue(src)

        if is_found == false {
            prerequisites.AddNode()
        }

    }
    return false
}
