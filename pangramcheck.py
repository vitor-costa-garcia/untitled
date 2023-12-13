import string

def ispangram(str1):
    newstring = sorted(set(str1.lower().replace(' ','a')))
    if newstring == list(string.ascii_lowercase):
        return True
    else:
        return False
