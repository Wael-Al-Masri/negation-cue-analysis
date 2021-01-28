import operator
from scipy import stats
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import LinearSVC
import pandas as pd



class classifierPicker:
    def __init__(self, *classifiers):
        """ This function use OOP to save an object and recall it later.

        :param classifiers: classifiers name
        :type classifiers : classifiers """
        self._classifiers = classifiers

    def classify(self, train, val):
        # Trains and stores fitted classifiers, and scores on test set
        """Trains and stores fitted classifiers, and scores on test set.

        :param train: a list of training data
        :type train : list
        :param val: a list of predicted data
        :type val : list """
        self.votes = {}
        self.fitted_clfs = {}
        for c in self._classifiers:
            clf = c()
            clf_name = repr(clf).split('(')[0] 
            clf.fit(train[0], train[1])
            self.fitted_clfs.update({clf_name : clf})
            self.votes.update({clf_name: clf.score(val[0], val[1])})
        return self.votes
    
    def get_best_classifier(self):
        # Returns name of best classifier
        return max(self.votes.items(), key=operator.itemgetter(1))[0]
        

    def confidence(self, X):
        """ Takes majority vote .

        :param X: a List of testing data
        :type X : list """
        all_preds = []
        if len(X.shape)==1:
            X = X.reshape(1, -1)
        for cn, c in self.fitted_clfs.items():
            preds = c.predict(X)
            all_preds.append(preds)
        array = np.array(all_preds)
        return stats.mode(array).mode[0]
            
            
                

def main():

    """ Read the data set and call the other function as well as printing the scores, the name of the best classifiers and the votes"""
    df = pd.read_csv('Data\data_csv.csv')
    
    df_encoded = df.apply(LabelEncoder().fit_transform)
    
    df = df.drop(['Unnamed: 0'], axis=1)
    
    X, y = df_encoded.drop(['Negation'], axis=1).to_numpy(), df_encoded['Negation'].to_numpy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    
    cp = classifierPicker(MultinomialNB, LogisticRegression, LinearSVC, BernoulliNB)
    print('Scores : \n\t', cp.classify([X_train, y_train], [X_test, y_test]))
    print('\nBest Classifier :', cp.get_best_classifier())
    print('\nMajority votes :', cp.confidence(X_test[:5]))
    

if __name__ == '__main__':
    main()