import re
def parse_int(string):
    string_to_int = {       'ze': 0,
                            'on': 1,
                            'tw': 2,
                            'th': 3,
                            'fo': 4,
                            'fi': 5,
                            'si': 6,
                            'se': 7,
                            'ei': 8,
                            'ni': 9,
                            'te': 10,
                            'el': 11 }
    no_space = re.split('[ -]', string)
    endnum,tempnum = 0,0
    for index, num in enumerate(no_space):
        if num[-3:-1] == 'ee':                          ## Checks thirteen - nineteen
            tempnum += string_to_int[num[0:2]] + 10
        elif num[-1] == 'y':                            ## Checks twenty - ninety
            tempnum += string_to_int[num[0:2]]*10
        elif num == "hundred":
            tempnum *= 100
        elif num == "thousand":
            tempnum *= 1000
            endnum += tempnum
            tempnum = 0
        elif num == "million":
            tempnum *= 1000000
        elif num == "and":
            pass
        elif num == "twelve":                           ## Twelve ruins everything
            tempnum += 12
        else:
            tempnum += string_to_int[num[0:2]]
    endnum += tempnum
    return endnum
ans = input("Write down a number: ")
print(parse_int(ans))