import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import BernoulliNB
import confidence_evaluation as cls_eva


feature_to_index = {'Token': 3, 'Lemma': 4, 'Pos': 5, 'Chunklabel': 6, 'depREL': 7, 'PToken': 8, 'PTokenPOS': 9, 'Negation':10}
                    
def extract_features_and_labels(trainingfile, selected_features):
    """ The training file is read and the features and labels are extracted and returned
    
    :param trainingfile: the path to the input file
    
    :returns: one dictionary containing the features and another one containing the NER labels
    """
    data = []
    targets = []
    with open(trainingfile, 'r+', encoding='utf8') as infile:
        for line in infile:
            components = line.rstrip('\n').split()
            if len(components) > 0:
                feature_value = {}
                for feature_name in selected_features:
                    row_index = feature_to_index.get(feature_name)
                    feature_value[feature_name] = components[row_index]
                data.append(feature_value)
                        #gold is in the last column
                targets.append(components[-1])
    return data, targets

def extract_features(inputfile, selected_features):
    """ The input file is read and the features are extracted and returned
    
    :param trainingfile: the path to the input file
    
    :returns: a dictionary containing the features
    """
    data = []
    with open(inputfile, 'r+', encoding='utf8') as infile:
        for line in infile:
            components = line.rstrip('\n').split()
            if len(components) > 0:
                feature_value = {}
                for feature_name in selected_features:
                    row_index = feature_to_index.get(feature_name)
                    feature_value[feature_name] = components[row_index]
                data.append(feature_value)
    return data

def create_classifier(train_features, train_targets, modelname):
    """ A classifier is created by using the training file features in order to create vectors and these vectors and the training file targets are then used to create the model.
    
    :param train_features: the features of the training file that were extracted
    :param train_targets: the targets of the training file that were extracted
    :param modelname: the name of the model that is being used
    
    :returns: the fitted model that includes the feature vectors and the training file targets as well as the vectoriser
    """
   
    if modelname ==  'logreg':
        model = LogisticRegression()
        vec = DictVectorizer()
        features_vectorized = vec.fit_transform(train_features)
        model.fit(features_vectorized, train_targets)
    elif modelname ==  'NB':
        model = MultinomialNB()
        vec = DictVectorizer()
        features_vectorized = vec.fit_transform(train_features)
        model.fit(features_vectorized, train_targets)
    elif modelname ==  'SVM':
        model = LinearSVC()
        vec = DictVectorizer()
        features_vectorized = vec.fit_transform(train_features)
        model.fit(features_vectorized, train_targets)
    elif modelname == 'Bernoulli':
        model = BernoulliNB()
        vec = DictVectorizer()
        features_vectorized = vec.fit_transform(train_features)
        model.fit(features_vectorized, train_targets)
    elif modelname ==  'baseline':
        model = LinearSVC()
        vec = DictVectorizer()
        features_vectorized = vec.fit_transform(train_features)
        model.fit(features_vectorized, train_targets)
        
    return model, vec

def get_predicted_and_gold(inputdata, vec, model, selected_features):
    """ the features of the input file are read, classified and then written on a new file.
    :param inputdata: the path to the input data
    :param vec: the vectoriser that is used to transform the features into vectors
    :param model: the model thas created by using the training file's training vectorised features and the regular targets
    :param selected_features: a list with the feature combination that needs to be analysed
    
    :returns: the predictions of the model and a dictionary containing the NER labels
    """
  
    features, goldlabels =extract_features_and_labels(inputdata, selected_features)
    #we need to use the same fitting as before, so now we only transform the current features according to this mapping (using only transform)
    features = vec.transform(features)
    predictions = model.predict(features)
    
    return predictions, goldlabels

def classify_data(model, vec, inputdata, outputfile, selected_features):
    """ the features of the input file are read, classified and then written on a new file.
    :param model: the model thas created by using the training file's training vectorised features and the regular targets
    :param vec: the vectoriser that is used to transform the features into vectors
    :param inputdata: the path to the input data
    :param outputfile: the path to the output file
    
    :writes: output file with classified data of the input data 
    """
  
    features = extract_features(inputdata, selected_features)
    features = vec.transform(features)
    predictions = model.predict(features)
    outfile = open(outputfile, 'w')
    counter = 0
    headers = 'Chapter','SentNumber',  'TNumber','Token', 'Lemma','POS', 'Chunk', 'DepREL','PToken', 'PTokenPOS','Negation'
    with open(inputdata, 'r') as infile:
        firstline = infile.readline()
        if firstline:
            outfile.write('\t'.join(headers) + '\n')
    for line in open(inputdata, 'r'):
        if len(line.rstrip('\n').split()) > 0:
            outfile.write(line.rstrip('\n') + '\t' + predictions[counter] + '\n')
            counter += 1
    outfile.close()
    
def print_confusion_matrix(predictions, goldlabels):
    '''
    Function that prints out a confusion matrix
    
    :param predictions: predicted labels
    :param goldlabels: gold standard labels
    :type predictions, goldlabels: list of strings
    '''
    #based on example from https://datatofish.com/confusion-matrix-python/ 
    data = {'Gold':    goldlabels, 'Predicted': predictions    }
    df = pd.DataFrame(data, columns=['Gold','Predicted'])

    confusion_matrix = pd.crosstab(df['Gold'], df['Predicted'], rownames=['Gold'], colnames=['Predicted'])
    print (confusion_matrix)
    
