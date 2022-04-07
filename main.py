def HistogramToString(histogram):
    text = ''
    for key in histogram.keys():
        text = text + key + ' -> ' + str(histogram[key]) + '\n'
    return text


histogram = {}  # histogram dictionary
directory = input("Input file directory: ")  # asking user to input file directory
try:
    file = open(directory, 'rt')  # opening file
    content = file.read().upper()  # reading file and changing all letters to upper
    for ch in content:  # iterating through file content
        if ch.isalpha():  # checking is character a letter
            if ch in histogram.keys():  # checking is character within keys
                histogram[ch] += 1  # rising counter value
            else:
                histogram[ch] = 1  # creating new key and setting counter value on 1
    file.close()  # closing file
    # sorting histogram the highest amount of characters to lowest
    histogram = dict(sorted(histogram.items(), key=lambda i: i[1], reverse=True))
    file = open(directory + '.hist', 'wt')
    file.write(HistogramToString(histogram))
    file.close()
except Exception as e:
    print(e)

print(HistogramToString(histogram))  # printing histogram
