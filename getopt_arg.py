import sys
import getopt


def parsing(arguments):
    first_input = ''
    second_input = ''
    Other_argument = ''
    try:
        opt, arg = getopt.getopt(arguments, "hi:o:", ['ifile=', "ofile="])
    except getopt.GetoptError:
        print "thappu"

    for option, args in opt:
        if option == "-i":
            first_input = args
        elif option == "-o":
            second_input = args
        elif option == "-h":
            print "wrong"

    Other_argument = arg

    print "first",first_input
    print "second", second_input
    print "others",Other_argument

if __name__ == "__main__":
    parsing(sys.argv[1:])
