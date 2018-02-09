import os
import porter

# initializing punctuation marks list and stop words list
PUNCTUATION_MARKS = [',', '.', '<', '>', '|', ':', '(', ')', '/', '_', '\\', '?', '-', '!', '#', '%', '^', '&', '*', '_', '+', '~']
STOP_WORDS = open('STOP_WORDSs.txt', "r").read().split('\n')

# cleaning data by removing punctuation marks
for root, dirs, files in os.walk("./comp.os.ms-windows.misc"):
    for input_file in files:
        output_file = 'cleaned_data/' + input_file
        input_file = 'comp.os.ms-windows.misc/' + input_file
        f = open(input_file, "r")
        f_new = open(output_file, "w")
        for characters in f.read():
            if characters not in PUNCTUATION_MARKS:
                f_new.write(characters)
        f.close()
        f_new.close()

# stemming and removal of stop words
DOCUMENTS = []
UNIQUE_WORDS = set()
for root, dirs, files in os.walk("./cleaned_data"):
    for input_file in files:
        output_file = input_file
        input_file = 'cleaned_data/' + input_file
        DOCUMENTS.append(output_file)
        f = open(input_file, "r")
        f_new = open("stemmed_data/" + output_file, "w")
        for line in f.readlines():
            words = line.split()
            for word in words:
                word = word.lower()
                if word.isalpha() == False:
                    continue
                if word not in STOP_WORDS:
                    f_new.write(porter.stem(word) + " ")
                    UNIQUE_WORDS.add(porter.stem(word))
            f_new.write("\n")
        f.close()
        f_new.close()

# creating index list with document frequency and term frequency
DOCUMENT_FREQUENCY = dict()
TERM_FREQUENCY = dict()

# initializing TERM_FREQUENCY matrix
for term in UNIQUE_WORDS:
    TERM_FREQUENCY[term] = dict()
    for root, dirs, files in os.walk("./stemmed_data"):
        for input_file in files:
            TERM_FREQUENCY[term][input_file] = 0

# building TERM_FREQUENCY matrix
for root, dirs, files in os.walk("./stemmed_data"):
    for input_file in files:
        f_new = open("stemmed_data/" + input_file, "r")
        for line in f_new.readlines():
            words = line.split()
            for word in words:
                word = word.lower()
                if word.isalpha() == False:
                    continue
                if word not in STOP_WORDS:
                    word = porter.stem(word)
                    if word in UNIQUE_WORDS:
                        TERM_FREQUENCY[word][input_file] += 1
        f_new.close()

POSTING_LIST = dict()
# building document frequency
for word in UNIQUE_WORDS:
    DOCUMENT_FREQUENCY[word] = 0
    POSTING_LIST[word] = []
    for input_file in TERM_FREQUENCY[word].keys():
        if TERM_FREQUENCY[word][input_file] > 0:
            POSTING_LIST[word].append(input_file)
            DOCUMENT_FREQUENCY[word] += 1

# example
print 'Document frequency of term "Made":'
print DOCUMENT_FREQUENCY['made']
print 'Term frequency of term "Made":'
print TERM_FREQUENCY['made']
print 'Posting List of term "Made":'
print POSTING_LIST['made']
