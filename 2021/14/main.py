def parse_file(path):
    with open(path) as f:        
        content = f.read()
        return content.splitlines()

class Polymer:
  def __init__(self, template, rules):
    self.template = template
    self.rules = rules
    self.pairs = self.init_pairs()
    self.el_counts = self.init_el_counts()
  
  @staticmethod
  def update_dict(d, k, v):
    if k in d.keys():
      d[k] += v
    else:
      d[k] = v
    return d

  def init_pairs(self):
    pairs = {}
    for i in range(len(self.template) - 1):
      k = self.template[i] + self.template[i+1]
      self.update_dict(pairs, k, 1)
    return pairs      

  def init_el_counts(self):
    el_counts = {}
    for el in self.template:
      self.update_dict(el_counts, el, 1)
    return el_counts

  def grow(self):
    pair_copy = self.pairs.copy()
    pair_names = [k for k, v in pair_copy.items()]
    for pair in pair_names:
      if pair in self.rules.keys():
        e1 = pair[0]
        e2 = pair[1]
        e3 = self.rules[pair]
        new_pair_1 = e1+e3
        new_pair_2 = e3+e2
        self.update_dict(self.pairs, new_pair_1, pair_copy[pair])
        self.update_dict(self.pairs, new_pair_2, pair_copy[pair])
        self.update_dict(self.el_counts, e3, pair_copy[pair])
        self.pairs[pair] -= pair_copy[pair]
        pair_copy.pop(pair)


data = parse_file("./example.txt")
template = data[0]
rules = {r[:2]: r[-1] for r in data[2:]}

def solve(polymer, steps):
  for _ in range(steps):
    polymer.grow()
  return max(polymer.el_counts.values()) - min(polymer.el_counts.values())


print("q1", solve(Polymer(template, rules), 10))
print("q2", solve(Polymer(template, rules), 40))
