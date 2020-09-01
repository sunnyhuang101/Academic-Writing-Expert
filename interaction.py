import sys
from collections import defaultdict, Counter
import re


import geniatagger
tagger = geniatagger.GeniaTagger('./geniatagger/geniatagger')

filtered2 = defaultdict(lambda:defaultdict()) #put filtered sentences(examples)

def find_pos(tagged):
    if tagged.startswith('NN'):
        return 'N'
    elif tagged.startswith('VB'):
        return 'V'
    elif tagged.startswith('JJ'):
        return 'J'
    else:
        return tagged

if __name__ == '__main__':
	#statistical result
	#filtered2(head, pos):pat:ex
    for line in open('test.txt', 'r'):
        line = eval(line.strip())
        head, pos1, freq, pat, ex = line[0], line[1], line[2], line[3], line[4]
        for i in range(len(pat)):
            print(ex)
            filtered2[(head, pos1)][pat[i]] = ex[i]

    #user input
    print('say something: ')
    for line in sys.stdin:

        line = line.strip()
        original = []
        base = []
        tag = []
        chunk = []
        #to transform the tagged data into a more user-friendly form
        for each_word in tagger.parse(line):
            original.append(each_word[0])
            base.append(each_word[1])
            tag.append(each_word[2])
            chunk.append(each_word[3])
            print(each_word[1])
            print(each_word[2])

        pos =  find_pos(tag[-1])

        if filtered2[(base[-1], pos)].items():
            #list all pattern recommendations
            for pat, sen in filtered2[(base[-1], pos)].items():
                print(pat)

            choice = input("choose a pattern: ")
            print(filtered2[(base[-1], pos)][choice])
        else:
            print("no result")