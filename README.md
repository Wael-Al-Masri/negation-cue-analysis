# negation-cue-analysis
analysis the negation cue in text

Authors: Dilara Çelik, Jasmine van Vugt, Wael al Masri, Amber Pichel
Date: 20-01-2021

In this file, the requirements that are needed in order to run the code are provided.
There are certain libraries that will need to be installed beforehand. These libraries can be installed with:

conda install pandas
pip install -U scikit-learn
pip install --user -U nltk
pip install -U spacy
pip install -U scipy
pip install -U numpy
pip install -U pandas

Code:

All of the code that has been used is placed within the 'SEM-2012-SharedTask-CD-SCO-simple' folder. In order to run all the code, there are a two text files that are of importance and normally need to be downloaded from the files section of the Applied Text Mining course:

- SEM-2012-SharedTask-CD-SCO-dev-simple
- SEM-2012-SharedTask-CD-SCO-training-simple

However, for convenience, these have been already included in the 'SEM-2012-SharedTask-CD-SCO-simple' folder, so the python scripts can be run directly from the command line.

The first code that is introduced is the 'negation-cue-analyser.py' python script. This is a script that goes over the input text file and counts the instances of negation cues and returns these. In order to run this code, the previously mentioned files should be located in the 'SEM-2012-SharedTask-CD-SCO-simple' folder. In general, this can be run as-is. However, if there are any issues, the file-path might be checked. Modules are already in the files, but the modules that are needed to run this code: glob and codecs
The second code that has been written is the 'AddedFeatures.py' python script. In this script, the text files are pre-processed and then features are added to the file as columns. Lastly, this is all written to a new output file and saved in the 'SEM-2012-SharedTask-CD-SCO-simple' folder. In order to run this code, the previously mentioned files should be located in the 'SEM-2012-SharedTask-CD-SCO-simple' folder. In general, this can be run as-is. However, if there are any issues, the file-path might be checked. Modules are already in the files, but the modules that are needed to run this code: from nltk.parse.corenlp the module CoreNLPParsersys, spacy, from spacy.symbols the modules ORTH, LEMMA, POS, from spacy.tokenizer the module Tokenizer, from spacy.lang.char_classes the modules ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS, and from spacy.util the module compile_infix_regex.
The third code is a python script called 'ClassifiersPrediction.py'. In this script, the features from the columns and the gold labels from the training file are obtained, while the features from the developmental data is also obtained. After this, the features are transformed and fitted according to each classfier that is used. All of the classifiers then make predictions and these predictions are stored in new files. Additionally, the evaluation scores are also printed with the confusion metrix as well. In order to run this code, the previously mentioned files should be located in the 'SEM-2012-SharedTask-CD-SCO-simple' folder. In general, this can be run as-is. However, if there are any issues, the file-path might be checked. MModules are already in the files, but the modules that are needed to run this code: pandas as pd, from sklearn.linear_model the module LogisticRegression, from sklearn.feature_extraction the module DictVectorizer, from sklearn.naive_bayes the module MultinomialNB, from sklearn.svm the module LinearSVC, from sklearn the module metrics, from sklearn.metrics the module accuracy_score, from sklearn.naive_bayes the module BernoulliNB
