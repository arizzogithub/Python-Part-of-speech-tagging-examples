import nltk
from nltk.corpus import treebank #import treebank corpus
from nltk.tag import DefaultTagger #import DefaultTagger
tagger = DefaultTagger('NN') #Default Tagger with assigning NN tag
treebank_tagged_sents = treebank.tagged_sents() #initialising treebank_tagged_sents 
tagger.tag(treebank_tagged_sents) #tag treebank_tagged_sents
print('Accuracy %4.1f%%' % (100.0 * tagger.evaluate(treebank_tagged_sents))) #calculate and print Accuracy 
