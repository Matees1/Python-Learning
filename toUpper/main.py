
def correctCap(string):
    r = string[0].upper() + string.replace(string[0], "")
    return r

phrase = correctCap("fix me plss")
print(phrase)