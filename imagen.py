from PIL import Image
import random
import numpy as np
import matplotlib.pyplot as plt
import math


x=Image.open("7p.png")
x.show()
image_arreglo = np.array(x)
image_conc=np.concatenate(image_arreglo)
#numero de pixeles
# 5p m=25
# 10p m=100
# 7p m=49
m=49
data = [1]*m
data_str = [1]*m
count=0
raiz=int(math.sqrt(m))
print(image_arreglo,raiz)
for i in range(0,raiz):
    for j in range(0,raiz):
        if image_arreglo[i][j]==1:
            data_str[count]=str(1)
            data[count]=1
            count=count+1
        else:
            data_str[count]=str(0)
            data[count]=0
            count=count+1
print(data)
print(len(data))
print(data_str)

print(len(data_str))
mul=len(data)
mul2=mul
#Si no es multiplo de n
if mul%3!=0:
    while True:
        mul=mul+1
        if mul%3==0:
            break
    mul3=mul-mul2
    for i in range(0,mul3):
        data_str.append("0")
    print(data_str)
    print(len(data_str))
rep=mul/3
rep=int(rep)
data_n = [1]*rep
counte=0
for i in range(0,rep):
        counte=3*i
        data_n[i]=data_str[counte]+data_str[counte+1]+data_str[counte+2]
        print(data_n[i])
grados = [1]*rep
for i in range(0,rep):
        if data_n[i]=="000":
            grados[i]=-112.5
        if data_n[i]=="100":
            grados[i]=112.5
        if data_n[i]=="010":
            grados[i]=-67.5
        if data_n[i]=="110":
            grados[i]=67.5
        if data_n[i]=="001":
            grados[i]=-157.5
        if data_n[i]=="101":
            grados[i]=157.5
        if data_n[i]=="011":
            grados[i]=-22.5
        if data_n[i]=="111":
            grados[i]=22.5
for i in range(0,rep):
    print(grados[i])
#probando git
fc=1000
t=np.arange(0,1/fc,(1/fc)/1000)
#t=np.arange(100,10/fc,(1/fc)/100)
print(t)
print(grados[0])
for i in range(0,11):
    rad=math.radians(grados[i])
    print(grados[i])
    if i==0:
        sen1 = np.sin(2*math.pi*t*fc+rad)
    else:
        sen1= np.concatenate((sen1,sen2), axis=0)
    rad=math.radians(grados[i+1])
    sen2 = np.sin(2*math.pi*t*fc+rad)

plt.figure()
plt.plot(sen1,c='r')
plt.xlabel('Tiempo uS')
plt.ylabel('Amplitud')
plt.title("Onda en 8-PSK")
plt.show()
