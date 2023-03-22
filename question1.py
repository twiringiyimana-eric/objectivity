def word_frequency(text):
    # Split the text into words
    words = text.lower().split()

    # Count the frequency of each word
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    # Sort the words by frequency in descending order
    sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Print the results
    for word, count in sorted_words:
        print(word, count)
text = "The quick brown fox jumped over the lazy dog. The dog slept all day."
word_frequency(text)
