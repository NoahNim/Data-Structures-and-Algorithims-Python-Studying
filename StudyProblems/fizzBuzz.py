def fizzBuzz(self, n: int):
    fbList = []
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            fbList.append("FizzBuzz")
        if i % 3 == 0 and i % 5 != 0:
            fbList.append("Fizz")
        if i % 5 == 0 and i % 3 != 0:
            fbList.append("Buzz")
        elif i % 3 != 0 and i % 5 != 0:
            stringedNum = str(i)
            fbList.append(stringedNum)
        i += 1
    return fbList
