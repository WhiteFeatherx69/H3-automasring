with open('readme.txt', 'w') as f:
    f.write('Python is powerful, but sometimes tricky')

def countA(text):
    count = 0
    for c in text:
        if c == 't':
            count = count + 1
    return count

print(countA("Python is powerful, but sometimes tricky"))

def reversed_string(a_string):
    return a_string[::-1]
print(reversed_string("Python is powerful, but sometimes tricky"))


tekst = "Python is powerful, but sometimes tricky."


ny_tekst = tekst.replace("Python", "PYTHON")


print(ny_tekst)