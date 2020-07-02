st=[]
num=int(input("how many numbers:"))
for n in range (num):
    numbers=int(input("Enter the Number:"))

    st.append(numbers)
print("Maximum elements in the list:",max(st),"\nMinimum element in the list is :",min(st))
