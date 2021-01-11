import sys
import spacy
def list_of_tokens(inputfile):
    """
    Function that extracts all tokens from a given file and returns them as a list
    
    :param file: path to file
    :type file: string
    
    :return tokens: list of tokens
    """
    tokens_list = []
    with open(inputfile, 'r+', encoding = 'utf8') as infile:
        for line in infile:
            if len(line) == 1:
                continue
            else:
                components = line.rstrip('\n').split()
                tokens_list.append(components[3]) 
    return tokens_list

def create_new_file(inputfile, outputfile):
    tokens_list = list_of_tokens(inputfile)
    outfile = open(outputfile, 'w')
    nlp = spacy.load("en_core_web_sm")
    headers = 'Chapter', 'SentNumber', 'TNumber', 'Token', 'Lemma', 'POS', 'Chunk', 'DepREL', 'PToken','PTokenPOS','Negation'
    with open(inputfile,'r') as infile:
        i=0
        firstline = infile.readline()
        infile.seek(0,0)
        outfile.write('\t'.join(headers) + '\n')
        for line in infile:
            if len(line) == 1:
                continue
            else:
                components = line.rstrip('\n').split('\t')
                doc = nlp(components[3])
                for token in doc:
                    components.insert(4, token.lemma_)
                    components.insert(5, token.pos_)
                    components.insert(6, token.tag_)
                    components.insert(7, token.dep_)
                    if i==0:
                        components.insert(8, 'None')
                        prevtoken = nlp(components[8])
                        for token in prevtoken:
                            components.insert(9, token.pos_)
                    else: 
                        components.insert(8, tokens_list[i-1])
                        prevtoken = nlp(components[8])
                        for token in prevtoken:
                            components.insert(9, token.pos_)
                    i+=1
                    file = '\t'.join(components)
                    outfile.write(file+ '\n')
                    
                
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
    create_new_file(inputfile, outputfile)
    
if __name__ == '__main__':
    main()

