# Mở file chứa dữ liệu đầu vào và file ghi kết quả đầu ra
fi = open("input.txt", "r")
fo = open("output.txt", "w")

for line in fi:
    if not line.strip():  
        continue
        
    n = int(line)
    fo.write(str(n) + " = ") 
    
    k = 2
    first = True 
    
    while n > 1:
        while n % k != 0:
            k = k + 1
            
        if first:
            fo.write(str(k))
            first = False
        else:
            fo.write(" * " + str(k))
            
        while n % k == 0:
            n = n // k

    fo.write("\n") 

fi.close()
fo.close()