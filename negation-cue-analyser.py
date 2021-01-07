import codecs
import glob




papers = glob.glob("*.txt")                                                    #get the name of all txt files in the folder
for z in papers:                                                                #pick one text file name from the list
    print(z)
    with codecs.open(z, 'r', encoding='utf8') as f:                             
        text = f.read()
        text = text.replace("\n", "")                                          #delete every symbol for new line
        text = text.split(" ")                                                  #devide the text to words
    list_neg_cue = ["not", "without", "no","never", "failed","nor"]             #list of adverbs negation cues
    for i in list_neg_cue:
        neg_counter = 0
        for x in text:
            if x.lower() == i:                                                  #search for the negation cues in the text
                neg_counter+=1
        print(neg_counter, i)
    opening_negation_cue = ["anti", "un","non","dis","no"]                      # list of prefix negation cues
    for cue in opening_negation_cue:
        neg_counter = 0
        for word in text:
            word_opening = word[0:len(cue)].lower()
            if len(cue)<len(word):
                if cue == word_opening:
                    neg_counter+=1
        print(neg_counter, cue)                                                 #print the results
    ending_cue = "n't"
    neg_counter = 0
    for word in text:
        word_ending = word[-len(ending_cue):len(word)].lower()
        if ending_cue == word_ending:
                neg_counter+=1
    print(neg_counter, ending_cue)
    print("****")