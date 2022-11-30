try:
    with open("kpr1.data","x") as k:
        print("-------------------------------------")
        print("\n file name opened in write mode successfully")
        print("Type of k=",type(k))
        print("-------------------------------------")
        print("Name of file=",k.name)
        print("file opening mode=",k.mode)
        print("Is this readable?=",k.readable)
        print("Is this writable?=",k.writable())
        print("within with open() as---line-11--->is this closed?=",k.closed)
    print("\nLine-12 outof with open() as---line-12--->is this closed?=",k.closed)
except FileNotFoundError:
    print("File name already exist")