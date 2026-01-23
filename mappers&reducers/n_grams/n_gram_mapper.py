import sys
import re


def clean_word(word):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()


def main(separator='\t'):
    for line in sys.stdin:
        words = [clean_word(w) for w in line.split() if clean_word(w)]
        for n in range(2, 6):
            for i in range(len(words) - n + 1):
                ngram = ' '.join(words[i:i+n])
                # we join the ngram words together
                print(ngram, separator, 1)

if __name__ == "__main__":
    main()