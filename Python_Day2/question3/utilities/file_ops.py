def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def write_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

def search_in_file(filename, keyword):
    with open(filename, 'r') as f:
        return keyword in f.read()
