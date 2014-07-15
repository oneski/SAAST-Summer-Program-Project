import random
grammar = { "<s>" : ["<np> <vp"]
			,"<np>" : ["<dp> <adjp> <n>","np>"]
			, "<dp>" :	["<dp> <adjp> <n>", "<np>"]
			, ""
}


def make_grammar(filename):
	#string -> map(string)
	pass

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


