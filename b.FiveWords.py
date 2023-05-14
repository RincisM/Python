print("Enter 5 words")
c =[]
for i in range (1,6):
    a = input("")
    c.append(a)
for word in c:
    if(len(word)<6):
        print("Re-enter the word", word)
        d = input(("Enter a word greater than 6 characters: "))
        e = c.index(word)
        c.remove(word)
        c.insert(e, d)
print("The Words are: ")
print(c)