# return masked string
def maskify(cc):
    strCC = str(cc)

    str1 = strCC[:-4]
    str2 = strCC[-4:]
    str3 = ""

    for i in range(len(str1)):
        str3 += "#"

    return str3 + str2
