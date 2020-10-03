file_name = input("Enter file:")
handle = None
try:
    handle = open(file_name)
except Exception as e:
    print("Invalid file Name")
    exit()

words_dict = {}
for line in handle:
    words = line.split()
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1
        
most_common_word = None
count = None
for word, value in words_dict.items():
    if count == None or value > count:
        count = value
        most_common_word = word

print(most_common_word, count)