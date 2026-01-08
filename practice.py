list1=["Melissa", "Heloise","Shami"]
for x in list1:
    print(x)
else:
    print("what is this its so fascinating")    
print(len(list1))    

#List comprehension is also impressive
fruits=["banana","mango","apple","gitub","linkedin"]
newlist=[x for x in fruits if "a" in x]