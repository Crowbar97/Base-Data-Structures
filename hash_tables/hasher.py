def is_seq(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True

# TODO: improve
def hash_string(string, bound, seed):
    str_hash = 0
    for i, char in enumerate(string, 1):
        h = ord(char) * seed ** i
        str_hash += h
    return str_hash % bound

# TODO: make right way
def hash_obj(obj, bound, seed=123):
    if not isinstance(obj, str):
        if not is_seq(obj):
            obj = [ obj ]
        obj = ''.join(map(str, obj))
    return hash_string(obj, bound, seed)