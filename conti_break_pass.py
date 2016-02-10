import sys
import argparse


def example(a):
    args = argparse.ArgumentParser("This programe illustrate the conti and break and pass")
    args.add_argument("-C", dest="conti", default=None)
    args.add_argument("-B", dest="breaking", default=None)
    args.add_argument("-P", dest="passing", default=None)
    return args.parse_args()


def control_statement(data):
    if data.conti == "continue":
        for i in "Example":
            if i == "a":
                print "missing A"
                continue
            print i

    if data.breaking == "break":
        for i in "Example":
            if i == "a":
                print "Breaking the controls here "
                break
            print i

    if data.passing == "pass":
        for i in "Example":
            if i == "a":
                pass
                print "passing the variable"
            print i


if __name__ == "__main__":
    data = example(sys.argv[1:])
    control_statement(data)
