def readfile(filename):
    try:
        with open(filename,"r")as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file{filename}is not found")


readfile("f1.py")
readfile("f2.py")
readfile("f3.py")
t=(12,23,34,45)
t.del(12)
