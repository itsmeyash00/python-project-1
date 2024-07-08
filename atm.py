amt=int(input("enter your amount"))
rs=int(amt/2000)
remain1=amt%2000

nt_500=remain1//500
remain2=remain1%500

nt_200=remain2//200
remain3=remain2%200

nt_100=remain3//100
remain4=remain3%100

nt_50=remain4//50
remain5=remain4%50

print("the 2000 notes are",rs )
print("the 500 notes are",nt_500)
print("the 200 notes are",nt_200)
print("the 100 notes are",nt_100)
print("the 50 notes are",nt_50)

