setA = {1 ,2 , 3 , 4, 5 , 6}
setB = {1 , 2 , 3}
print(setA.issuperset(setA))


hi = 'About me'
name = "Hi , Muhammmad Umar"
title = """For example following statement 
works well in Python"""



if 'Look' in 'Look into my eyes':
    print("Found")
else:
    print("Not Found")



x = 20
y = 0

if x or y:
    print("At least one is true")
else:
    print("Both are false")

if x and y:
    print("Both are true")
else:
    print("At least one is false")






type = ['yes' , 'no' , 'true' , 'false']

if 'yes'in type:
    print("Found")
else:
    print("Not Found")




if 'rost' in "Hello world rost":
    print("Found")
else :
    print("Not Found")



if 'trues' in ['yes' , 'no' , 'true' , 'false']:
    print("Found")
else:
    print("Not Found")




name = "Muhammad Umar"

if name == "Joe":
    print("Hello Joe")
elif name == "John":
    print("Hello John")
elif name == "Mith Kavins":
    print("Hello Mith Kavins")
elif name == "Muhammad Umar":
    print("Hello Muhammad Umar")
elif name == "Sara":
    print("Hello Sara")
else:
    print("Hello Stranger")




get_Names = {
    'Joe' : 'Hello Joe',
    'John' : 'Hello John',
    'Mith Kavins' : 'Hello Mith Kavins',
    'Muhammad Umar' : 'Hello Muhammad Umar',
    'Sara' : 'Hello Sara'
}
name1 = get_Names.get('Joe' , "I don't know who you are!")
print(name1)
name2 = get_Names.get('Alica' , "I don't know who you are!")
print(name2)




x = 2

if x == 1: print("One"); print("Single"); print("Uno");
elif x == 2: print("Two"); print("Double"); print("Dos");
elif x == 3: print("Three"); print("Triple"); print("Tres");
else: print("Something else"); print("Algo mas");




x = 3
y = 2

if y > x:
    x == y
    print("X is now equal to Y")
else:
    y == x
    print("Y is now equal to X")


x = 4

s = ('Olma' if (x == 1) else
     'Banan' if (x == 2) else
     'Limon' if  (x == 3) else
     'Qovun' if (x == 4) else
     'Tarviz'
)
print(s)



def Check_Age(age):
    if age < 18 and age == 18:
        return "Siz biznig korhanamizda ishlay olmaysiz"
    elif age > 20 and age == 20:
        return "Siz biznig korhanamizda ishlashingiz mumkin lekin ba'zi cheklovlar bilan"
    elif age > 25 and age == 25:
        return "BIzga sizga oxshagan kadrlar juda kerak edi"
    elif age < 60 and age == 60:
        return "Siz nafaqaga chiqqansiz"
    else: 
        return "Iltimos yoshingizni to'g'ri kiriting"
    

nam1 = Check_Age(20)
print(nam1)






# def baxo_Ber(ball):
#     if ball >= 90:
#         return "A"
#     elif ball >= 80:
#         return "B"
#     elif ball >= 70:
#         return "C"
#     elif ball >= 60:
#         return "D"
#     else:
#         return "F"
    
# natija = baxo_Ber(62)
# print(natija)


natijani  = int(input("Iltimos ballingizni kiriting: "))

def baxo_Ber(ball):
    if ball > 90 or ball == 90:
        return "Sizning to'plagan ballingiz A"
    elif ball > 80 or ball == 80:
        return "Sizning to'plagan ballingiz B"
    elif ball > 70 or ball == 70:
        return "Sizning to'plagan ballingiz C"
    elif ball > 60 or ball == 60:
        return "sizning to'plagan ballingiz D"
    else:
        return "Siz imthiondan o'ta olmadingiz F"
    
natija = baxo_Ber(natijani)
print(natija)







a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
operator = input("Amalni kiriting (+ , - , * , /): ")

def Canculyator(a , b , operator):
    if operator == '+':
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else :
        return "Noto'g'ri amal kiritildi"

natija = Canculyator(a , b , operator)
print("Natija: " , natija)





username = input("Iltimos username kiriting: ")
password = input("Iltimos parol kiriting: ")

def Login(username , password):
    if username == "codeby.umar@gmail.com" and password == "12345":
        return f"Xush kelibsiz {username} and {password}"
    else:
        return "Login yoki parol xato"
    
natija = Login(username , password)
print(natija)




