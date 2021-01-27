# negation-cue-analysis

analysis the negation cue in text

Authors: Dilara Çelik, Jasmine van Vugt, Wael al Masri, Amber Pichel

Date: 26-01-2021

In this file, the requirements that are needed in order to run the code are provided.
There are certain libraries that will need to be installed beforehand. These libraries can be installed with:

conda install pandas

pip install scikit-learn

pip install nltk

pip install spacy

pip install scipy

pip install numpy

pip install pandas


Code:

All of the code that has been used is placed together. In order to run all the code, there are a two text files that are of importance and normally need to be downloaded from the files section of the Applied Text Mining course:

- SEM-2012-SharedTask-CD-SCO-dev-simple
- SEM-2012-SharedTask-CD-SCO-training-simple
- SEM-2012-SharedTask-CD-SCO-test-circle

However, for convenience, these have been already included and should be there when having unzipped the zip file, so the python scripts can be run directly from the command line.


The first code that is introduced is the 'negation-cue-analyser_Data.py' and 'negation-cue-analyser_Papers.py' python script. 'negation-cue-analyser_Data.py' is a script that goes over the input text file and counts the instances of negation cues and returns these. In order to run this code via the command line, one needs to specify the input file only. So for example: 'SEM-2012-SharedTask-CD-SCO-dev-simple.txt'. 'negation-cue-analyser_Papers.py' do exactly the same as 'negation-cue-analyser_Data.py'but it receive as an input a whole article while the 'negation-cue-analyser_Data.py'receive a list of tokens. Modules are already in the files, but the modules that are needed to run this code: glob and codecs
The second code that has been written is the 'AddedFeatures.py' python script. In this script, the text files are pre-processed and then features are added to the file as columns. Lastly, this is all written to a new output file and saved in the same place as the original file. In order to run this code via the command line, one needs to specify the input file and a new output file. So for example: 'SEM-2012-SharedTask-CD-SCO-train-simple.txt' and 'newtrainfile.txt'. Modules are already in the files, but the modules that are needed to run this code: from nltk.parse.corenlp the module CoreNLPParsersys, spacy, from spacy.symbols the modules ORTH, LEMMA, POS, from spacy.tokenizer the module Tokenizer, from spacy.lang.char_classes the modules ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS, and from spacy.util the module compile_infix_regex.
The third code is a python script called 'ClassifiersPrediction.py'. In this script, the features from the columns and the gold labels from the training file are obtained, while the features from the development data is also obtained. After this, the features are transformed and fitted according to each classfier that is used. All of the classifiers then make predictions and these predictions are stored in new files. Additionally, the evaluation scores are also printed with the confusion metrix as well.In order to run this code via the command line, one needs to specify the training file, the input file and the new output file. So the train simple file with the added features should be specified first and then either the development file or the test file can be written with a new output text file. Modules are already in the files, but the modules that are needed to run this code: pandas as pd, from sklearn.linear_model the module LogisticRegression, from sklearn.feature_extraction the module DictVectorizer, from sklearn.naive_bayes the module MultinomialNB, from sklearn.svm the module LinearSVC, from sklearn the module metrics, from sklearn.metrics the module accuracy_score, from sklearn.naive_bayes the module BernoulliNB
The final code that is used in this report is the 'ErrorAnalysis.py'. In order to run this script, the development file should be written as the input file. This can be done by writing: 'SEM-2012-SharedTask-CD-SCO-dev-simple.txt'. This script goes over all of the times that a gold label of B-neg is not predicted as B-neg and when a gold label of I-neg is not predicted as I-neg. If there are instances of not matching labels, then the sentence number, token number, and token will be printed out. Modules are already in the files, but the modules that are needed to run this code: import sys
