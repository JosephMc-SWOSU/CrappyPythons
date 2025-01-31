def count_word_frequencies(words):
    """Counts the frequency of each word in the list (case insensitive)."""
    word_count = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in word_count:
            word_count[word_lower] += 1
        else:
            word_count[word_lower] = 1
    return word_count

if __name__ == "__main__":
    # Read the input list of words
    input_words = input("Enter a list of words: ").split()
    
    # Count the word frequencies
    word_frequencies = count_word_frequencies(input_words)
    
    # Use a set to keep track of printed words
    printed_words = set()
    
    # Output the words and their frequencies
    for word in input_words:
        word_lower = word.lower()
        if word_lower not in printed_words:
            print(f"{word} {word_frequencies[word_lower]}")
            printed_words.add(word_lower)