import re
import string
import sys

class HTMLTokenizer:

    def __init__(self, abbreviations, infile):
        with open(abbreviations, "r") as f:
            self.abv = f.read()
        self.infile = infile

    def obtain_sentences(self, file = "output.txt"):
        text = open(file, "r").read()
        return text

    def split_sentences(self, text):
        sent_pattern = r"(?<=[a-zäöü][.!?])\s+"
        sentences = re.split(sent_pattern, infile)
        return sentences

    def tokenizer_sent(self, split):
        new_split = list()
        for sentence in split:
            for pos, char in enumerate(sentence):
                if char in string.punctuation:
                    sentence = sentence.replace(char, " " + char + " ")
            new_split.append(sentence)

        tokenized_pattern = ["<s>" + sentence + "</s>" + "\n" for sentence in new_split]
        for tokenized_pat in tokenized_pattern:
            print("|".join(tokenized_pat.split()))

tokenizer = HTMLTokenizer(sys.argv[1], sys.argv[2])
infile = tokenizer.obtain_sentences()
sentences = tokenizer.split_sentences(infile)
print(tokenizer.tokenizer_sent(sentences))