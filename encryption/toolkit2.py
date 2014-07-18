from string import ascii_lowercase

def caesar(plaintext, key):
	print "".join([chr((ord(i) - ord("a") + key) % 26 + 97) for i in list(plaintext)])
	while True: 
		if getInput("Would you like to run again? (y or n):", lambda x: x != "y" and x != "n") == "y": caesar(plaintext, key + 1)
		else: break

def main():
	print caesar(getInput("All lowercases and no spaces please: ", lambda ans: len([i for i in list(ans) if i not in list(ascii_lowercase)])), int(getInput("Numerical key: ", lambda key: not key.isdigit())))

def getInput(prompt, condition, output = "ASDF"):
	while condition(output): output = str(raw_input(prompt))
	return output

