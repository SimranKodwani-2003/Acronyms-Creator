a=input("Enter your phrase")
b=a.split()
c="".join(word[0].upper() for word in b)
print(c)

