def append_example():
    li = ['a', 'b', 'mpilgrim', 'z', 'example']

    li.append("new")
    print li

def insert_example():
    li = ['a', 'b', 'mpilgrim', 'z', 'example']

    li.insert(2, "new")
    print li

def extend_example():
    li = ['a', 'b', 'mpilgrim', 'z', 'example']

    li.extend(["two", "elements"])
    print li
if __name__ == "__main__":
    append_example()
    insert_example()
    extend_example()
