import random
import pyfiglet
print(pyfiglet.figlet_format("Welcome", font = "banner3-D" ))
def password_generator():
   numlist = [1,2,3,4,5,6,7,8,9,0]
   special_char_list = [",","/","%","+","&","₹","@","#","_","-",":",":","*","!","?","$"]
   alphabets =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
   password = ""
   for i in range(random.randint(16,46)):
     rand_choice = random.choice([1,2,3])
     if rand_choice == 1:
       password += str(random.choice(numlist))
     elif rand_choice == 2:
       password += random.choice(special_char_list)
     else:
       password += random.choice(alphabets)
   return password

print(f"password suggestion : {password_generator()}")