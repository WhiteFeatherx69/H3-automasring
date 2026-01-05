import curses.ascii

str1 = "P@#yn26at^&i5ve"

def devide(bogstaver):
    alfa = curses.ascii.isalpha(bogstaver)
    tal = curses.ascii.isdigit(bogstaver)

    print(alfa)
    print(tal)

print(devide(str1))