# Task: Create a function that reverses the words in a given sentence

def reverse_words(sentence):
    words = sentence.split()
    # Reverse the words in the sentence
    reversed_sentence = ' '.join(reversed(words))
    # Return the reversed sentence
    return reversed_sentence

# Example usage:
original_sentence = "This is a sample sentence."
result = reverse_words(original_sentence)
print(f"Original Sentence: {original_sentence}")
print(f"Reversed Sentence: {result}")

