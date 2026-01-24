import sys
import re


def clean_word(word):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()


def read_input(file):
    for line in file:
        yield line.split()


def split_sentences(text):
    # Split by sentence delimiters
    sentences = re.split(r'[.!?]+', text)
    # Clean and filter empty sentences
    return [s.strip() for s in sentences if s.strip()]


def main(separator='\t'):
   
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        sentences = split_sentences(line)
        
        for sentence in sentences:
            words = sentence.split()
            cleaned_words = [clean_word(w) for w in words if clean_word(w)]
            
            for word in cleaned_words:
                print(f"{word}{separator}{sentence}")


if __name__ == "__main__":
    main()