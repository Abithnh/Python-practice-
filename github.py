n=int(input("enter a number:"))
total=0
count=0
for i in range(1,n+1):
    if i%2==0:
        total=total+i
        count=count+1
print("total of even numbers",total)
print("even numbers",count)
