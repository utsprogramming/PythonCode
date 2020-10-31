lines = int(input('how tall is ur pyramid'))

n = '0'
s = ' '

a = 1
l = lines - 1

for i in range(lines):
    print(f'{l * s}{n * a}')
    a = a + 2
    l = l - 1

