
lines_len = []
with open("a.txt", 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        lines_len.append(len(line))

max_line = max(lines_len)
print(max_line)