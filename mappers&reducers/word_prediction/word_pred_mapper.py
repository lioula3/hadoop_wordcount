import sys
import re


def clean_word(word):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()


def read_input(file):
    for line in file:
        yield line.split()


def main(separator='\t'):
    # We need to sumbit pairs of words (current_word, following_word)    
    data = read_input(sys.stdin)
    
    for words in data:
        cleaned_words = [clean_word(w) for w in words if clean_word(w)]
        
        for i in range(len(cleaned_words) - 1):
            current_word = cleaned_words[i]
            following_word = cleaned_words[i + 1]
            print(f"{current_word}{separator}{following_word}{separator}1")


if __name__ == "__main__":
    main()