import sys


def main(separator='\t'):
    
    current_pair = None
    count = 0
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        try:
            word, following_word, c = line.rsplit(separator, 2)
        except ValueError:
            continue
        
        pair = (word, following_word)
        
        if pair != current_pair:
            if current_pair is not None:
                print(f"{current_pair[0]}{separator}{current_pair[1]}{separator}{count}")
            
            current_pair = pair
            count = 0
        
        count += int(c)
    
    if current_pair is not None:
        print(f"{current_pair[0]}{separator}{current_pair[1]}{separator}{count}")


if __name__ == "__main__":
    main()