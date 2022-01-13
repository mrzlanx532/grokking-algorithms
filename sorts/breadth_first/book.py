# python2.7
# Breadth first algorithm. O(count_of_nodes + count_of_edges)

from collections import deque

example_graph = {}
example_graph["you"] = ["alice", "bob", "claire"]
example_graph["bob"] = ["anuj", "peggy"]
example_graph["alice"] = ["peggy"]
example_graph["claire"] = ["thom", "jonny"]
example_graph["anuj"] = []
example_graph["peggy"] = []
example_graph["thom"] = []
example_graph["jonny"] = []

search_queue = deque()
search_queue += example_graph["you"]

def search():
    search_queue = deque()
    search_queue += example_graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller"
                return True
            else:
                search_queue += example_graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search()