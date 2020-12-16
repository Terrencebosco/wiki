# TODO oop?

import pandas as pd
import numpy as np
import wikipedia
import re

data = []

def get_count_base(word):
    '''
    Returns contents from Wikipedia based on the base user input. based on the
    Wikipedia's sorting system some gene's are not searchable based on acronym
    of gene name.

    word = none zero sum of strings.
    '''

    word_strip = word.strip()
    test = wikipedia.page(word_strip)
    summary = wikipedia.summary(word_sort)
    count = len(test.content.split(' '))
    data.append([word,count,summary])
    # return data

def get_count_abc(word):
    '''
    Returns contents from Wikipedia based on the base users acronym input. based on the
    Wikipedia's sorting system some gene's are not searchable based on acronym
    of gene name.

    word = none zero sum of strings.
    '''
    word_strip = word.strip()
    word_cleaned = re.sub(r'[^a-zA-Z 0-9]', '', word_strip)
    word_gene = word_cleaned+'gene'
    test = wikipedia.page(word_gene)
    summary = wikipedia.summary(word_gene)
    count = len(test.content.split(' '))
    data.append([word,count,summary])
    # return test.content.split(' ')


def get_count_word(word):
    '''
    Returns contents from Wikipedia based on the raw text of user input. based on the
    Wikipedia's sorting system some gene's are not searchable based on acronym
    of gene name.

    word = none zero sum of strings.
    '''
    word_strip = word.strip()
    word_cleaned = re.sub(r'[^a-zA-Z 0-9]', '', word_strip)
    test = wikipedia.page(word_cleaned)
    summary = wikipedia.summary(word_cleaned)
    count = len(test.content.split(' '))
    data.append([word,count,summary])
    # return test.content.split(' ')

def get_count(listgene):
    if len(data)>0:
        data.clear()
    for i in listgene[0]:
        try:
            get_count_abc(i)
        except:
            try:
                get_count_base(i)
            except:
                try:
                    get_count_word(i)
                except:
                    data.append((f'{i} is bad input'))
    return data