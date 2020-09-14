def is_seq(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True

# TODO: improve
def hash_string(string, size=100):
    str_hash = 0
    k = 123
    for i, char in enumerate(string):
        str_hash += ord(char) * k ** i
    return str_hash % size

# TODO: make right way
def hash_obj(obj, size):
    if not isinstance(obj, str):
        if not is_seq(obj):
            obj = [ obj ]
        obj = ''.join(map(str, obj))
    return hash_string(obj, size)