from operator import itemgetter
import sys


def read_mapper_output(file, separator='\t'):
    for line in file:
        parts = line.rstrip().split(separator)
        if len(parts) == 3:
            yield (parts[1], int(parts[2]))  


def main(separator='\t'):
    
    letters_list = []
    for letter, count in read_mapper_output(sys.stdin, separator=separator):
        letters_list.append((letter, count))
    
    if not letters_list:
        return
    
    # We have to sort the keys from the highest count to the lowest
    letters_list.sort(key=itemgetter(1), reverse=True)
    
    # We take the top 2%
    total_letters = len(letters_list)
    top_2_percent = max(1, int(total_letters * 0.02))
    
    # We want to take the ones having the same frequency
    min_threshold = letters_list[top_2_percent - 1][1]
    
    for letter, count in letters_list:
        if count >= min_threshold:
            print(f"{letter}{separator}{count}")


if __name__ == "__main__":
    main()