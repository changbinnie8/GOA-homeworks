password = "SecretWord"    #ამ ხაზზე ვქმნით ცვლადს
guess = input()    #აქ მომხმარებელს უნდა შემოვატანონით ინფორაცია რომელსაც ვიინახავთ ცვლადში
while guess != password: #ვქმნით while loop-ს
    guess = input()    #ისევ შემოგვაქვს მომხმარებლისგან ინფორმაცია
print("Access Granted")    #ამ ხაზზე ტერმინალში გამოგვაქვს წინადადება Access Granted