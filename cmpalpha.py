text=input("enter char:")
str=[]
for i in range(len(text)):
    if text[i]>='a'and text[i]<='z':
       if text[i]=='a':
          str.append('A')
       if text[i]=='b':
          str.append('B')
       if text[i]=='c':
          str.append('C')
       if text[i]=='d':
          str.append('C')  
       if text[i]=='e':
          str.append('E')
       if text[i]=='f':
          str.append('F')
       if text[i]=='g':
          str.append('G')
for i in range(len(str)):
     print(str[i])
         
        