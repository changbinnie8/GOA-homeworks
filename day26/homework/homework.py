# 1)მომხარებელს შემოატანინეთ რიცხვი, შემდეგ შეამოწმეთ მეტია ის თუარა 18 ზე, თუ მეტია დაწერეთ რომ სრულწლოვანია, თუ მომხარებელმა 15 შემოიტანა რიცხვად დაწერეთ რომ თინეიჯერია, სხვა შემთხვევაში დაწერეთ რომ ბავშვია
age = int(input("enter your age: "))
if age > 18:
    print("adult")
elif age >= 15:
    print("Teenager")
else:
    print("Child")

# 2)მომხარებელს შემოატანინეთ სახელი, თუ იგი უდრის "ალექსანდრე" ს დაპრინ6ტეთ "შენ ხარ მენტორი", თუ იგი უდრის "გურამი" ს დაპრინტეთ "შენ არ ხარ მენტორი", სხვა შემთხვევაში დაპრინტეთ "შენ ხარ მოსწავლე"

name = input("Enter your name")
if name == "aleqsandre":
    print("You are a mentor")
elif name == "gurami":
    print("You are not a mentor")
else:
    print("You are a student")

# 3)მომხარებელს შემოატანინეთ 2 რიცხვი, თუ მეორე რიცხვი მეტია პრიველზე დაპრინტეთ "Level up", და პირველი მეტია მეორეზე დაპრინტეთ "Level down", სხვა შემთხვევაში დაპრინტეთ "Level updown"

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))

if num1 < num2:
    print("Level up")
elif num1 > num2:
    print("Level down")
else:
    print("Level updown")

# 4)კომენტარების სახით ახსენით if elif else და რა განსხვავებაა მათ შორის

# if - არის პირველხარისხოვანი, elif - კოდში დამატებული პირობები და else - ყველა სხვა შემთხვევა