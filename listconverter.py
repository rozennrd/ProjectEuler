
def converter(input):
    str ="["
    for string in input :
        str += "["
        for carac in string:
            if carac == " ":
                str += ", "
            elif string.index(carac) == len(string) -1:
                str += carac + "]"
            else:
                str += carac
        if input.index(string) == len(input) - 1:
            str += "]"
    return str

with open("exercice67.txt", "r") as file:
    triangle = file.readlines()
    for l in triangle:
        l = l.strip()
        l = l.strip('"')
        l = l.split(" ")
        try :
            l = [int(x) for x in l]
        except ValueError:
            pass
        print(l)
    # print(converter(triangle))


