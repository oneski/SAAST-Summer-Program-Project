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

def vignere(ctfilename = "dracula-enc.txt", keyfilename = "dracula-keywords.txt"):
	with open(ctfilename) as f:
		cypherText = f.readlines()
	with open(keyfilename) as g:
		keys = [x for x in g.readlines() if x != "\n"]
	print cypherText
	print keys
	for i in range(len(keys)):
		print vignereDecrypter(cypherText[i].strip(), keys[i].strip())
		
def vignereDecrypter(line, key):
	return "".join([addChars(line[i], key[i % len(key)]) for i in range(len(line))])

def addChars(a, b):
	return chr((ord(a) - ord(b)) % 26 + 97)

def onetimepad(ciphertext, key):
	if len(ciphertext) == len(key):
		return "".join([addChars(ciphertext[i], key[i]) for i in range(len(ciphertext))])
	else:
		raise ValueError("Ciphertext and key were not same length.")

def subCipher(ciphertext, filename = "subst-table-ex.txt"):
	subDict = tbl(filename)

	return "".join( [subDict[char] for char in ciphertext] )

def tbl(filename):
	output = {}

	with open(filename) as f:
		lines = f.readlines()

	for i in range(26):
		output[chr(i + 97)] = lines[i].strip()
        
	return output

print subCipher("edddaikglyedh\
ltkllktvkuvnalooh\
txvgtxvddtlktxvh\
rvtdlhvqivltih\
qldbvktxgpdlyqygw\
aikgxlkxtlelyedh\
aookxgwtxvirhilbaye\
txvitxvvuanvytvdgs\
ihypnovldrgir")