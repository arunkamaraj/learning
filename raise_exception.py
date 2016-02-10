class Error(Exception):
    pass

class TooSmallValue(Error):
    pass

class TooBigValue(Error):
    pass

def checkandraise(no):

    try:
        if no > 10:
            raise TooBigValue
        elif no < 10:
            raise TooSmallValue

    except TooSmallValue:
        print "Value is too small"

    except TooBigValue:
        print "Value is too big"

    else:
        print "Give the no"


checkandraise(20)
checkandraise(9)
checkandraise("arun")
