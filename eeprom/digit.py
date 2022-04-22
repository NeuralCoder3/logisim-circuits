from operator import mod


digits=["7e","30","6d","79","33","5b","5f","70","7f","7b"]
digits+=["7d","1f","4e","3d","4f","47"]
print("v2.0 raw",end="\n")

data=[]

for modulus in [10,16]:
    for v in range(256):
        data.append(digits[v%modulus])
    for v in range(256):
        data.append(digits[(v//modulus)%modulus])
    for v in range(256):
        data.append(digits[(v//(modulus*modulus))%modulus])
    for v in range(256):
        data.append("00")
        
    ones=[]
    tens=[]
    hundrets=[]
    sign=[]
    for a in range(0,256):
        v=(a+128)%256-128
        ones.append(digits[abs(v)%modulus])
        tens.append(digits[(abs(v)//modulus)%modulus])
        hundrets.append(digits[(abs(v)//(modulus*modulus))%modulus])
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