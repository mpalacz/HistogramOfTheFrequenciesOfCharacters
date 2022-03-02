histogram = {}

try:
    file = open('input.txt', 'rt')
    content = file.read().upper()
    for ch in content:
        if ch.isalpha():
            if ch in histogram.keys():
                histogram[ch] += 1
            else:
                histogram[ch] = 1
    file.close()
except Exception as e:
    print(e)

for key in histogram.keys():
    print(key, '->', histogram[key])