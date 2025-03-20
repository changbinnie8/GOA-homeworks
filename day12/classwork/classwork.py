#1
print(8 > 9 or 17 == 17)
print(92 < 100 and 42 == 127)

#2
#print(True and False or False or True and False) - გამოიტანს False

#3
print(False or True and False or True) #გამოიტანს True
print(False and True or True and False or True) #გამოიტანს True
print((True and False) or (False or True and True)) #გამოიტანს True
print(True and True or False and False or True) #გამოიტანს True
print((False or True) and (True or False and True)) #გამოიტანს True
print(False and True or False or False and True) #გამოიტანს False
print(True and False or False and True or False) #გამოიტანს False
print((False or False) and (True and False)) #გამოიტანს False
print(True and False and True or False) #გამოიტანს False
print((False or False) and (False or True and False)) #გამოიტანს False