f = open("output.txt", "rb")

txt = f.read()
txt_input = open("input.txt", "r").read()

d = {}

for x in txt_input:
    if x not in d:
        d[x] = True

print(d.keys())


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c

    return a


def lca(*numbers):
    print(numbers)
    ans = 1
    for number in numbers:
        ans = ans * number // gcd(ans, number)

    return ans


sizes = []

for i in range(1, 32):
    sizes.append(i)

sizeLCA = lca(*sizes)

n = len(txt)

formatInput = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 º¶€,©â”Ã:*'_;`/\"-.?!{}[]()\n"
formatParola = "©â”Ã º¶€~|@<>#$%^&,:*'_;`/\"-.?!{}[]()\+=\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
ans = []

for x in d.keys():
    if x not in formatInput:
        print(x)

for sizeKey in sizes:
    print(f"for the length of the key being: {sizeKey}")
    yesAnswersTotal = []
    for i in range(sizeKey):
        yesAnswers = []

        for x in formatInput:
            semafor = True

            for j in range(i, n, sizeKey):
                ceva = chr(txt[j] ^ ord(x))

                if ceva not in formatInput:
                    semafor = False
                    break

            if semafor:
                yesAnswers.append(x)

        if len(yesAnswers):
            yesAnswersTotal.append(yesAnswers)

    print(yesAnswersTotal)
    if len(yesAnswersTotal) == sizeKey:
        ans = ''.join([str(x[0]) for x in yesAnswersTotal])
        break

print(ans)

"""for i in range(0, 15):
    ans.append(chr(ord(txt_input[i]) ^ txt[i]))

ans = ''.join([str(x) for x in ans])
print(ans)
"""
