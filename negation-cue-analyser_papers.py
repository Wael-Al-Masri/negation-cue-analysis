import codecs
import glob
from nltk.corpus import words



def advance_analyser(token_list):
    negation_cue_list = [["-Less",0],["Ir-", 0],["Im-",0],["Un-",0],["Dis-",0],["In-",0],["De-",0],["Mis-",0]]
    for i in token_list:
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
                    #print(x)
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
                    #print(x)
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
    for z in negation_cue_list:
        print(z[1]," ", z[0])


papers = glob.glob("*.txt")                                                    #get the name of all txt files in the folder
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
        print(neg_counter," ", i)
    opening_negation_cue = ["anti-", "non-","no-"]                      # list of prefix negation cues
    for cue in opening_negation_cue:
        neg_counter = 0
        for word in text:
            word_opening = word[0:len(cue)].lower()
            if len(cue)<len(word):
                if cue == word_opening:
                    neg_counter+=1
        print(neg_counter," ", cue)                                                 #print the results
    ending_cue = "-n't"
    neg_counter = 0
    for word in text:
        word_ending = word[-len(ending_cue):len(word)].lower()
        if ending_cue == word_ending:
                neg_counter+=1
    print(neg_counter, " ", ending_cue)
    advance_analyser(text)
    print("****")