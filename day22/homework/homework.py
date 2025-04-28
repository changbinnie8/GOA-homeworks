n=int(input("enter a number: "))
for i in range(n+1):
    print(i)

sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)

for i in range(0, n+1, 3):
    print(i)

sum2 = 1
for i in range(0, n+1, 4):
    sum2 = sum2 * i

#while loop-ი ცოტა ვერ გავიგე და ხვალ ლიდერი ამიხსნის