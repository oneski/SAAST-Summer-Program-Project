def is_isbn(input):

	"""TAKE ISBN RETURN TRUE IF VALID"""

def calculate_check(ISBN):
	if(len(ISBN)<=8 or len(ISBN)>=11):
		raise ValueError("Invalid String Format")
	else:
		isbn9 = ISBN[:9]
		abc = [int(a)*b for a,b in zip(list(isbn9),range(1,10))]
		print abc
		print sum(abc)%11
def isbn_sum():
	pass
calculate_check("123456789X")

"""CALCULATE THE CHECK DIGIT"""

listt = range(1,10)

print listt

listtt = list("asdf")

print listtt;

"""ZIP IS A FUNCTION THAT TAKES 2 LISTS, [1,2,3] and [a,b,c] RESULT IS TUPLE LIST[(1,a),(2,b),(3,c)]

l = [(1,a),(2,b),(3,c)]

'[(x,y) for x,y in l]'


a*b for a,b in zip(a,b)

"""