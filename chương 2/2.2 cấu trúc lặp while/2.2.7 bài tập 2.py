n = int(input("nhập số n: "))
i = 2
print("các ước số nguyên tố của n là:")

while i <= n:
    if n % i == 0:
        j = 2
        nguyento = True
        while j < i:
            if i % j == 0:
                nguyento = False
                break
            j = j + 1
        
        if nguyento:
            print(i)
    i = i + 1