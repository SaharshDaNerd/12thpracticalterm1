import pickle
f = open("record.bin", "wb")
a = input("What to write in the file? ")
pickle.dump(a, f)
f.close()
