import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)

for i in tokenized:
    words = nltk.word_tokenize(i)
    tagged = nltk.pos_tag(words)

    named_entity = nltk.ne_chunk(tagged)

    named_entity.draw()