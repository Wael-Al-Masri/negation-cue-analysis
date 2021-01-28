import codecs
import glob
from nltk.corpus import words
 
def list_of_tokens(inputfile):
    """ This function go through the input file and pick only the tokens and save them in a list.

        :param inputfile: a file path to the inputfile
        :type inputfile : string
        "return: Tokes list and every feature column """

    tokens_list = []
    column_list= []
    columns = []
    sentance_number = 0
    with open(z, 'r+', encoding = 'utf8') as infile:
        for line in infile:
            if len(line) != 1:
                columns_strip = line.rstrip('\n').split("\t")
                columns.append(columns_strip)
                if int(columns_strip[1]) == sentance_number:
                    column_list.append(columns_strip[3])                         
                else:
                    tokens_list.append(column_list)
                    column_list= []
                    sentance_number = int(columns_strip[1])
                    column_list.append(columns_strip[3])
        tokens_list.append(column_list)
    return tokens_list, columns
 
def analyse(token_list):
    """ This function loop through the list of negation cues and search for them in the tokens list.

    :param token_list: a list of tokens
    :type token_list : list"""                                                                                                              
    list_neg_cue = ["not", "without", "no","never", "failed", "nor", "nothing", "neither", "nobody", "none", "n't"]             #list of negation cues
    for i in list_neg_cue:
        neg_counter = 0
        for x in token_list:
            for z in x:
                if z.lower() == i:                                                                                      #search for the negation cues in the token list
                    neg_counter+=1
        print(neg_counter, i)
    
def advance_analyser(token_list):
    """ This function loop through the list of lists of negation cues and search for them in the tokens list after that delete the cue part from the token and check if the rest of the token is a qord in the English dictionary.

    :param token_list: a list of tokens
    :type token_list : list"""  

    negation_cue_list = [["-Less",0],["Ir-", 0],["Im-",0],["Un-",0],["Dis-",0],["In-",0],["De-",0],["Mis-",0]]
    for i in token_list:
        for x in i:
            if "less" in x:
                root = x.split("less")[0]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[0][1] +=1
            elif "ir" in x[0:2]:
                root = x.split("ir")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[1][1] +=1
            elif "im" in x[0:2]:
                root = x.split("im")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[2][1] +=1
            elif "un" in x[0:2]:
                root = x.split("un")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[3][1] +=1
                        #print(x)
            elif "dis" in x[0:3]:
                root = x.split("dis")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[4][1] +=1
            elif "in" in x[0:2]:
                root = x.split("in")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[5][1] +=1
                        #print(x)
            elif "de" in x[0:2]:
                root = x.split("de")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[6][1] +=1
            elif "mis" in x[0:3]:
                root = x.split("mis")[1]
                if len(root)>2:
                    if root in words.words():
                        negation_cue_list[7][1] +=1
    for z in negation_cue_list:
        print(z[0]," ", z[1])


if __name__ == '__main__':
    papers = glob.glob("papers\*.txt")
    print(papers)                                                                             #get the name of all txt files in the folder
    for z in papers:                                                                                        #pick one text file name from the list
        print(z) 
        list_papers = list_of_tokens(z)
        analyse(list_papers)
        advance_analyser(list_papers)
        print("****")