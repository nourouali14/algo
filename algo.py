def count_sentence(sentence):
    length = 0
    words = 1  
    vowels = 0
    for char in sentence:
        if char != ' ' and char != '.':
            length += 1
            if char.lower() in 'aeiou':
                vowels += 1
        elif char == ' ':
            words += 1
    print("Length of the sentence:", length)
    print("Number of words:", words)
    print("Number of vowels:", vowels)


count_sentence("This is a sample sentence.")
