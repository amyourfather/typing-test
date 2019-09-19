""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
def lines_from_file(path):
    file = open(path, "r")
    list = readlines(file)
    for i in range(len(list)):
        list[i] = strip(list[i], "\n")
        list[i] = strip(list[i])
    return list

def new_sample(path, i):
    doc = lines_from_file(path)
    return doc[i]

def analyze(sample_paragraph, typed_string, start_time, end_time):
    def speed():
        num_of_chars = len(typed_string)
        num_of_chars = num_of_chars / 5
        time = (end_time - start_time) / 60
        speed = num_of_chars / time

        return speed
    def accuracy():
        cpy_typed = typed_string
        cpy_sample = sample_paragraph
        cpy_typed = split(cpy_typed)
        cpy_sample = split(cpy_sample)
        correct = 0
        effective_length = min(len(cpy_typed), len(cpy_sample))
        for i in range(effective_length):
            if cpy_sample[i] == cpy_typed[i]:
                correct += 1
        if effective_length == 0:
            return 0.0
        else:
            return correct / effective_length * 100
    return [speed(), accuracy()]

    return 0

def pig_latin(word):
    cpy_w = word
    vowel = ['a', 'e', 'i', 'o', 'u']
    if not(cpy_w[0] in vowel):
        cut = 0
        for i in range(len(cpy_w)):
            cut = i
            if cpy_w[i] in vowel:
                break
            else:
                if i == len(cpy_w) - 1:
                    cut = i + 1
        if cut == len(cpy_w):
            #print(cut)
            cpy_w = cpy_w + "ay"
        else:
            #print(cut)
            part_one = cpy_w[:cut]
            part_two = cpy_w[cut:]
            #print(part_one)
            #print(part_two)
            cpy_w = part_two + part_one + "ay"
    else:
        cpy_w = cpy_w + "way"


    return cpy_w

def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    return min(words_list, key = lambda x: score_function(user_input, x))

def swap_score(string1, string2):
    if string1 == "" or string2 == "":
        return 0
    else:
        if string1[0] == string2[0]:
            return swap_score(string1[1:], string2[1:])
        else:
            return 1 + swap_score(string1[1:], string2[1:])

"*** YOUR CODE HERE ***"

# END Q1-5

# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if word1 == '' or word2 == '': # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return max(len(word1), len(word2))
        # END Q6
    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return score_function(word1[1:], word2[1:])
        # END Q6
    else:
        add_char = 1 + score_function(word1, word2[1:])  # Fill in these lines
        remove_char = 1 + score_function(word1[1:], word2)
        substitute_char = 1 + score_function(word1[1:], word2[1:])

        return min([add_char, remove_char, substitute_char])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6


KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
cache = {}
def memo(f):
    def memoized(word1, word2):
        if (word1, word2) in cache:
            return cache[(word1, word2)]
        elif (word2, word1) in cache:
            return cache[(word2, word1)]
        else:
            cache[(word1, word2)] = f(word1, word2)
            return cache[(word1, word2)]
    return memoized

def score_function_accurate(word1, word2):
    if word1 == '' or word2 == '': # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return max(len(word1), len(word2))
        # END Q6
    elif word1[0] == word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        return memo(score_function_accurate)(word1[1:], word2[1:])
        # END Q6
    else:
        add_char = 1 + memo(score_function_accurate)(word1, word2[1:])  # Fill in these lines
        remove_char = 1 + memo(score_function_accurate)(word1[1:], word2)
        substitute_char = KEY_DISTANCES[word1[0], word2[0]] + memo(score_function_accurate)(word1[1:], word2[1:])

        return min([add_char, remove_char, substitute_char])
# END Q7-8

def score_function_final(w1, w2):
    return memo(score_function_accurate)(w1, w2)
