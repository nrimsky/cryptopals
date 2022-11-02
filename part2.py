from part1 import ex3
from base64 import b64decode


def ex5(s, key):
    xored = ""
    for i, c in enumerate(s):
        xored += chr(ord(c) ^ ord(key[i % len(key)]))
    return xored.encode().hex()


def repeat_xor(s, key):
    xored = ""
    for i, c in enumerate(s):
        xored += chr(ord(c) ^ ord(key[i % len(key)]))
    return xored


def hamming(s1, s2):
    _s1 = s1.encode('utf8')
    _s2 = s2.encode('utf8')
    assert len(_s1) == len(_s2)
    dist = 0
    for bit1, bit2 in zip(_s1, _s2):
        diff = bit1 ^ bit2
        dist += sum([1 for bit in bin(diff) if bit == '1'])
    return dist


def find_best_keysize(text, start=1, stop=5, topn=2):
    res = []
    for keysize in range(start, stop):
        sample_indices = range(0, len(text) - keysize * 2, keysize * 2)
        distance = sum([hamming(text[i:i + keysize], text[i + keysize:i + 2 * keysize]) for i in sample_indices]) / len(sample_indices)
        normalised = distance / keysize
        res.append((keysize, normalised))
    res = sorted(res, key=lambda x: x[1])  # Sort by normalised hamming distance
    return [t[0] for t in res[:topn]]  # Return top n key sizes


def break_repeated_xor_with_keysize(text, keysize):
    blocks = [text[i: i + keysize] for i in range(0, (len(text) // keysize) * keysize, keysize)]
    transposed = ["".join([b[i] for b in blocks]) for i in range(keysize)]
    keys = [ex3(s.encode('utf-8').hex()) for s in transposed]
    full_key = "".join(keys)
    return full_key


def break_repeated_xor(text):
    keysizes = find_best_keysize(text, start=1, stop=30, topn=12)
    # print(f"Key sizes: {keysizes}")
    # print(f"Using top key size: {keysizes[0]}")
    key = break_repeated_xor_with_keysize(text, keysizes[0])
    # print(f"key: {key}")
    # print(f"decrypted: {repeat_xor(text, key)}")
    return repeat_xor(text, key)


def ex6(filename):
    with open(filename) as textfile:
        data = b64decode(textfile.read()).decode('utf8')
        return break_repeated_xor(data)

