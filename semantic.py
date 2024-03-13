# Practical Task 1 of Task 20 - NLP - Semantic similarity

# comparing words and examining the similarity results given by spaCy

import spacy

nlp = spacy.load('en_core_web_lg')

#comparing words
word_1 = "cat"
word_2 = "monkey"
word_3 = "banana"

word_1doc = nlp(word_1)
word_2doc = nlp(word_2)
word_3doc = nlp(word_3)

print("\nSimilarity between cat, monkey and banana:")
print(f"Similarity between cat and monkey: {word_1doc.similarity(word_2doc)}")
print(f"Similarity between banana and monkey: {word_3doc.similarity(word_2doc)}")
print(f"Similarity between banana and cat: {word_3doc.similarity(word_1doc)}")
print("Observation: monkey has higher similarity to cat. Banana has higher similarity to monkey than to cat.\n")

# comparing another set of words
word_1 = "theatre"
word_2 = "cinema"
word_3 = "actor"

word_1doc = nlp(word_1)
word_2doc = nlp(word_2)
word_3doc = nlp(word_3)

print("Similarity between theatre, cinema and actor:")
print(f"Similarity between theatre and cinema: {word_1doc.similarity(word_2doc)}")
print(f"Similarity between actor and cinema: {word_3doc.similarity(word_2doc)}")
print(f"Similarity between actor and theatre: {word_3doc.similarity(word_1doc)}")
print("Observation: theatre and cinema have highest similarity. Actor is similar to both theatre and cinema.\n")

print("example.py running on simpler language model en_core_web_sm has no word vectors and runs similarity method based on tagger, parser and NER.\n")
