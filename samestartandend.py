stringslist = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]
samestring = [""] 
notsamestring = [""] 
i = 0
while 0 < len(stringslist):
    string = stringslist[i][0] == stringslist[i][-1]
    if stringslist[i][0] == stringslist[i][-1]:
        samestring.append(string)
        i = 0 + 1
    else:
        notsamestring.append(string)
        i = i + 1
samestringnum = (len(samestring))
print(f"The number of characters that are the same at the beginning, and end of an element of the list are:",samestringnum)