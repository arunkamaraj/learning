try :
    # l = open("myfile1", "r")
    f = 20
    assert f == "10", "value is not matching"
# except (IOError,AssertionError) , e:
except IOError, e:
    print e

except AssertionError, a:
    print a


