f_num=int(input("Enter your first number"))
s_num=int(input("Enter your Second number"))

all_f_num= id(f_num)
print("location of First Number :" , all_f_num)

hex_s_num= hex(s_num)
print("location of Second Number :" , hex_s_num)

no1= f_num + s_num
print("Answer of  addition =" , no1)


if f_num > s_num :
    no2=f_num-s_num
    print("Answer of subtration =" ,no2)
    
else :
     no2=s_num-f_num
     print("Answer of subtration =" , no2)
     
no3= f_num * s_num
print("Answer of multiplication =" , no3)


if f_num > s_num :
    no4=f_num//s_num
    print("Answer of division =" ,no4)
    
else:
    no4=s_num//f_num
    print("Answer of division =" ,no4 )
     
all_no1= id(no1)
print("location of No1 :" , all_no1)
     
all_no2= id(no2)
print("location of No2 :" , all_no2)
     
all_no3= id(no3)
print("location of No3 :" , all_no3)
     
all_no4= id(no4)
print("location of No4 :" , all_no4)

hex_no1= hex(no1)
print("location of No1 :" , hex_no1)
     
hex_no2= hex(no2)
print("location of No2 :" , hex_no2)
     
hex_no3= hex(no3)
print("location of No3 :" , hex_no3)
     
hex_no4= hex(no4)
print("location of No4 :" , hex_no4)
     
     


        



