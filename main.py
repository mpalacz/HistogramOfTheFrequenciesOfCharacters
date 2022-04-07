def HistogramToString(histogram):
    text = '' # output text
    for key in histogram.keys(): # iterating through histogram
        text = text + key + ' -> ' + str(histogram[key]) + '\n' # adding text to output
    return text # returning output


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
    file = open(directory + '.hist', 'wt') # opening new file
    file.write(HistogramToString(histogram)) # writing histogram into the file
    file.close() # closing file
except Exception as e:
    print(e)

print(HistogramToString(histogram))  # printing histogram
