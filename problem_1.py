# Azat Dovgeldiyev
#02/13/2020
#I have not given or received any unauthorized assistance on this assignment.

def main():
    import os.path
    from os import path
    DL={}#creating a dictionary to hold a file

    def read_txt_file(filename,DS):
        print("Reading file",filename)
        if not path.exists(filename):#using boolean to check whether file exists or not
            print("Error: file not found")
            return ""
        f=open(filename,"r")
        txt=f.read().split()
        DL.clear()
        for num in txt:
            stem=int(num[0])
            leaf=int(num[1])
            if stem in DL:
                DL[stem].append(leaf)
            else:
                DL[stem]=[leaf]
    def display():
        print("Stem and leaf plot\n")
        if len(DL)==0:
            print("Nothing to display")
            return
        for k,v in DL.items():
            leaves=" "
            for x in sorted(v):
                leaves=leaves+" "+str(x)
            print(k,leaves)
        print()

    msg="Enter number\n1.upload a file \n2.display graph \n3.exit\nEnter choice: "
    print("Welcome")
    while True:
        i=int(input(msg))
        if i==1:
            fname=input("file name: ")
            read_txt_file(fname,DL)
        elif i==2:
            display()
        elif i==3:
            print("Exiting")
            break
        else:
            print("Wrong selection try again")

if __name__=="__main__":
    print("problem_1.py is being run directly")
    main()
