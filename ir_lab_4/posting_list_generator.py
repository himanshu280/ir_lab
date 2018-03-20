import os
import re
import porter
import math
import pprint

pp = pprint.PrettyPrinter( indent = 4 )

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
    doc_term_vector[doc_id] = [0]*len(unique_words)
    doc_length[doc_id] = 0

# building doc_vector dictionary and doc length
for root, dirs, files in os.walk("./stemmed_data"):
    for file in files:
        f = open("./stemmed_data/" + file, "r")
        for line in f.readlines():
            words = line.split()
            doc_length[file] += len(words)
            for word in words:
                doc_term_vector[ file ][ term_index[ word ] ] += 1

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
                document_frequency[ word ] += 1
    
# print( document_frequency ) 
# print( doc_length )

for key in doc_term_vector:
    vector = doc_term_vector[key]
    d_length = doc_length[key]
    
    for term in unique_words:
        vector[ term_index[term] ] =  vector[ term_index[term]] * document_frequency[ term ] / d_length
    doc_term_vector[ key ] = vector
    
# printing data
for key in doc_term_vector:
    print('\n')
    print(key + " : ")
    print( doc_term_vector[key] )
    print('\n')
# pp.pprint( doc_term_vector )


# def resolve(w_1=None, w_2=None, operator=None, list_1=None, list_2=None):
#     result = []
#     # set of functions for finding and
#     if(operator == "^" and list_1 == None and list_2 == None and w_1 != None and w_2 != None):
#         for i in posting_list[w_1]:
#             for j in posting_list[w_2]:
#                 if(i == j):
#                     result.append(i)
#         return result
#     if(operator == "^" and list_1 != None and list_2 == None and w_1 != None and w_2 == None):
#         for i in posting_list[w_1]:
#             for j in list_1:
#                 if(i == j):
#                     result.append(i)
#         return result
#     if(operator == "^" and list_1 != None and list_2 != None and w_1 == None and w_2 == None):
#         for i in list_1:
#             for j in list_2:
#                 if(i == j):
#                     result.append(i)
#         return result

#     # set of functions for finding or
#     if(operator == "+" and list_1 == None and list_2 == None and w_1 != None and w_2 != None):
#         for i in posting_list[w_1]:
#             result.append(i)
#         for j in posting_list[w_2]:
#             result.append(j)
#         return result
#     if(operator == "+" and list_1 != None and list_2 == None and w_1 != None and w_2 == None):
#         for i in posting_list[w_1]:
#             result.append(i)
#         for j in list_1:
#             result.append(j)
#         return result
#     if(operator == "+" and list_1 != None and list_2 != None and w_1 == None and w_2 == None):
#         for i in list_1:
#             result.append(i)
#         for j in list_2:
#             result.append(j)
#         return result

#     # set of functions for finding not
#     if(operator == "!" and w_1 != None and list_1 == None and list_2 == None and w_2 == None):
#         for i in documents:
#             flag = 0
#             for j in posting_list[w_1]:
#                 if(i == j):
#                     flag = 1
#             if(flag == 0):
#                 result.append(i)
#         return result

#     if(operator == "!" and w_1 == None and list_1 != None and list_2 == None and w_2 == None):
#         for i in documents:
#             flag = 0
#             for j in list_1:
#                 if(i == j):
#                     flag = 1
#             if(flag == 0):
#                 result.append(i)
#         return result
