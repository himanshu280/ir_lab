import os
import re
import porter
import math
import operator
import pprint
from collections import OrderedDict
from operator import itemgetter

pp = pprint.PrettyPrinter(indent=4)

z = 0
# initializing punctuation marks list and stop words list
punctuation_marks = [',', '.', '<', '>', '|', ':',
                     '(', ')', '/', '_', '\\', '?', '-', '!', '#', '%', '^', '&', '*', '_', '+', '~']
stop_word = open('stop_words.txt', "r").read().split('\n')

# ------------------------------------------------------------------------------------------------------------------------------------

f = []
for (dirpath, dirnames, filenames) in os.walk("./stemmed_data"):
    f.extend(filenames)
    break

if len(f) == 0:
    # cleaning data by removing punctuation marks
    for root, dirs, files in os.walk("./comp.os.ms-windows.misc"):
        for input_file in files:
            output_file = 'cleaned_data/' + input_file
            input_file = 'comp.os.ms-windows.misc/' + input_file
            f = open(input_file, "r")
            f_new = open(output_file, "w")
            for characters in f.read():
                if characters not in punctuation_marks:
                    f_new.write(characters)
            f.close()
            f_new.close()

    # stemming and removal of stop words
    documents = []
    unique_words = set()
    for root, dirs, files in os.walk("./cleaned_data"):
        for input_file in files:
            output_file = input_file
            input_file = 'cleaned_data/' + input_file
            # documents.append(output_file)
            f = open(input_file, "r")
            f_new = open("stemmed_data/" + output_file, "w")
            for line in f.readlines():
                words = line.split()
                for word in words:
                    word = word.lower()
                    if word.isalpha() == False:
                        continue
                    if word not in stop_word:
                        f_new.write(porter.stem(word) + " ")
                        # unique_words.add(porter.stem(word))
                f_new.write("\n")
            f.close()
            f_new.close()

# creating index list with document frequency and term frequency
documents = []
unique_words = set()

for root, dirs, files in os.walk("./stemmed_data"):
    for file in files:
        documents.append(file)
        f = open("./stemmed_data/" + file, "r")
        for line in f.readlines():
            words = line.split()
            # print(words)
            for word in words:
                unique_words.add(word)

# initialze index vs term dictonary
term_index = dict()

index = 0
for term in unique_words:
    term_index[term] = index
    index += 1

# print( term_index )

# initialize doc_vector dictornary and doc length
doc_term_vector = dict()
doc_length = dict()

for doc_id in documents:
    doc_term_vector[doc_id] = [0] * len(unique_words)
    doc_length[doc_id] = 0

# building doc_vector dictionary and doc length
for root, dirs, files in os.walk("./stemmed_data"):
    for file in files:
        f = open("./stemmed_data/" + file, "r")
        for line in f.readlines():
            words = line.split()
            doc_length[file] += len(words)
            for word in words:
                doc_term_vector[file][term_index[word]] += 1

# building document_frequency
document_frequency = dict()

for term in unique_words:
    document_frequency[term] = 0

for root, dirs, files in os.walk("./stemmed_data"):
    for file in files:
        f = open("./stemmed_data/" + file, "r")
        for line in f.readlines():
            words = line.split()
            for word in words:
                document_frequency[word] += 1

for key in doc_term_vector:
    vector = doc_term_vector[key]
    d_length = doc_length[key]

    for term in unique_words:
        vector[term_index[term]] = vector[term_index[term]] * \
            document_frequency[term] / d_length
    doc_term_vector[key] = vector

# k means using terms vectors as feature vectors


def eu_dist(p_A, p_B):
    # p_A is point A which is a vector
    print "noting"


def find_centroid(l_p):
    num_points = len(l_p)
    sum_vec = []
    for doc_id in l_p:
        print doc_term_vector[doc_id]

    return []


def find_label(doc_vec, centroid_list):
    # doc_vec is a point,
    # centroid list is the list of all vectors of all centroids
    # use eu_dist from above
    # return the index of the centroid it is closet to
    print "nothing"


def check_condition(bins_1, bins_2):
    # check if both are equal
    # return boolean
    print "nothing"


# parameter initilization
num_data_points = len(list(doc_term_vector.keys()))
k = 20
iters = 10
set_of_docs = list(doc_term_vector.keys())

# data structures to be used
bins_1 = []

for i in range(k):
    bins_1.append([])

bins_2 = []

for i in range(k):
    bins_2.append([])

# randomly initilize bins
for i in range(num_data_points):
    bins_1[i % k].append(set_of_docs[i])

# find centroids of bins for each iteration
for iter_count in range(iters):
    centroids = []

    # find all centroids of bins
    for num_bin in bins_1:
        centroids.append(find_centroid(num_bin))
        break

    # # lable each data point using min_dist(cluster_set,single_point)
    # for doc_id in set_of_docs:
    #     doc_label = find_label(doc_term_vector[doc_id], centroids)
    #     bins_2[doc_label].append(doc_id)

    # # termination condition
    # should_terminate = check_condition(bins_1, bins_2)

    # if should_terminate:
    #     break
    # else:
    #     continue
