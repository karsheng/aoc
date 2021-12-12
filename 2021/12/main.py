from typing import List, Set, TypeVar 

def parse_file(path):
  f = open(path, "r")
  return [x.strip() for x in f.readlines()]

def preprocess(data):
  return [r.split("-") for r in data]

def get_nodes_names(data):
  nodes_names = set()
  for r in data:
    nodes_names.add(r[0])
    nodes_names.add(r[1])

  return nodes_names

data = preprocess(parse_file("./input.txt"))
nodes_names = get_nodes_names(data)


N = TypeVar('N', bound='Node')
class Node:
  def __init__(self, name: str):
    self.name = name
    self._neighbours = set()

  @property
  def neighbours(self) -> Set[N]:
    return self._neighbours
  
  def add_neighbour(self, node):
    self._neighbours.add(node)

def init_nodes(data, nodes_names):
  nodes = {n: Node(n) for n in nodes_names}
  for r in data:
    n1 = r[0]
    n2 = r[1]
    nodes[n1].add_neighbour(nodes[n2])
    nodes[n2].add_neighbour(nodes[n1])

  return nodes

nodes = init_nodes(data, nodes_names)


def solve_1(node: Node, visited: List[str], pc : int = 0):
  visited.append(node.name)
  for neighbour in node.neighbours:
    if neighbour.name.lower() not in visited and neighbour.name != "end":
      pc = solve_1(neighbour, visited, pc)
    if neighbour.name == "end":
      pc += 1
  visited.pop()
    
  return pc

print("q1", solve_1(nodes["start"], []))

def check_small_caves(visited: str):
  small_caves_visit_count = { c: 0 for c in visited if c.lower() in visited }
  for c in visited:
    if c in small_caves_visit_count.keys():
      small_caves_visit_count[c] += 1

  return any([v == 2 for v in small_caves_visit_count.values()])
  

def solve_2(node: Node, visited: List[str], pc : int = 0):
  visited.append(node.name)
  for neighbour in node.neighbours:
    if neighbour.name.lower() not in visited and neighbour.name != "end":
      pc = solve_2(neighbour, visited, pc)
    if neighbour.name.lower() in visited and not check_small_caves(visited) and neighbour.name != "start":
      pc = solve_2(neighbour, visited, pc)
    if neighbour.name == "end":
      pc += 1
  visited.pop()
    
  return pc

print("q2", solve_2(nodes["start"], []))
