f = open('python-basics/text.txt')
print(f.read())

l = [str(i)+str(i-1) for i in range(10)]

f = open('python-basics/text.txt', 'a')
for index in l:
    f.write(index + '\n')

f.close()

f = open('python-basics/text.txt', 'r')
l = [line.strip() for line in f]
print(l)
f.close()