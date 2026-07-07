number=[]
num=[]
for x in range():
    number= int(input("Enter the inputs: "))
    num.append(number)

the_num=int ( input("Enter the number whose duplicate needs to be removed: "))
freq=number.count(the_num)
if(freq==0):
    print(the_num,"not found")
elif(freq==1):
    ("No duplicate found")
else:
    number.reverse()
    for x in range(freq-1):
        number.remove(the_num)
    number.reverse()
print(number)

