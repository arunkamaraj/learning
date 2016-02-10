import sys
import argparse

def arg_training(a):
    pass
    args = argparse.ArgumentParser(description="this is example programe")
    args.add_argument("-name", default="AK",dest= "name" )
    args.add_argument("-appaname", default="KJ", dest = "appaname")
    data = args.parse_args()

    print data.name
    print data.appaname

if __name__== "__main__":
    a = sys.argv[1:]
    data = arg_training(a)
