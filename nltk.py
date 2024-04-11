import nltk
from nltk.corpus import wordnet as wn

# Download NLTK resources (only need to run once)
nltk.download('punkt')
nltk.download('wordnet')

def detect_word_origin(word):
    synsets = wn.synsets(word)
    origins = set()
    for synset in synsets:
        origins.update(synset.lemma_names())
    return origins

def main():
    input_text = input("Enter a sentence: ")
    words = nltk.word_tokenize(input_text)
    for word in words:
        origins = detect_word_origin(word)
        print(f"Word: {word}, Origins: {', '.join(origins)}")

main()
