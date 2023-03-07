graph1 = {
    "A" : ["C","B"],
    "B" : ["A", "C", "D"],
    "C" : ["A", "B"],
    "D" : ["B"]
}

graph2 = {
    "1" : ["3","2"],
    "2" : ["1", "3", "4"],
    "3" : ["1", "2"],
    "4" : ["2"]
}


graph1 = {
    "A" : ["B","D","F"],
    "B" : ["A", "C"],
    "C" : ["B", "D"],
    "D" : ["A","C","E"],
    "E" : ["D","F"],
    "F" : ["A", "E"]
}

graph2 = {
    "1" : ["2","4","6"],
    "2" : ["1", "3"],
    "3" : ["4", "2"],
    "4" : ["1","3","5"],
    "5" : ["4","6"],
    "6" : ["1", "5"]
}

variants = {point:[] for point in graph1 }
edges = dict()

for point, edge in graph1.items():
    if edges.get(len(edge)) == None:
        edges[len(edge)] = [point]
    else:
        edges[len(edge)].append(point)

for point, edge in graph2.items():
    if edges.get(len(edge)) != None:
        for k in edges.get(len(edge)):
            variants[k].append(point)

def decart(*args):

    pools = [list(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool if y not in x]
    for prod in result:
        yield list(prod)        


def road(graph):
    roads = []
    for point, edges in graph.items():
        for edge in edges:
           roads += [point+edge ]
    return sorted(roads)

def road2(graph, ver):
    roads = []
    for point, edges in graph.items():
        for edge in edges:
           roads += [ver[point]+ver[edge]]
    return sorted(roads)


versions = []



for i in decart(*list(variants.values())):
    versions.append({l : k  for k, l in zip(variants.keys(), i)})



real_road = road(graph1)

res = [ver for ver in versions if road2(graph2, ver) == real_road]

print(res)
