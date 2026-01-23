import sys


def main():
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        try:
            letter, count = line.rsplit('\t', 1)
        except ValueError:
            continue
        
        print(f"all\t{letter}\t{count}")


if __name__ == "__main__":
    main()