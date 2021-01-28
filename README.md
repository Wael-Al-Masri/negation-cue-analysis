# negation-cue-analysis

analysis the negation cue in text

Authors: Dilara Çelik, Jasmine van Vugt, Wael al Masri, Amber Pichel

Date: 28-01-2021

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

- Data\SEM-2012-SharedTask-CD-SCO-dev-simple
- Data\SEM-2012-SharedTask-CD-SCO-training-simple
- Data\SEM-2012-SharedTask-CD-SCO-test-circle

However, for convenience, these have been already included and should be there when having unzipped the zip file, so the python scripts can be run directly from the command line.

How to run the first code: 
1) 'negation-cue-analyser_Data.py': 
- Script that goes over the input text file and counts the instances of negation cues and returns these. 
- This code can be ran through the command line as is
- Example input file: 'Data\SEM-2012-SharedTask-CD-SCO-dev-simple.txt'. 
2)'negation-cue-analyser_Papers.py' 
- Does exactly the same as 'negation-cue-analyser_Data.py'.
- Receives as an input a whole article
3) Modules:
- glob and codecs
4) Output:
- a list of negation cues found in every paper with its frequency in the text.
5) Examples of system errors:
- “until”, “disease”, “individual”

How to run the second code:
1)'AddedFeatures.py'
- In this code text files are pre-processed.
- Features are added to the file as columns
- This is all written to a new output file
- Saved in the same place as the original file
- This code needs to be ran 3 times, once with training file, once with development file and once with test file
- First time it can be ran without any further adjustments which will be on the training file. 
- After that the filepaths can be changed to:'Data\SEM-2012-SharedTask-CD-SCO-dev-simple.txt' for the input file and 'Data\SEM-2012-SharedTask-CD-SCO-dev-simple1.txt' for the outputfile.
- Lastly, for the test file the filepaths can be changed to: 'Data\SEM-2012-SharedTask-CD-SCO-test-circle.txt' for the input file and 'Data\SEM-2012-SharedTask-CD-SCO-test-circle1.txt' for the output file. 
#NOTE: this code might take a bit longer to run
2) Run in command line:
- specify the input file and a new output file
- Example: 'Data\SEM-2012-SharedTask-CD-SCO-train-simple.txt' and 'newtrainfile.txt'
3) Modules:
- from nltk.parse.corenlp the module CoreNLPParsersys
- spacy
- from spacy.symbols the modules ORTH, LEMMA, POS
- from spacy.tokenizer the module Tokenizer
- from spacy.lang.char_classes the modules ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
- from spacy.util the module compile_infix_regex

How to run the third code:
1)'ClassifiersPrediction.py'
- Features columns obtained
- gold labels from training file obtained
- features development data obtained
- After that: features are transformed and fitted according to each classifier
- Classifier makes prediction, which is stored in a new file
- Evaluation score and confusion matrix are printed
2)Run in command line:
- Specify the training file, the input file and the new output file
- This code can be ran from the command line as is
3) Modules:
- pandas as pd
- from sklearn.linear_model the module LogisticRegression
- from sklearn.feature_extraction the module DictVectorizer
- from sklearn.naive_bayes the module MultinomialNB
- from sklearn.svm the module LinearSVC
- from sklearn the module metrics
- from sklearn.metrics the module accuracy_score
- from sklearn.naive_bayes the module BernoulliNB

How to run the final code:
1)'ErrorAnalysis.py'
- This code can be ran from the command line as is. With the SVM final file.
- This script looks whether gold label B-neg is not predicted as B-neg
- Whether a gold label of I-neg is not predicted as I-neg.
- Not matching labels: sentence number, token number, and token will be printed out.
2) Modules:
- import sys
