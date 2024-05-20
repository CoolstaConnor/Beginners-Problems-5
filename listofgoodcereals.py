cereal = False
cereallist = []
while not cereal:
    cereal = input("Enter a Cereal: ")
    if cereal == "sultana bran" or cereal == "weetbix":
        cereallist.append(cereal)
        print(cereallist)
        cereal = True
        break
    if cereal != "sultana bran" or cereal != "weetbix":
        cereallist.append(cereal)
        cereal = False
        continue