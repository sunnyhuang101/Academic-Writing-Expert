#test POS only
'''import nltk
words = nltk.word_tokenize('As the Network Processors are used to implement increasingly complicated applications, task distribution among the cores is becoming an important problem. ')
print(words)
word_tag = nltk.pos_tag(words)
print(word_tag)

#test POS + lemma

from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


def  get_wordnet_pos (treebank_tag):
     if treebank_tag.startswith( 'J' ):
         return wordnet.ADJ
     elif treebank_tag.startswith( 'V' ):
         return wordnet.VERB
     elif treebank_tag.startswith( 'N' ):
         return wordnet.NOUN
     elif treebank_tag .startswith( 'R' ):
         return wordnet.ADV
     else :
         return  None


def  lemmatize_sentence (sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        print(pos)
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))
    return res

print(lemmatize_sentence('As the Network Processors are used to implement increasingly complicated applications, task distribution among the cores is becoming an important problem. '))
'''
#test IBO
import nltk
from nltk.corpus import conll2000

test_sents = conll2000.chunked_sents("train.txt", chunk_types=["NP"])
print(nltk.chunk.tree2conlltags(test_sents[0]))
#print(test_sents[0])



#test tree
import nltk
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.tag import StanfordNERTagger

style.use('fivethirtyeight')

# Process text  
def process_text():
    #raw_text = open("/usr/share/news_article.txt").read()
    token_text = word_tokenize('As the Network Processors are used to implement increasingly complicated applications, task distribution among the cores is becoming an important problem. ')
    return token_text
def nltk_tagger(token_text):
    tagged_words = nltk.pos_tag(token_text)
    ne_tagged = nltk.ne_chunk(tagged_words)
    return(ne_tagged)
def nltk_main():
    s = nltk_tagger(process_text())
    print(s)
    print("bio")
    print(bio_tagger(s))
    return s
def bio_tagger(ne_tagged):
    bio_tagged = []
    prev_tag = "O"
    for token, tag in ne_tagged:
        if tag == "O": #O
            bio_tagged.append((token, tag))
            prev_tag = tag
            continue
        if tag != "O" and prev_tag == "O": # Begin NE
            bio_tagged.append((token, "B-"+tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag == tag: # Inside NE
            bio_tagged.append((token, "I-"+tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag != tag: # Adjacent NE
            bio_tagged.append((token, "B-"+tag))
            prev_tag = tag
    return bio_tagged
# Stanford NER tagger    
def stanford_tagger(token_text):
    st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                            '/usr/share/stanford-ner/stanford-ner.jar',
                            encoding='utf-8')   
    ne_tagged = st.tag(token_text)
    return(ne_tagged)
def stanford_main():
    print(stanford_tagger(process_text()))

if __name__ == '__main__':
    
    #stanford_main()
    tags = nltk.chunk.tree2conlltags(nltk_main())
    print(tags)