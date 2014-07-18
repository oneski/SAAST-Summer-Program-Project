from string import ascii_lowercase

def caesar(plaintext, key, recc = 0):
	print "".join([chr((ord(i) - ord("a") + key) % 26 + 97) for i in list(plaintext)])
	while getInput("Would you like to run again? (y or n):", lambda ans: len([i for i in list(ans) if i not in list(ascii_lowercase)]))=="y" and recc == 0: (caesar(plaintext, key + 1,1))

		#(caesar(plaintext, key + 1))
		#(caesar(plaintext, key + 1))
		#lambda ans: len([i for i in list(ans) if i not in list(ascii_lowercase)])
		#Lambda x: x == "y" or x == "n")=="y"		

def main():
	print caesar(getInput("All lowercases and no spaces please: ", lambda ans: len([i for i in list(ans) if i not in list(ascii_lowercase)])), int(getInput("Numerical key: ", lambda key: not key.isdigit())))

def getInput(prompt, condition, output = "False"):
	while condition(output): output = str(raw_input(prompt))
	return output

main()