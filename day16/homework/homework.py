#debugging არის კოდში შეცდომების გასწორება
#input-ის საწყიდი data type არის სტრინგი. ამის დამამტკიცებელი მაგალითი არის:

num1 =(input("enter a number: "))
num2 =(input("enter a number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
#ეს კოდი გამოიტანს ერორს რადგან სტრინგებს შორის ვერ მოხდება მათემატიკური ოპერაცია.
#casting არის მონაცემის ტიპის შეცვლა. მაგალითად:
#str(), int(), float(), bool().