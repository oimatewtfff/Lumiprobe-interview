from queue import SimpleQueue

def parChecker(parString):
    s = SimpleQueue()
    balanced = True
    index = 0
    while index < len(parString) and balanced:
        symbol = parString[index]
        if symbol == "(":
            s.put(symbol)
        else:
            if s.empty():
                balanced = False
            else:
                s.get()

        index = index + 1

    if balanced and s.empty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))
