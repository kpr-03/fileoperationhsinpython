#program for reading the data from keyboard and write it to the file
with open("pat.data","a")as fp:
    print("enter the data and press stop to terminate")
    print("="*50)
    while(True):
        inputdata=input()
        if inputdata.lower()!="stop":
            fp.write(inputdata +"\n")
        else:
            print("="*50)
            break