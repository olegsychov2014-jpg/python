


# for i in range(1,11):
#
#
#     d.append(i)
#     print(d)

# d=[1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
# e=0
# f=0,
# for i in d:
#         if i>0:
#            e+=1
#            print(e)
#         if i<0:
#             f+=i
#
#
#         print(f)
# g=[]
# g.append(e)
# g.append(f)
# print(g)

#
#
#
#
# b=[]
# a = [1, 3, 8, 5, 8]
# c=0
# for i in a:
#     if  i not in b:
#         b.append(i)
# for i in b:
#     c=c+i
#
#     print(b)
#     print(c)

# a =10
# b=[]
# for i in range (1,11):
#     if a not in b:
#         b.append(i)
#         print(b)







# b = []
# a = [-1, 2, 3, -4]
# c=[1,-2,-3,4]
# for i in a:
#     if i not in b:
#         b.append(c)
# print(b)





# b = []
# a = [-1, 2, 3, -4]
# c=0
# for i in a:
#     if i not in b:
#         c=i*-1
#         b.append(c)
# print(b)




# a=[1,2,3,4,5,-6,-7,-8]
# b=0
# for i in a:
#     if i>0 :
#         b=b+1
#         print(b)
#
#
#
#
#
# a=[1,2,3,4,5,-6,-7,-8]
# b=0
# for i in a:
#     if i<0 :
#         b=b-1
#         print(b)

# a=[1,2,3,4,5,-6,-7,-8]
# b=1
# for i in a:
#     if i>0 :
#         b=b*i
#         print(b)

# a=[1,2,3,4,5,-6,-7,-8]
# b=0
# c=0
# for i in a:
#    if i<0:
#     b=b+i
#    elif i>0:
#     c=c+1
#
# print(b)
# print(c)

# a=[-1,2,3,-5,3,6,6,10,11]
# b=[]
#
# for i in range (len(a)):
#     if i%2==1:
#         b.append(a[i])
# print(b)
# print(a)print

# b="+1-234-567-89-10"
# print(b.replace("-","*"))

# a="парта"
#
# if a.isalpha():
#     print("там тільки букви")
#     if a.islower():
#         print("там маленькі літери")
# elif a.isdigit():
#     print("там тіки цифри")
# else:
#     print("там букви і цифри")

# b=0
# a="авакадо"
# for i in a:
#     if a.isalpha():
#         if i=="а":
#             b=b+1
#             print("там",i,"букви а")
#             print(b)

# a="алегатор"
# a=a.replace("а","олег")
# print(a)
#
# c=0
# b=0
# a="в київі є машинa"
# for i in a:
#     if i.islower():
#         b=b+1
#     elif i.isupper():
#         c = c + 1
# print(b)
# print(c)

# a="в київі є "
# b=a.split(" ")
# e=len(b)-1
# c=a.rstrip(b[e])
# d=c.lstrip(b[0])
# print(d)


# a="в київі є машина"
# d=[]
# b=a.split()
# c=random.randint(0,3)
# e=random.randint(0,3)
# l=random.randint(0,3)
# g=random.randint(0,3)
# f=b[c]
# print(b[3])
# d.append(f)
# d.append(e)
# d.append(l)
# d.append(g)
# print(d)
# print(f)

import random
# a="в киеві є машина"
# d=[]
# b=a.split()
#
# for i in range(len(b)*2):
#     print(i)
#     c=random.randint(0,3)
#     f = b[c]
#     if f not in d:
#         d.append(f)
# print(d)

# a="hello"
# b=("a","i","e","o","u")
# for i in a:
#     if i not in b:
#         print("в речені не має голосних букв")
#     elif i in b:
#         print("в речені є голосні букви")
#
# b=["Germani " , "Belgium " ]
# final_result=[2,0]
#
# def match(spisok,rezut):
#     a=(spisok[0])
#     c=(spisok[1])
#     e=(spisok[0])
#     m="at match " + a+c
#     print(rezut[0],rezut[1])
#     g = (rezut[0])
#     p=(rezut[1])
#     if g>p:
#         m+=spisok[0] + "won "
#     elif p>g:
#         m+=spisok[1] + "won "
#     elif p==g:
#         m+="draw"
#     print(m)
# match(spisok=b,rezut=final_result)


# match(['Germany','Ukraine'],[])"at match Germani-Ukraine,germani won"
# match(['Belgium','Italy'],[])"at match-Belgium,Italy,Italy won"
# match(['Portugal','Iceland'],[])"at match Portugal-Iceland,Iceland won"

# def slova(kilikisti):
#     a= "hello"
#     b= "hello world"
#     c= "no results for term 's'"
#     d= "hello"
#     e=[]
#     f=0
#     g=0
#     e=c.split()
#     print(e)
#
# slova(split)
#
# e=0
# a="solar systems1"
# for i in a:
#     a.isalpha()
#     if i=="a":
#         e=e+1
#         print("там ",i,"буква a")
# print(e)




# a="solar systems1"
# b=["a","i","e","u","o"]
# for i in a:
#     if i in b:
#         print(i)

# b=0
# a="solar systems1"
# print(a[13])
#
#
# c=0
# a="solar s  ystems11111111111111111111a"
# for i in a:
#     c=c+1
#     print(c)
# print(a[c-1])

# c=0
# b=""
# a="hello"
# for i in a:
#     b=b+i*2
#     # print(i)
#     # print(a)
# print(b)


# c=""
# a="+--+"
# b="++--"
# for i in range(len(a)):
#         if a[i]=="+" and b[i]=="+":
#             c=c+"+"
#             print(i,"plus")
#         elif a[i]=="-" and b[i]=="-":
#             c=c+"-"
#             print(i,"mines")
#         elif a[i] == "+" and b[i] == "-":
#             c=c+"0"
#             print(i,"zero")
#         elif a[i] == "-" and b[i] == "+":
#             c = c + "0"
#             print(i, "zero")
# print(c)



































