def is_isbn(ISBN):
	"""TAKE ISBN RETURN TRUE IF VALID"""
	if not(isinstance(ISBN, basestring)):
		raise ValueError("Invalid Format")
	else:
		if(len(ISBN)!=10):
			raise ValueError("Invalid String Format")
		else:
			checkDigit = calculate_check(ISBN)
			if(checkDigit == 10):
				checkDigit = "X"
			if(checkDigit == ISBN[9]):
				return True
			else:
				return False

def calculate_check(ISBN):
	"""CALCULATE THE CHECK DIGIT"""
	if not(isinstance(ISBN, basestring)):
		raise ValueError("Invalid Format")
	else:	
		if(len(ISBN)<=8 or len(ISBN)>=11):
			raise ValueError("Invalid String Format")
		else:
			return sum([int(a)*b for a,b in zip(list(ISBN[:9]),range(1,10))])%11

print calculate_check("123456789X")
print is_isbn("123456789X")


#TO DO:

#ERROR PREVENT IS_ISBN FOR 10 DIGIT String
#BUG FIX