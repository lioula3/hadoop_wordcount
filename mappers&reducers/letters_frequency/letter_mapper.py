import sys
import re


def clean_word(word):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()


def read_input(file):
    for line in file:
        yield line.split()


def filter_words_by_length(words, min_length=4, max_length=10):

    return [w for w in words if min_length < len(w) < max_length]


def main(separator='\t'):
    
    data = read_input(sys.stdin)
    for words in data:
        filtered = filter_words_by_length(words)
        for word in filtered:
            cleaned = clean_word(word)
            if cleaned:  
                for letter in cleaned:
                    print(letter, separator, 1)


if __name__ == "__main__":
    main()