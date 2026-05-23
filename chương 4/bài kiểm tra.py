data = "Nguyen Van Duy Sinh ngay 21 nam sinh 2005 "

so = ""
chu = ""

for c in data:
    if c.isdigit():
        so += c
    elif c.isalpha():
        chu += c

print("out so: ", so)   
print("out chu: ", chu)