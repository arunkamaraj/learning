import re
str = "this is regular expression examples"
pattern = "this"

str_new = "arun this for arun statisfaction , arun trying something to learn"

def match_example():
    match = re.match(pattern, str)
    print match
    pass


def compile_expression():
    regex = [re.compile(i) for i in ["this", "that"]]
    print regex
    for j in regex:
        if j.search(str):
            print "found with ",j.pattern
        else:
            print "No"

def findall_find():

    find_data = re.findall("arun", str_new)
    print find_data
    finditer_data = re.finditer("arun", str_new)
    for i in finditer_data:
        print i

def sample():
    str = "abbaaabbbbaaaaa"
    ptn0 = 'a.*b'
    ptn1 = 'a.*?b'
    data0 = re.findall(ptn0, str)
    data1 = re.findall(ptn1, str)
    print "data0 : ", data0
    print "data1 : ", data1

def fucked():
    str = "'This is some text  -- with punctuation.'"
    ptn = r"\Bt\B"
    data = re.findall(ptn, str)
    print data

def search_with_pos():
    str = "This is some text -- with punctuation."
    ptn =r"\b\w*is"
    com = re.compile(ptn)
    pos = 0
    while True:
        match = com.search(str, pos)
        if not match:
            break
        print match.start(), ":", match.end(), match.group()

        # print match.group()
        pos = match.end()

def grouping():
    str = "arun-k@gmail.com, kamaraj_a@gmail.com"
    ptn = r"(?P<Name>[\w._-]*)@(?P<Domain>[\w._-]*)"
    comp =re.compile(ptn)
    data = comp.search(str)
    group1 = data.group(1)
    group2 = data.group(2)
    #
    print group1
    print group2
    print data.groupdict()


def alternate():
    str = "abbaaabbbbaaaaa"
    # ptn = r'a((a+)|(b+))' # important is | symbol
    ptn = r'a((a+)|(b+))' # important is | symbol
    # data = re.search(ptn, str)
    data = re.findall(ptn, str)
    print data


if __name__ == "__main__":
    # compile_expression()
    # findall_find()
    # sample()
    # fucked()
    # search_with_pos()
    # grouping()
    alternate()