'''
Created on 09 Ara 2012

@author: burakkerim
'''

import sys

from nltk.parse import load_parser 
cp = load_parser('file:extended.fcfg')

sentences = [
             #----------------------------------
             # POSITIVES - already covered by the grammar
             #----------------------------------
##             ' ALREADY POSITIVES',
##             'Mary likes John',
##             'a boy disappeared',
##             'John eats sandwiches',
##             'a boy finds cats',
##             'the boy finds cats',
##             'Kim believes John likes her',
##             'the students vanished with the telescope',
##             'every woman likes John', 
##             'Kim believes John likes her',
             #----------------------------------
             # MISSING - add these to the grammar
##             #----------------------------------
##             ' POSITIVES',
             'the dog chased the cat which ate the mouse',
             'people chase Sue who ate the unicorn which Tom saw',
             'Jody who chases dogs tries to find Tom who likes all cats',
             'John has a little sister who plays with unicorns',
             'the park which John hates has unicorns',
             'Mary saw Sue who ate sandwich',
             'David ate pizza which Tom gave',
             'Jody read book which unicorns left at the park',
             'the house which Jody lives is very big',
             'the men who went to the park see the stars with the telescope which the boy find',
             'people like children who play with unicorns',
             'the fish fishes fishes fish fishes',
             #----------------------------------
             # NEGATIVES - these are true negatives
             #----------------------------------
##             ' NEGATIVES',
             'a boy find cats',
             'students comes unicorns',
             'students come unicorns',
             'the dog chased who the cat ate the mouse',
             'people chase Sue which ate the unicorn who Tom saw',
             'Jody reads books at the park who unicorns play with children',
             'John has a little sister with what he plays at the park',
             'David ate pizza which Tom gave pizza',
             'the house which Jody eats sandwiches is very big',
             'the dog whom John likes very much disappeared from the park',
             'some dogs like all cats where eat mice',
             'a child which chases cats tries to eat sandwiches',
             'Sue who she likes Kim hates Mary',
             'Tom chases the dog who chases the cat whom chases the mouse',
             'John whom disappeared from the park lives in a car',
             'David which he reads books plays in the park',
             'Jody left the children in the park who the unicorns play',
             'Kim went to the car which Mary likes the car',
             ]


for sentence in sentences:
    tokens = sentence.split()
    print sentence
    try: 
        # if empty no parse possible
        for tree in cp.nbest_parse(tokens):
##            print tree
            print "OK"
##            break
    except: 
        # such as missing word in grammar
        print "ERROR IN PARSE"
        for e in sys.exc_info():
            print e
    print

    
