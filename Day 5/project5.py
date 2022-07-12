import random
print("Welcome to the Password Generator")
l=int(input("How many letters would you like in your passwords: "))
s=int(input("How many symbols would you like: "))
n=int(input("How many numbers would you like: "))
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

#easy level:
# pwd=""
# for char in range(1,l+1):
#     pwd=pwd+random.choice(letters)

# for char in range(1,s+1):
#     pwd=pwd+random.choice(symbols)

# for char in range(1,n+1):
#     pwd=pwd+random.choice(numbers)

# print(pwd)

#hard level:
pwd_list=[]
for char in range(1,l+1):
    pwd_list.append(random.choice(letters))

for char in range(1,s+1):
    pwd_list.append(random.choice(symbols))

for char in range(1,n+1):
    pwd_list.append(random.choice(numbers))

random.shuffle(pwd_list)

password=""
for char in pwd_list:
    password+=char

print("Your final password is: ",password)