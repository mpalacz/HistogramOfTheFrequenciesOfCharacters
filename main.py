histogram = {} # histogram dictionary

try:
    file = open('input.txt', 'rt') # opening file
    content = file.read().upper() # reading file and changing all letters to upper
    for ch in content: # iterating through file content
        if ch.isalpha(): # checking is character a letter
            if ch in histogram.keys(): # checking is character within keys
                histogram[ch] += 1 # rising counter value
            else:
                histogram[ch] = 1 # creating new key and setting counter value on 1
    file.close() # closing file
except Exception as e:
    print(e)

for key in histogram.keys():
    print(key, '->', histogram[key]) # printing histogram
