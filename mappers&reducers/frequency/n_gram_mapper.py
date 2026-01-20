import sys
import re


def clean_word(word):
    """
	Remove punctuation and convert the word to lowercase
	"""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()


def main(separator='\t'):
    """
    Count the frequencies of composition from 2 to 5
    """
    for line in sys.stdin:
        words = [clean_word(w) for w in line.strip().split() if clean_word(w)]
        for n in range(2, 6):
            for i in range(len(words) - n + 1):
                ngram = ' '.join(words[i:i+n])
                # we join the ngram words together
                print(ngram, separator, 1)

if __name__ == "__main__":
    main()