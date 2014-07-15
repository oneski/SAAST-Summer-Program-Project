'''
import random
grammar = { "<s>" : ["<np> <vp"]
			,"<np>" : ["<dp> <adjp> <n>","np>"]
			, "<dp>" :	["<dp> <adjp> <n>", "<np>"]
			, "<adjp>" : ["<adj>","<adj> <adjp>"]
			, "<adj>" : ["big,""fat","green|wonderful|faulty|subliminal|pretentious"]
			,"<n>" : ["dog","cat","man","university","father","mother","child","television"]
			,"<pn>" : ["John|Jane|Sally|Spot|Fred|Elmo"]
			,"<vp>" : ["<tv> <np>","<iv>"]
			,"<tv>" : ["hit","honored","kissed","helped"]
			,"<iv>" : "died","collapsed","laughed","wept"]
}
'''

def make_grammar(filename):
	#string -> map(string
	s = []
	diction = {}
	f = open(filename).readlines()
	f = [item.replace("\n", "") for item in f]
	g = [item.split("::=") for item in f]
	for i in range(0, len(g)):
		g[i][1] = g[i][1].split("|")

	for i in range(0, len(g)):
		diction[g[i][0]] = g[i][1]
	return diction
	

def generate(grammer, tok):
	#0. Determine if tok is a terminal or non-terminal
	#1. Figure out the alternatives for the non-termal
	#2. Choose one at random
	#3. Return the string formed by concatenating all the terinals and results of expanding the non-terminals together.
	if tok not in grammar:
		return tok
	else:
		rules = grammar[tok]
		alt = rules[random.randint(0,len(rules)-1)]
		toks = alt.split()
		return " ".join([generate(grammar, tok) for tok in toks])

print make_grammar("sentence_grammar.txt")
print make_grammar("operations.txt")