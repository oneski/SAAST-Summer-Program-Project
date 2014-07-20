"""import inspect, os


x = inspect.getfile(inspect.currentframe()).split("/")[len(inspect.getfile(inspect.currentframe()).split("/"))-1][4:len(inspect.getfile(inspect.currentframe()).split("/")[len(inspect.getfile(inspect.currentframe()).split("/"))-1])-3]						



with open("bomb"+str(x)+".py") as g:
	runningfile = g.readlines()

if int(x) < 50:

	if int(x) == 0:
		os.chdir("../")
		print os.system("ls")
		os.system("mv bomb .bomb")
		os.chdir(".bomb")
	filename = "bomb" + str(int(x) + 1) + ".py"
	with open(filename, "w") as f:
		f.writelines(runningfile)
	os.system("python bomb" + str(int(x) + 1) + ".py")

	"""