###FILE FOR HW 3
###PARTNER = VIVIAN
""" 							   <s>

				<np>								<vp>
		<dp><adjp><n>  | <pn>      			<tv><np> |  <iv>
					2									2	


			2			2															8
		<dp>			<adjp>														<n>
	"the" | "a"		<adj>  |  <adj><adjp>		"dog" | "cat" | "man" | "university" | "father" | "mother" | "child" | "television" 

							6																		7
						<pn>																		<adj>
	"John" | "Jane" | "Sally" | "Spot" | "Fred" | "Elmo"			"big" | "fat" | "green" | "wonderful" | "faulty" | "subliminal" | "pretentious"

						4															4
					<tv>														<iv>
		"hit" | "honored" | "kissed" | "helped" 				"died" | "collased" | "laughed" | "wept"
"""
from random import randint

def s():
	return np().capitalize() + " " + vp() + "."

def np():
	if(randint(0,1)):
		return pn()
	else:
		return dp() + " " + adjp() + " " + n()

def vp():
	if(randint(0,1)):
		return tv() + " " + np()
	else:
		return iv()

def dp():
	return ["the","a"][randint(0,1)]

def adjp():
	if(randint(0,1)):
		return adj() + " " + adjp()
	else:
		return adj()

def adj():
	return ["big" , "fat" , "green" , "wonderful" , "faulty" , "subliminal" , "pretentious"][randint(0,6)]

def n():
	return ["dog", "cat", "man", "university", "father", "mother", "child", "television"][randint(0,7)]

def pn():
	return ["John", "Jane", "Sally", "Spot", "Fred", "Elmo"][randint(0,5)]

def tv():
	return ["hit", "honored", "kissed", "helped"][randint(0,3)]

def iv():
	return ["died", "collased", "laughed", "wept"][randint(0,3)]

print s()