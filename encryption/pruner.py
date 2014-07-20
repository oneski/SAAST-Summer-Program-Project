with open("manualList.txt") as f:
	f = f.readlines()


f = [x.replace("\n","") for x in f]
f = [x.lower() for x in f if len(x)== 11]
f = [x for x in f if x.count("a")<3]
f = [x for x in f if x.count("b")<2]
f = [x for x in f if x.count("c")==0]
f = [x for x in f if x.count("d")<4]
f = [x for x in f if x.count("e")<6]
f = [x for x in f if x.count("f")==0]
f = [x for x in f if x.count("g")<5]
f = [x for x in f if x.count("h")==0]
f = [x for x in f if x.count("i")<7]
f = [x for x in f if x.count("j")==0]
f = [x for x in f if x.count("k")<2]
f = [x for x in f if x.count("l")<3]
f = [x for x in f if x.count("m")==0]
f = [x for x in f if x.count("n")<3]
f = [x for x in f if x.count("o")==0]
f = [x for x in f if x.count("p")<2]
f = [x for x in f if x.count("q")==0]
f = [x for x in f if x.count("r")<3]
f = [x for x in f if x.count("s")<4]
f = [x for x in f if x.count("t")<3]
f = [x for x in f if x.count("u")==0]
f = [x for x in f if x.count("v")==0]
f = [x for x in f if x.count("w")<3]
f = [x for x in f if x.count("x")==0]
f = [x for x in f if x.count("y")==0]
f = [x for x in f if x.count("z")==0]
f = [x+"\n" for x in f]
with open("manualList2.txt", "w") as g:
	g.writelines(f)

with open("manualList2.txt") as ww:
	w = ww.readlines()

print len(w)


#aabdddeeeeeeggggiiiiiikllnnprrsssttwwwww