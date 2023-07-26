from typing import List
from random import Random

class Node:
	pass

class Composite(Node):
	def __init__(self):
		self.Rules = []

	def append_rule(self, rule : List[Node]):
		self.Rules.append(rule)
		return self

class Tokens(Node):
	def __init__(self, tokens : List[str]):
		self.Tokens = tokens;


class Empty(Node):
	pass


Nouns = Tokens(["Donald Trump", "S. N. Goenka", "Mary Jane", "Paris"])
Verbs = Tokens(["eats", "enrages", "meditates on", "thanks"])
Joiners = Tokens(["and", "but", "because"])

Sentence = Composite()
Sentence.append_rule([ Nouns, Verbs, Nouns ]).append_rule([ Nouns, Verbs, Nouns ]).append_rule([ Sentence, Joiners, Sentence ])

def generate_random_sentences(num : int, seed : int, ruleset : Node) -> List[str]:
	strs = [];
	rand = Random()
	rand.seed(0)

		
	while num >= 0:
		# do a random depth first search
		cur_stack = [ruleset]
		cur_str = ""
		while len(cur_stack) != 0:
			cur_node = cur_stack.pop()
			if isinstance(cur_node, Empty):
				pass
			elif isinstance(cur_node, Tokens):
				rand_index = rand.randrange(0, len(cur_node.Tokens))
				rand_str = cur_node.Tokens[rand_index]
				cur_str += " " + rand_str
			elif isinstance(cur_node, Composite):
				rand_index = rand.randrange(0, len(cur_node.Rules))
				rand_rule = cur_node.Rules[rand_index]# todo!
				for node in reversed(rand_rule): # not 100% sure this is right
					cur_stack.append(node)
			else:
				raise "Impossible"
			
		strs.append(cur_str)
		num -= 1
	return strs

# quite hard skipping for now
def is_valid(sentence : str, ruleset : Node):
	pass

strs = generate_random_sentences(5, 0, Sentence)
print("generating stuff")
for str in strs:
	print(str)
