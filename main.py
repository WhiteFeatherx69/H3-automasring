str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for ch in str1:
    if ch.isalpha():
        chars += 1
    elif ch.isdigit():
        digits += 1
    else:
        symbols += 1

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)
