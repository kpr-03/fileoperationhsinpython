#program for counting number of lines,words and charcters of any file.
filename=input("Enter Any File Name:")
try:
	with open(filename,"r") as fp:
		lines=fp.readlines()
		nl,nw,nc=0,0,0
		for line in lines:
			nl=nl+1
			nw=nw+len(line.split())
			nc=nc+len(line)
		else:
			print("-"*50)
			print("Number of Lines={}".format(nl))
			print("Number of Words={}".format(nw))
			print("Number of Characters={}".format(nc))
			print("-"*50)
except FileNotFoundError:
	print("File Does not Exist")