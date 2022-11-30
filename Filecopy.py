#program for copying the content of one file(source file) into another file(destination file)
sfile=input("Enter source file name:")
try:
    with open(sfile,"r") as rp:
        dfile=input("enter destination file:")
        with open(dfile,"a") as wp:
            srcfiledata=rp.read()
            wp.write(srcfiledata)
            print("\nFile copy process completed!!!")
except FileNotFoundError:
    print("File doesnot exists")