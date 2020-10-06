#asc2.py
for i in range (0,256):
	c = chr(i)
	print("[",i,"=",c, "]",end="")
	if (i % 7 == 0):
		print()
