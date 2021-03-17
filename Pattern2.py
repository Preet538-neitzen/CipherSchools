rows = 6
char = 97

for i in range(rows):
    for j in range(i):
        print(chr(char), end=' ')
        char += 1
    print('')