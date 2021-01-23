from nltk.parse.corenlp import CoreNLPParser
import sys
import spacy
from spacy.symbols import ORTH, LEMMA, POS
from spacy.tokenizer import Tokenizer
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from spacy.util import compile_infix_regex
def list_of_tokens(inputfile):
    """
    Function that extracts all tokens from a given file and returns them as a list
    
    :param file: path to file
    :type file: string
    
    :return tokens: list of tokens
    """
    tokens_list = []
    column_list= []
    columns = []
    sentance_number = 0
    with open(inputfile, 'r+', encoding = 'utf8') as infile:
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

def custom_tokenizer(nlp):
    infixes = (
        LIST_ELLIPSES
        + LIST_ICONS
        + [
            r"(?<=[0-9])[+\-\*^\``](?=[0-9-])",
            r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
                al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
            ),
            r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
            #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
            r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
        ]
    )

    infix_re = compile_infix_regex(infixes)

    return Tokenizer(nlp.vocab, prefix_search=nlp.tokenizer.prefix_search,
                                suffix_search=nlp.tokenizer.suffix_search,
                                infix_finditer=infix_re.finditer,
                                token_match=nlp.tokenizer.token_match,
                                rules=nlp.Defaults.tokenizer_exceptions)



def dep_calculater(senatnce, nlp_module):
    nlp = nlp_module
    doc = nlp(senatnce)
    sent_dep_list=[]
    for token in doc:
        sent_dep_list.append(token.dep_)
    return(sent_dep_list)

def create_new_file(inputfile, outputfile):
    pre_proccessed = list_of_tokens(inputfile)
    tokens_list = pre_proccessed[0]
    columns = pre_proccessed[1]
    outfile = open(outputfile, 'w')
    nlp = spacy.load("en_core_web_sm")
    nlp.tokenizer = custom_tokenizer(nlp)
    nlp.tokenizer.add_special_case(u'1.',
    [
        {
            ORTH: u'1.',
            LEMMA: u'1',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'2.',
    [
        {
            ORTH: u'2.',
            LEMMA: u'2',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'3.',
    [
        {
            ORTH: u'3.',
            LEMMA: u'3',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'4.',
    [
        {
            ORTH: u'4.',
            LEMMA: u'4',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'5.',
    [
        {
            ORTH: u'5.',
            LEMMA: u'5',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'6.',
    [
        {
            ORTH: u'6.',
            LEMMA: u'6',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'7.',
    [
        {
            ORTH: u'7.',
            LEMMA: u'7',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'8.',
    [
        {
            ORTH: u'8.',
            LEMMA: u'8',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'9.',
    [
        {
            ORTH: u'9.',
            LEMMA: u'9',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'10.',
    [
        {
            ORTH: u'10.',
            LEMMA: u'10',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'11.',
    [
        {
            ORTH: u'11.',
            LEMMA: u'11',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'12.',
    [
        {
            ORTH: u'12.',
            LEMMA: u'12',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'13.',
    [
        {
            ORTH: u'13.',
            LEMMA: u'13',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'14.',
    [
        {
            ORTH: u'14.',
            LEMMA: u'14',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u"'86",
    [
        {
            ORTH: u"'86",
            LEMMA: u"86",
            POS: u'NUM'}
     ])
    nlp.tokenizer.add_special_case(u"'66",
    [
        {
            ORTH: u"'66",
            LEMMA: u"66",
            POS: u'NUM'}
     ])
    nlp.tokenizer.add_special_case(u"'m",
    [
        {
            ORTH: u"'m",
            LEMMA: u"am",
            POS: u''}
     ])
    nlp.tokenizer.add_special_case(u'No.',
    [
        {
            ORTH: u'No.',
            LEMMA: u'X',
            POS: u'X'}
     ])
    nlp.tokenizer.add_special_case(u'``',
    [
        {
            ORTH: u'``',
            LEMMA: u'`',
            POS: u'PUNCT'}
     ])
    nlp.tokenizer.add_special_case(u"'ve",
    [
        {
            ORTH: u"'ve",
            LEMMA: u'have',
            POS: u'ADJ'}
     ])
    
    final_list=[]
    i = 0
    for token_list in tokens_list:
        wordcounter = 0
        for token in token_list:
            doc = nlp(token_list[wordcounter])
            for token in doc:
                columns[i].insert(4, token.lemma_)
                columns[i].insert(5, token.pos_)
                columns[i].insert(6, token.tag_)
                columns[i].insert(7, dep_calculater(" ".join(token_list),nlp)[wordcounter])
                if i==0:
                    columns[i].insert(8, 'None')
                    columns[i].insert(9, 'None')
                    
                else:
                    columns[i].insert(8,token_list[wordcounter-1])   
                    prevtoken = nlp(columns[i-1][5])
                    columns[i].insert(9, prevtoken)
                final_list.append(columns[i])
                i+=1
            wordcounter +=1
                
    
    return(final_list)

def dumper(list_of_futures,outfile):
    file1 = open(outfile,"w")
    for i in list_of_futures:
        final_string = ""
        for z in i:
            final_string += str(z)
            final_string += ("\t")
        file1.writelines(final_string)
        file1.writelines("\n")
    file1.writelines("\n")
    file1.close()
                    
                
def main(argv=None):
    """ A list of commandline arguments are used to define the training file, input file and output file and then the whole process of classifying the data is guided
    
    :param argv: similar to an array, this is a parameter that is already predefined to 'None'. 
    
    :??:
    """
    #a very basic way for picking up commandline arguments
    if argv is None:
        argv = sys.argv
        
    #Note 1: argv[0] is the name of the python program if you run your program as: python program1.py arg1 arg2 arg3
    #Note 2: sys.argv is simple, but gets messy if you need it for anything else than basic scenarios with few arguments
    #you'll want to move to something better. e.g. argparse (easy to find online)
    
    
    #you can replace the values for these with paths to the appropriate files for now, e.g. by specifying values in argv
    #argv = ['mypython_program','','','']
    inputfile = argv[1]
    outputfile = argv[2]
    something= create_new_file(inputfile, outputfile)
    dumper(something,outputfile)
 
    
if __name__ == '__main__':
    argv = ['python','SEM-2012-SharedTask-CD-SCO-dev-simple.txt','SEM-2012-SharedTask-CD-SCO-dev-simple1.txt']
    main(argv)
    print("done")