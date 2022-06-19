# import torch
# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# tokenizer = AutoTokenizer.from_pretrained("google/roberta2roberta_L-24_gigaword")
# model = AutoModelForSeq2SeqLM.from_pretrained("google/roberta2roberta_L-24_gigaword")
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

def summarize(text, per):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    word_frequencies={}
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1
    max_frequency=max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency
    sentence_tokens= [sent for sent in doc.sents]
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():                            
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+=word_frequencies[word.text.lower()]
    select_length=int(len(sentence_tokens)*per)
    summary=nlargest(select_length, sentence_scores,key=sentence_scores.get)
    final_summary=[word.text for word in summary]
    summary=''.join(final_summary)
    return summary

# context = """The lifeless bodies of at least 20 civilian men line a single street in the town of Bucha near the Ukrainian capital. Some lie face down on the pavement while others are collapsed on their backs, mouths open in a tragic testament to the horrors of Russian occupation.

# The hands of one man are tied behind his back with a piece of white cloth. Another man lies alone, tangled up in a bicycle by a grassy bank. A third man lies in the middle of the road, near the charred remains of a burned-out car.

# The shocking images of the carnage in Bucha were captured by Agence France-Presse on Saturday, the same day Ukraine declared the town liberated from Russian troops. Accounts of alleged Russian atrocities are emerging as its forces retreat from areas near Kyiv following a failed bid to encircle the capital.

# The town of Bucha has endured five weeks of near-constant firefights. Now officials and human rights groups are blaming the civilian deaths on the departed Russian forces.

# “Corpses of executed people still line the Yabluska street in Bucha. Their hands are tied behind their backs with white ‘civilian’ rags, they were shot in the back of their heads. So you can imagine what kind of lawlessness they perpetrated here,” Bucha mayor Anatoliy Fedoruk told Reuters on Saturday."""
# out=summarize(context, 0.3)
# print(out)