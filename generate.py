from typing import List

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
Sentence.append_rule([ Nouns, Verbs, Nouns ]).append_rule([ Sentence, Joiners, Sentence ])

def generate_random_sentences(num : int, seed : int, ruleset : Node) -> str:
	pass

# quite hard skipping for now
def is_valid(sentence : str, ruleset : Node):
	pass
