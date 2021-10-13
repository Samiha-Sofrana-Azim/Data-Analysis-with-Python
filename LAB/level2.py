from graph import Vertex, Edge

file = open("input2.txt", "r")
lines = file.readlines()

number_of_vertex = int(lines[0])
number_of_edges = int(lines[1])
vertex_list = []

for i in range(0, number_of_vertex):
    v = Vertex(i)
    vertex_list.append(v)

for i in range(0, number_of_edges):
    line = lines[i+2]
    line = line.replace('\n', '')
    values = line.split(' ')
    v1 = vertex_list[int(values[0])]
    v2 = vertex_list[int(values[1])]

    e = Edge(int(values[0]), int(values[1]))
    v1.add_neighbour(e)
    v2.add_neighbour(e)

lina_position = int(lines[number_of_edges+2])
nora_position = int(lines[number_of_edges+3])
lara_position = int(lines[number_of_edges+4])


def bfs(s):
    visited = [False] * (len(vertex_list))
    queue = []
    queue.append(s)
    vertex_list[s].step = 0
    visited[s] = True

    while queue:
        s = queue.pop(0)
        for edge in vertex_list[s].edges:
            if (edge.v1 != s) and (visited[edge.v1] is False):
                queue.append(edge.v1)
                vertex_list[edge.v1].step = vertex_list[s].step + 1
                visited[edge.v1] = True
            elif (edge.v2 != s) and (visited[edge.v2] is False):
                queue.append(edge.v2)
                vertex_list[edge.v2].step = vertex_list[s].step + 1
                visited[edge.v2] = True


# for nora
bfs(nora_position)
nora_step = vertex_list[lina_position].step
# for lara
bfs(lara_position)
lara_step = vertex_list[lina_position].step
if nora_step > lara_step:
    print('Lara')
elif lara_step > nora_step:
    print('Nora')