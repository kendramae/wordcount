# put your code here.
def make_word_list(filepath):
    """Takes a .txt filepath and returns a list of the words therein.
    """
    text_log = open(filepath)
    word_list = []
    for line in text_log:
        line = line.strip()
        words = line.replace("--", " ").split(" ")
        for word in words:
            word = word.lower()
            word = word.strip(',?."!-:;_\'*)($')
            word_list.append(word)
    text_log.close()
    return word_list



def count_list(word_list):
    """Calls make_word_list and tallies words in that list, returning each unique
    word with how many times it occurs.
    """
    word_tally = {}
    for word in word_list:

        # check if word is in dictionary (already seen it); if so, bump up by 1
        # otherwise, add to dictionary as the first we've seen it

        if word in word_tally:
            word_tally[word] +=1
        else:
            # First time we've seen this word
            word_tally[word] = 1

        # Alternate way to think about this:
        # word_tally[word] = word_tally.get(word, 0) + 1

    # for key_and_value in word_tally.items():
    #     word = key_and_value[0]
    #     used = key_and_value[1]

    for word, used in word_tally.items():
        print "{}: {}".format(word, used)


word_list = ['apple', 'berry', 'cherry', 'berry', 'apple']
count_list(word_list)

# combine the two: get a list of word,s then count them
word_list = make_word_list("myfile.txt")
count_list(word_list)





# def count_list(filepath):
#     """Calls make_word_list and tallies words in that list, returning each unique
#     word with how many times it occurs.
#     """
#     word_list = make_word_list(filepath)
#     word_tally = {}
#     for word in word_list:

#         # check if word is in dictionary (already seen it); if so, bump up by 1
#         # otherwise, add to dictionary as the first we've seen it

#         if word in word_tally:
#             word_tally[word] +=1
#         else:
#             # First time we've seen this word
#             word_tally[word] = 1

#         # Alternate way to think about this:
#         # word_tally[word] = word_tally.get(word, 0) + 1

#     # for key_and_value in word_tally.items():
#     #     word = key_and_value[0]
#     #     used = key_and_value[1]

#     for word, used in word_tally.items():
#         print "{}: {}".format(word, used)






#first function 
# def word_counter(filepath):
#     """Takes a .txt filepath and returns a count of the words and how many
#     times they appear.
#     """

#     test_log = open(filepath)
#     word_tally = {}
#     for line in test_log:
#         line = line.strip()
#         words = line.split(" ")
#         for word in words:
#             word = word.lower()
#             ## words_doubled = word.split("--")
#             ## print "WORDS DOUBLED:", words_doubled
#             ## if len(words_doubled) > 1:
#                 ## word = words_doubled[0]
#                 ## words.append(words_doubled[1])
#             word = word.strip("'")
#             word = word.strip(',?."!-:;_*)($')
#             word = word.strip("'")
#             if word in word_tally:
#                 word_tally[word] += 1
#             else:
#                 word_tally[word] = 1
#     test_log.close()
#     for word, used in word_tally.iteritems():
#         print "{}: {}".format(word, used)
