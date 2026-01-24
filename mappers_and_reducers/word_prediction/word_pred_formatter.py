import sys
from collections import defaultdict


def main(separator='\t'):
    
    word_followers = defaultdict(lambda: defaultdict(int))
    # it is a dict of dicts to count occurrences of following words for each word
    # We use defaultdict to simplify counting, otherwise we would need to check for existence first
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        try:
            word, following_word, count = line.rsplit(separator, 2)
            word_followers[word][following_word] += int(count)
        except ValueError:
            continue
    
    # Output formatted results
    for word in sorted(word_followers.keys()):
        followers = word_followers[word]
        
        # Sort followers by frequency : the most recurrent comes first
        sorted_followers = sorted(followers.items(), key=lambda x: (-x[1], x[0]))
        
        # Format: following_word1:count1,following_word2:count2,...
        followers_str = ','.join(f"{fw}:{c}" for fw, c in sorted_followers)
        
        print(f"{word}{separator}{followers_str}")


if __name__ == "__main__":
    main()