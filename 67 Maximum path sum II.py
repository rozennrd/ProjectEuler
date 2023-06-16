
triangle = []

with open("exercice67.txt", "r") as file:
    fileconverted = file.readlines()
    for l in fileconverted:
        l = l.strip()
        l = l.strip('"')
        l = l.split(" ")
        l = [int(x) for x in l]
        print(l)
        triangle.append(l)



for indice, row in enumerate(triangle[1:]):
    current = triangle[indice]
    next = triangle[indice + 1]
    for ie, element in enumerate(row) :
        if ie == 0 :
             next[0] = element + current[0]
        elif ie == len(row)-1:
            next[-1] = element + current[-1]
        else:
            a = element + current[ie-1]
            b = element + current[ie]
            next[ie] = max(a, b)
    print(row)

print(max(triangle[-1]))