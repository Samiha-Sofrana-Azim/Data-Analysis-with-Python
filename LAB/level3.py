from graph import Vertex, Edge

file = open("input3.txt", "r")
lines = file.readlines()

number_of_vertex = int(lines[0])
number_of_edges = int(lines[1])
vertex_list = []


for i in range(0, number_of_vertex):
    v = Vertex(i)
    vertex_list.append(v)

lina_position = int(lines[number_of_edges+2])
number_of_participant = int(lines[number_of_edges+3])
participants_position_list = []
for i in range(0, number_of_participant):
    participants_position_list.append(int(lines[number_of_edges+4+i]))


def bfs(s):
    visited = [False] * (len(vertex_list))
    queue = []
    queue.append(s)
    vertex_list[s].step = 0
    visited[s] = True

    while queue:
        s = queue.pop(0)
        for edge in vertex_list[s].edges:
            if (edge.v2 != s) and (visited[edge.v2] is False):
                queue.append(edge.v2)
                vertex_list[edge.v2].step = vertex_list[s].step + 1
                visited[edge.v2] = True


if len(participants_position_list) > 1:
    for i in range(0, number_of_edges):
        line = lines[i + 2]
        line = line.replace('\n', '')
        values = line.split(' ')
        v1 = vertex_list[int(values[1])]
        e = Edge(int(values[1]), int(values[0]))
        v1.add_neighbour(e)
    bfs(lina_position)
    min_step = 50
    for position in participants_position_list:
        if min_step > vertex_list[position].step:
            min_step = vertex_list[position].step
    print(min_step)