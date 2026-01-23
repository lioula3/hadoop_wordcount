import sys

current_letter = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        letter, c = line.rsplit('\t', 1)
    except ValueError:
        continue
    
    if letter != current_letter:
        if current_letter is not None:
            print(f"{current_letter}\t{count}")
        current_letter = letter
        count = 0
    
    count += int(c)

if current_letter is not None:
    print(f"{current_letter}\t{count}")