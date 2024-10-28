
file = open('words.txt', 's')
lines = list (file)
file_contents = file.read()
print(lines)
file.close()
words_all = 0

for line in lines:
    words_all = words_all + len(line.split())
    print('Total number of words: ',words_all)

full_stops = 0
for stop in lines:
    full_stops = full_stops +len(stop.split(' . '))
    print('Total number of stops:  ',full_stops)