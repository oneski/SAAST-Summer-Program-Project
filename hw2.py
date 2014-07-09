def is_isbn(input):

	"""TAKE ISBN RETURN TRUE IF VALID"""

def calculate_check(ISBN):
	"""CALCULATE THE CHECK DIGIT"""
	if(len(ISBN)<=8 or len(ISBN)>=11):
		raise ValueError("Invalid String Format")
	else:
		return sum([int(a)*b for a,b in zip(list(ISBN[:9]),range(1,10))])%11


calculate_check_test("123456789X")


"""ZIP IS A FUNCTION THAT TAKES 2 LISTS, [1,2,3] and [a,b,c] RESULT IS TUPLE LIST[(1,a),(2,b),(3,c)]

l = [(1,a),(2,b),(3,c)]

'[(x,y) for x,y in l]'


a*b for a,b in zip(a,b)

"""