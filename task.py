temp = ""
result = ""
s1 = input("Word 1:")
s2 = input("Word 2:")
while s1:
    for x in s1:
        temp += x
        if temp not in s2:
            temp = ""
            break
        elif len(result) < len(temp):
            result = temp
    s1 = s1[1:]
input("Your result: " + result + "\nPress Enter to end")
