# Large sum

with open('13.txt', 'r') as file:
    content = file.read()

print(str(sum(list(map(int, content.split('\n')))))[:10])
