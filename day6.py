def dna():
	output = []
	inputFile = raw_input("DISH DAT INPUT FILE BRAHHHHHHHHHHHHH! \n - VIVIAN, brothority\nInput File:	")
	outputFile = raw_input("Can you please give me a location to output your results? \n Thank you! \n - David Silverman (dsilvs)\nOutput File:	")
	f = open(inputFile).readlines()
	#f.split("\n")
	g = [item.replace("\n","") for item in f]
	#print g
	for i in range(0,len(g)):
		if(i%2==0):
			output += ["Region Name: %s \n" % (g[i])]
		else:
			output += ["Nucleotides: %s \n" % (g[i].replace("-","").upper())]
			output += ["Nuc. Counts: %s \n" % (str([g[i].upper().count("A"),g[i].upper().count("C"),g[i].upper().count("G"),g[i].upper().count("T")]))]
			totalMass = [float(g[i].upper().count("A")*135.128),float(g[i].upper().count("C")*111.103),float(g[i].upper().count("G")*151.128),float(g[i].upper().count("T")*125.107),float(g[i].count("-")*100.000)]
			output += ["Total Mass%: [{0:.2f},{1:.2f},{2:.2f},{3:.2f}] of {4:.2f} \n".format((totalMass[0]/float(sum(totalMass)))*100,(totalMass[1]/float(sum(totalMass)))*100,(totalMass[2]/float(sum(totalMass)))*100,(totalMass[3]/float(sum(totalMass)))*100,float(sum(totalMass)))]
			codonFull = []
			codonInProduction = []
			h = list(g[i].replace("-","").upper())
			for i in range(0,(len(h))):
				if(i%3 == 2):
					codonInProduction += [h[i]]
					codonFull += ["".join(codonInProduction)]
					codonInProduction = []
				else:
					codonInProduction += [h[i]]

			output += ["Codons List: %s \n" % (str(codonFull))]
			if(codonFull[0] == "ATG" and ((codonFull[len(codonFull)-1]) == "TAA" or codonFull[len(codonFull)-1] == "TAG" or codonFull[len(codonFull)-1] == "TGA")) :
				output += ["Is Protein?: YES \n"]
			else:
				output += ["Is Protein?: NO \n"]
			output += ["\n"]
			#ACGT
		i += 1
	with open(outputFile, "w'") as s:
		s.writelines(output)
	return output
	output = g
dna()