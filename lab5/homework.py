def word_counts(input_file_name):
    word_count = {}
    with open(input_file_name, 'r') as file:
        content = file.read().strip()
        lines = content.split('\\n')
        for line in lines:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1

    return word_count


filename = "file2.txt"
print(word_counts(filename))
