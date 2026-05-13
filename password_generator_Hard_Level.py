import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
Numbers = ['0','1','2','3','4','5','6','7','8','9']
Symbols = ['!','#','$','%','&','*',(','),'+']

print("welcome to the pypossword generator!")

nr_Letters = int(input("How many letters would you like in your password\n"))
nr_Numbers = int(input("How many numbers would you like in your password\n"))
nr_Symbols = int(input("How many Symbols would you like in your password\n"))


#Hard Level
password_list = []
for char in range(0,nr_Letters):
    password_list.append(random.choice(Letters))
for char in range(0,nr_Numbers):
    password_list.append(random.choice(Numbers))
for char in range(0,nr_Symbols):
    password_list.append(random.choice(Symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password += char
print(f"final password is :{password}")