def print_precision_recall_fscore(predictions, goldlabels):
    '''
    Function that prints out precision, recall and f-score
    
    :param predictions: predicted output by classifier
    :param goldlabels: original gold labels
    :type predictions, goldlabels: list of strings
    '''
    
    precision = metrics.precision_score(y_true=goldlabels,
                        y_pred=predictions,
                        average='macro')

    recall = metrics.recall_score(y_true=goldlabels,
                     y_pred=predictions,
                     average='macro')


    fscore = metrics.f1_score(y_true=goldlabels,
                 y_pred=predictions,
                 average='macro')
    
    accuracy = accuracy_score(y_true=goldlabels,
                 y_pred=predictions)

    print('P:', precision, 'R:', recall, 'F1:', fscore, 'A:', accuracy)
    
def main(argv=None):
    """ A list of commandline arguments are used to define the training file, input file and output file and then the whole process of classifying the data is guided
    
    :param argv: similar to an array, this is a parameter that is already predefined to 'None'. 
    
    :prints: the incorrectly classified tokens when run from the command line
    """
    
    #a very basic way for picking up commandline arguments
    if argv is None:
        argv = sys.argv
    
    trainingfile = argv[1]
    inputfile = argv[2]
    outputfile =argv[3]
    #Note 1: argv[0] is the name of the python program if you run your program as: python program1.py arg1 arg2 arg3
    #Note 2: sys.argv is simple, but gets messy if you need it for anything else than basic scenarios with few arguments
    #you'll want to move to something better. e.g. argparse (easy to find online)
    
    #features that are analysed, these can be adjusted based on which feature combination you want to analyse
    all_features = ['Token', 'Lemma', 'Pos', 'Chunklabel', 'depREL', 'PToken', 'PTokenPOS']
    baseline_feature = ['Token']
    training_features, gold_labels = extract_features_and_labels(trainingfile, all_features)
    baseline_features, gold_labels = extract_features_and_labels(trainingfile, baseline_feature)
    
    for modelname in ['logreg', 'NB', 'baseline', 'SVM', 'Bernoulli']:
        
        if modelname == 'logreg':
            print('Logistic Regression')
            ml_model, vec = create_classifier(training_features, gold_labels, 'logreg')
            classify_data(ml_model, vec, inputfile, outputfile.replace('.txt','.' + modelname + '.txt'), all_features)
            predictions, goldlabels = get_predicted_and_gold(inputfile, vec, ml_model, all_features)
            print_confusion_matrix(predictions, goldlabels)
            print_precision_recall_fscore(predictions, goldlabels)
            print(" ")
        if modelname == 'NB':
            print('Naive Bayes')
            ml_model, vec = create_classifier(training_features, gold_labels, 'NB')
            classify_data(ml_model, vec, inputfile, outputfile.replace('.txt','.' + modelname + '.txt'), all_features)
            predictions, goldlabels = get_predicted_and_gold(inputfile, vec, ml_model, all_features)
            print_confusion_matrix(predictions, goldlabels)
            print_precision_recall_fscore(predictions, goldlabels)
            print(" ")
        if modelname == 'baseline':
            print('baseline SVM')
            ml_model, vec = create_classifier(baseline_features, gold_labels, 'baseline')
            classify_data(ml_model, vec, inputfile, outputfile.replace('.txt','.' + modelname + '.txt'), baseline_feature)
            predictions, goldlabels = get_predicted_and_gold(inputfile, vec, ml_model, baseline_feature)
            print_confusion_matrix(predictions, goldlabels)
            print_precision_recall_fscore(predictions, goldlabels)
            print(" ") 
        if modelname == 'SVM':
            print('SVM')
            ml_model, vec = create_classifier(training_features, gold_labels, 'SVM')
            classify_data(ml_model, vec, inputfile, outputfile.replace('.txt','.' + modelname + '.txt'), all_features)
            predictions, goldlabels = get_predicted_and_gold(inputfile, vec, ml_model, all_features)
            print_confusion_matrix(predictions, goldlabels)
            print_precision_recall_fscore(predictions, goldlabels)
            print(" ")  
        if modelname == 'Bernoulli':
            print('Bernoulli')
            ml_model, vec = create_classifier(training_features, gold_labels, 'Bernoulli')
            classify_data(ml_model, vec, inputfile, outputfile.replace('.txt','.' + modelname + '.txt'), all_features)
            predictions, goldlabels = get_predicted_and_gold(inputfile, vec, ml_model, all_features)
            print_confusion_matrix(predictions, goldlabels)
            print_precision_recall_fscore(predictions, goldlabels)
            print(" ")
    confidence = cls_eva.main()

if __name__ == '__main__':
    argv = ['python','SEM-2012-SharedTask-CD-SCO-training-simple1.txt','SEM-2012-SharedTask-CD-SCO-dev-simple1.txt', 'final.txt'  ]
    main(argv)
    print("done")
