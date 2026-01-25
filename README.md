# Hadoop WordCount – Text Analysis on *Notebooks of Leonardo Da Vinci*

This project implements a series of Hadoop MapReduce programs to perform advanced text analysis on the *Notebooks of Leonardo Da Vinci* (Project Gutenberg ID: 5000). The objective is to extract linguistic statistics and patterns from a large text corpus using distributed processing.


## Project Objectives

The project performs the following text analysis tasks using MapReduce:

### 1. Word Composition Frequency
Count the frequency of:
- 2-word combinations (bigrams)
- 3-word combinations (trigrams)
- 4-word combinations
- 5-word combinations


### 2. Word Length Count
Generate statistics showing the number of words per word length.

### 3. Letter Frequency Analysis
- Consider only words with length **greater than 4 and less than 10**
- Count letter frequencies
- Output the **top 2% most used letters**

### 4. Next Word Prediction
For a given word, list the most frequent words that immediately follow it in the text.

### 5. Sentence Extraction
List all sentences that contain a given input word.


## Input Data

The input text is the *Notebooks of Leonardo Da Vinci*, available from Project Gutenberg:

🔗 https://www.gutenberg.org/ebooks/5000

Download the text file and place it in:

## Requirements

- Java 8 or higher
- Apache Hadoop

## How to Run
Here is an example, if you need to run multiple jobs:

bin/hadoop jar path/to/hadoop-streaming-1.2.1.jar \
-input /user/username/job1_output \
-output /user/username/job2_output \
-mapper "python3 mapper2.py" \
-reducer "python3 reducer2.py" \
-file path/to/project/mappers/mapper2.py \
-file path/to/project/reducers/reducer2.py

## Notes
In this project, numbers were not removed during preprocessing. However, they could be excluded to retain only alphabetic words, which would improve the readability and interpretability of the results.