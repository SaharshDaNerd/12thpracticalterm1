import pickle
f = open("record.bin", "rb")
try:
    while True:
        ruh = pickle.load(f)
        print(ruh)
except EOFError:
    f.close()
