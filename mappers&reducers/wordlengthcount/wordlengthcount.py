import sys
import re


def clean_word(word):
    """
	Remove punctuation and convert it to lowercase,
	"""

    cleaned = re.sub(r'[^a-zA-Z0-9]', '', word)
    return cleaned.lower()

def read_input(file):
	for line in file:
	# split the line into words
		yield line.split()


def main(separator='\t'):
	"""
	We should count the words having the same length
	So we will give the length as a key
	"""

	data = read_input(sys.stdin)
	for words in data:
		# words is the list of words within that line
		# write the results to STDOUT (standard output);
		# what we output here will be the input for the
		# Reduce step, i.e. the input for reducer.py

		# tab-delimited; the trivial word count is 1
		for word in words:
			cleaned = clean_word(word)
			if cleaned:
				print(len(cleaned), separator, 1)


if __name__ == "__main__":
	main()