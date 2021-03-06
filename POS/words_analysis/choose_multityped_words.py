# Samples 10% of each POS tag type in dictionaries/words_nltk.json and dictionaries/words_stanza.json
# Before sampling, filter out ones with only 1 type pos, threshold -> appeared 3 times.
import pandas as pd
import json

# nltk
with open('../dictionaries/lemmatized/words_nltk.json') as nltk:
    words_nltk_dict = json.load(nltk)
    print("Before filtering, NLTK detected %i words." % len(words_nltk_dict.keys()))
    ## unlemmatized: 3556
    # lemmatized: 2762
    new_word_dict = {key:val for key, val in words_nltk_dict.items() if not (val["word_count"]>=3 and len(val.keys())==2)}
    new_word_dict = dict(sorted(new_word_dict.items(), key=lambda x: x[0].lower()))
    print("After filtering: %i words left." % len(new_word_dict))
    ## unlemmatized: 2690
    ## lemmatized: 2273

with open('../dictionaries/lemmatized/words_nltk_multi_typed.json', 'w') as fp:
    json.dump(new_word_dict, fp, indent=4)

# stanza
with open('../dictionaries/lemmatized/words_stanza.json') as stanza:
    words_stanza_dict = json.load(stanza)
    print("Before filtering, Stanza detected %i words." % len(words_stanza_dict.keys()))
    # unlemmatized: 3541
    # lemmatized: 2748
    new_word_dict = {key:val for key, val in words_stanza_dict.items() if not (val["word_count"]>=3 and len(val.keys())==2)}
    new_word_dict = dict( sorted(new_word_dict.items(), key=lambda x: x[0].lower()) )
    print("After filtering: %i words left." % len(new_word_dict))
    ## unlemmatized: 2487
    ## lemmatized: 2110

with open('../dictionaries/lemmatized/words_stanza_multi_typed.json', 'w') as fp:
    json.dump(new_word_dict, fp, indent=4)