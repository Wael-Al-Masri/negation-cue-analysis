import sys

def check_neg(inputfile):
    """ A function to check in the predicted and gold labels if the negation labels match, and if they do not, print the sentence number, token number and token.
    
   :param inputfile: the filepath to the input file
   
   :prints: the incorrectly classified tokens with its sentence number and token number when run from the command line
    
    """
    print('incorrectly predicted token')
    with open(inputfile, 'r+', encoding='utf8') as infile:
        for line in infile:
            components = line.rstrip('\n').split('\t')
            if components[10] == 'B-NEG' and components[12] != 'B-NEG':
                print(components[1], components[2], components[3])
            if components[10] == 'I-NEG' and components[12] != 'I-NEG':
                print(components[1], components[2], components[3])

def main(argv=None):
    """ A list of commandline arguments are used to define the input file and the process of getting the incorrectly predicted tokens.
    
    :param argv: similar to an array, this is a parameter that is already predefined to 'None'. 
    
    :prints: the incorrectly classified tokens with its sentence number and token number when run from the command line
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
    check_neg(inputfile)
    
if __name__ == '__main__':
    argv = ['python', "Data\ final.SVM.txt"]
    main(argv)