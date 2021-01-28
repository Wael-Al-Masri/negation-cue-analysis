import codecs
import glob
from nltk.corpus import words



def advance_analyser(token_list):
    """ This function loop through the list of lists of negation cues and search for them in the tokens list after that delete the cue part from the token and check if the rest of the token is a qord in the English dictionary.

    :param token_list: a list of tokens
    :type token_list : list""" 
    negation_cue_list = [["-Less",0],["Ir-", 0],["Im-",0],["Un-",0],["Dis-",0],["In-",0],["De-",0],["Mis-",0],["anti", 0],["none",0]]
    for i in token_list:
        i = i.lower()
        if "less" in i:
            root = i.split("less")[0]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[0][1] +=1
        elif "ir" in i[0:2]:
            root = i.split("ir")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[1][1] +=1
        elif "im" in i[0:2]:
            root = i.split("im")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[2][1] +=1
        elif "un" in i[0:2]:
            root = i.split("un")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[3][1] +=1
        elif "dis" in i[0:3]:
            root = i.split("dis")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[4][1] +=1
        elif "in" in i[0:2]:
            root = i.split("in")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[5][1] +=1
        elif "de" in i[0:2]:
            root = i.split("de")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[6][1] +=1
        elif "mis" in i[0:3]:
            root = i.split("mis")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[7][1] +=1
        elif "anti" in i[0:4]:
            root = i.split("anti")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[8][1] +=1
        elif "non" in i[0:3]:
            root = i.split("non")[1]
            if len(root)>2:
                if root in words.words():
                    negation_cue_list[9][1] +=1
    for z in negation_cue_list:
        print(z[1]," ", z[0])

def main():
    """ This function loop through the list of the files in the folder pick one file, toknize it and search for every negation cues and search for them in the tokens list.
    """
    papers = glob.glob("papers\*.txt")                                                    #get the name of all txt files in the folder
    for z in papers:                                                                #pick one text file name from the list
        print(z)
        with codecs.open(z, 'r', encoding='utf8') as f:                             
            text = f.read()
            text = text.replace("\n", "")                                          #delete every symbol for new line
            text = text.split(" ")                                                  #devide the text to words
        list_neg_cue = ["not", "without", "no","never", "failed","nor","nobody", "none"]             #list of adverbs negation cues
        for i in list_neg_cue:
            neg_counter = 0
            for x in text:
                if x.lower() == i:                                                  #search for the negation cues in the text
                    neg_counter+=1
            print(neg_counter," ", i)                                              #print the results
        ending_cue = "n't"
        neg_counter = 0
        for word in text:
            word_ending = word[-len(ending_cue)::].lower()
            if ending_cue == word_ending:
                    neg_counter+=1
        print(neg_counter, " -",ending_cue)
        advance_analyser(text)
        print("****")

if __name__ == '__main__':
    main()