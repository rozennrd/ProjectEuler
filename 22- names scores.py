from Timer import Timer

time = Timer()
time.start()
def convert_to_number(word):
    return sum([ord(char) - 96 for char in word])

with open("names.txt","r") as file:
    fileconverted = file.read()
    noms = sorted([nom.strip('"').lower() for nom in fileconverted.split(',')])
    print(sum([(ind+1) * convert_to_number(nom) for ind, nom in enumerate(noms)]))
time.stop()
print(time.elapsed)