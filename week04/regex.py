import re


def find_name(line):
    pattern = r"([A-Za-z][-,A-Za-z. ']+[ ]*)+"
    result = re.findall(pattern,line)
    
    pattern = r'(?:Mr|Mrs|Ms|Miss|Madame|Mme|Dr|Prof|Sr)\.?\s+\w[A-Za-z]+\s+\w[A-Za-z]+'
    result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)
