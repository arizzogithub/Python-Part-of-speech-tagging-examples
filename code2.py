import nltk #import nltk
from nltk.tag import RegexpTagger #import RegexpTagger 
from nltk.corpus import treebank #import treebank corpus
treebank_tagged_sents = treebank.tagged_sents()#initialising treebank_tagged_sents 

patterns = [
    (r'.*ing$', 'VBG'),                         # gerunds
    (r'.*ed$', 'VBD'),                          # simple past
    (r'.*es$', 'VBZ'),                          # 3rd singular present
    (r'.*ould$', 'MD'),                         # modals
    (r'.*\'s$', 'NN$'),                         # possessive nouns
    (r'.*s$', 'NNS'),                           # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),            # cardinal numbers
    (r'(The|the|A|a|An|an)$', 'AT'),            # articles 
    (r'.*able$', 'JJ'),                         # adjectives 
    (r'.*ness$', 'NN'),                         # nouns formed from adjectives
    (r'.*ly$', 'RB'),                           # adverbs
    (r'(He|he|She|she|It|it|I|me|Me|You|you)$', 'PRP'), # pronouns
    (r'(His|his|Her|her|Its|its)$', 'PRP$'),    # possessive pronouns
    (r'(my|Your|your|Yours|yours)$', 'PRP$'),   # possessive pronouns
    (r'(on|On|in|In|at|At|since|Since)$', 'IN'),# time prepositions
    (r'(for|For|ago|Ago|before|Before)$', 'IN'),# time prepositions
    (r'(till|Till|until|Until)$', 'IN'),        # time prepositions
    (r'(by|By|beside|Beside)$', 'IN'),          # space prepositions
    (r'(under|Under|below|Below)$', 'IN'),      # space prepositions
    (r'(over|Over|above|Above)$', 'IN'),        # space prepositions
    (r'(across|Across|through|Through)$', 'IN'),# space prepositions
    (r'(into|Into|towards|Towards)$', 'IN'),    # space prepositions
    (r'(onto|Onto|from|From)$', 'IN'),          # space prepositions

    (r'(and|And|or|Or|but|But)$', 'CC'),        # coordinate conjunctions
    (r'(if|If|when|When)$', 'IN'),              # subordinate conjunctions
    (r'\.$','.'), (r'\,$',','), (r'\?$','?'),   # full stop, comma, ?mark
    (r'\($','('), (r'\)$',')'),                 # round brackets
    (r'\[$','['), (r'\]$',']'),                 # square brackets
    (r'(Sam)$', 'NAM'),
    (r'.*', 'NN')                               # nouns (default)
    ]

regexp_tagger = nltk.RegexpTagger(patterns)
print('RegexpTagger accuracy %4.1f%%' % (100.0 * regexp_tagger.evaluate(treebank_tagged_sents))) #calculate and print Accuracy
