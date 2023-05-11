print("To end the loop enter -1")
even=0
odd=0
evenset=[]
oddset=[]
print("Enter the Numbers: ")
while True:
    a=int(input())
    if(a==-1):
        break
    if(a%2==0):
        evenset.append(a)
        even = even+1
    if(a%2!=0):
        oddset.append(a)
        odd = odd+1
print("The Count of Even Numbers: ", even, "\nThe Numbers are: ", evenset)
print("The Count of Odd Numbers: ", odd, "\nThe Numbers are: ", oddset)