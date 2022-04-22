digits=["7e","30","6d","79","33","5b","5f","70","7f","7b"]
print("v2.0 raw",end="\n")

data=[]

for v in range(256):
    data.append(digits[v%10])
for v in range(256):
    data.append(digits[(v//10)%10])
for v in range(256):
    data.append(digits[(v//100)%10])
for v in range(256):
    data.append("00")
    
ones=[]
tens=[]
hundrets=[]
sign=[]
for a in range(0,256):
    v=(a+128)%256-128
    ones.append(digits[abs(v)%10])
    tens.append(digits[(abs(v)//10)%10])
    hundrets.append(digits[(abs(v)//100)%10])
    sign.append("00" if v>=0 else "01")

data.extend(ones)
data.extend(tens)
data.extend(hundrets)
data.extend(sign)

i=0
for d in data:
    print(d,end="")
    i+=1
    if i%8==0:
        print(end="\n")
    else:
        print(" ",end="")
print(end="\n")