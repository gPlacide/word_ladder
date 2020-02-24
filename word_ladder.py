#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file
    '''
    data_1 = open(dictionary_file)
    data = data_1.read().split("\n")
    #with open (dictionary_file) as f:
     #   data = f.readlines()
    #print("data" ,data)
    words_s = []
    words_s.append('start_word')
    words_d = deque()
    words_d.appendleft(words_s)

    while not len(words_d)==0:
        word_a = words_d.pop()
        word = word_a[len(word_a)-1]
        for i in range(len(data)):
            dictionary_w = data[i]
            #print(dictionary_w)
           # print(_adjacent(word, dictionary_w))
            #print(_adjacent(word,dictionary_w))
            #print(:'+dictionary_w)
            #if('abler'==dictionary_w):
               # print("aaaaaaaaaaaaaaaaaaaaa")
            if _adjacent(word, dictionary_w):
                if dictionary_w == (end_word):
                    word_a.append(dictionary_w)
                    return word_a

                stack_n = copy.deepcopy(word_a)
                stack_n.append(dictionary_w)
                words_d.appendleft(stack_n)
                data.remove(dictionary_w)




def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    score = 0
    len_1 = len(word1)
    len_2 = len(word2)
    length = min(len_1, len_2)


    for i in range(length):
        if (word1[i] != word2[i]):

            score += 1

    if len_1 == len_2 and score <= 1:
        return True
    elif len_1 == (len_2 - 1) and score == 0:
        return True
    elif (len_1 - 1) == len_2 and score == 0:
        return True
    else:
        return False
