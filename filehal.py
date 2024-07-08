data=input("enter your data=")
with open('mydata.txt','a') as file:
    file.write(f'{data}\n')
with open('mydata.txt','r')as file:
    mydata=file.read()
    print(mydata)
