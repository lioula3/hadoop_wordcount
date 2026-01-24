import sys
from collections import defaultdict


def main(separator='\t'):

    
    word_sentences = defaultdict(list)
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        try:
            word, sentence = line.rsplit(separator, 1)
            # We add sentence to this word if it is not already present
            if sentence not in word_sentences[word]:
                word_sentences[word].append(sentence)
        except ValueError:
            continue
    
    for word in sorted(word_sentences.keys()):
        sentences = word_sentences[word]
        sentences_str = '|'.join(sentences) # we separate sentences by '|'
        
        print(f"{word}{separator}{sentences_str}")


if __name__ == "__main__":
    main()