# python2.7

import json

graph = {}
graph["start"] = {}
graph["start"]["weight"] = 0

graph["start"]["e"] = {}
graph["start"]["e"]["weight"] = 14
graph["start"]["d"] = {}
graph["start"]["d"]["weight"] = 9
graph["start"]["b"] = {}
graph["start"]["b"]["weight"] = 7

graph["e"] = {}
graph["e"]["weight"] = 0
graph["e"]["f"] = {}
graph["e"]["f"]["weight"] = 9

graph["e"]["f"]["g"] = {}
graph["e"]["f"]["g"]["weight"] = 6

graph["d"] = {}
graph["d"]["weight"] = 0
graph["d"]["g"] = {}
graph["d"]["g"]["weight"] = 11

graph["b"] = {}
graph["b"]["weight"] = 0
graph["b"]["g"] = {}
graph["b"]["g"]["weight"] = 15

#print(json.dumps(graph, sort_keys=True, indent=4))

costs = {}
costs["e"] = 14
costs["d"] = 9
costs["b"] = 7

def find_min_cost_node(graph):
    min_node_cost = float("inf")
    min_node = None

    del graph["weight"]

    for node in graph:

        print node["weight"]

        if node["weight"] < min_node_cost:
            min_node_cost = costs[node]
            min_node = node

    return min_node

print find_min_cost_node(graph["start"])

