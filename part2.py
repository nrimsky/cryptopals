def ex5(s, key):
    xored = ""
    for i, c in enumerate(s):
        xored += chr(ord(c) ^ ord(key[i % len(key)]))
    return xored.encode().hex()


def hamming(s1, s2):
    n = 0
    # For each character...
    for c1, c2 in zip(s1, s2):
        # Convert to strings of 1 and 0
        b1 = str(bin(ord(c1)))[2:]
        b2 = str(bin(ord(c2)))[2:]
        # Zero pad the bit strings so that they are equal length
        if len(b1) < len(b2):
            b1 = "".join(["0" for _ in range(len(b2) - len(b1))]) + b1
        else:
            b2 = "".join(["0" for _ in range(len(b1) - len(b2))]) + b2
        # Count number of differing bits
        for _b1, _b2 in zip(b1, b2):
            if _b1 != _b2:
                n += 1
    return n

