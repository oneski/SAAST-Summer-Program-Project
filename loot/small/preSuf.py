from random import randint

def preSuf(a):
	roll = a
	#print roll
	if(roll == 0):
		return ("","","","")
	elif(roll == 1):
		f = open("MagicPrefix.txt").readlines()
		f = [item.replace("\n", "").split(",") for item in f[1:len(f)]]
		selector = randint(0,len(f)-1)
		attibute = str(randint(int(f[selector][2]),int((f[selector][3])))) + " " + str(f[selector][1])

		return (f[selector][0]+ " ", attibute,"","")
	elif(roll == 2):
		f = open("MagicSuffix.txt").readlines()
		f = [item.replace("\n", "").split(",") for item in f[1:len(f)]]
		selector = randint(0,len(f)-1)
		attibute = str(randint(int(f[selector][2]),int((f[selector][3])))) + " " + str(f[selector][1])
		
		return ("",""," "+f[selector][0], attibute)
	else:
		pref = preSuf(1)
		suff = preSuf(2)
		return (pref[0],pref[1],suff[2],suff[3])

	"""else:
		f = open("MagicPrefix.txt").readlines()
		f = [item.replace("\n", "") for item in f[1:len(f)]]
		f = [item.split(",") for item in f]
		selector = randint(0,len(f)-1)
		attibute = str(randint(int(f[selector][2]),int((f[selector][3])))) + " " + str(f[selector][1])

		g = open("MagicSuffix.txt").readlines()
		g = [item.replace("\n", "") for item in g[1:len(g)]]
		g = [item.split(",") for item in g]
		selector2 = randint(0,len(g)-1)
		attibute2 = str(randint(int(g[selector2][2]),int((g[selector2][3])))) + " " + str(g[selector2][1])

		print (f[selector][0],attibute,g[selector][0],attibute2)
		return (f[selector][0],attibute,g[selector][0],attibute2)"""
	#f = open(inputFile).readlines()

print preSuf(randint(0,3))