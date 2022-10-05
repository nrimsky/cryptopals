from base64 import b64encode
from constants import LETTER_FREQUENCIES
from collections import Counter


def hex_to_b64(s):
    s_bytes = bytes.fromhex(s)
    b64 = b64encode(s_bytes)
    s_b64 = b64.decode()
    return s_b64


def xor(s1, s2):
    s1_bytes = bytes.fromhex(s1)
    s2_bytes = bytes.fromhex(s2)
    xor_byes = bytes([a ^ b for a, b in zip(s1_bytes, s2_bytes)])
    return xor_byes.hex()


def char_xor(s1, char):
    s1_bytes = bytes.fromhex(s1)
    char_bytes = bytes.fromhex(char)
    xor_byes = bytes([a ^ char_bytes[0] for a in s1_bytes])
    try:
        return xor_byes.decode()
    except UnicodeDecodeError:
        return ""


def ex1(s):
    return hex_to_b64(s)


def ex2(s1, s2):
    return xor(s1, s2)


def hex_str_to_binary(s):
    return bin(int(s, base=16))


def score_result(s):
    if " " not in s:
        return 0
    _s = s.upper().replace(" ", "")
    c = Counter(_s)
    p = {ch: (freq * 100) / len(_s) for ch, freq in c.items()}
    tot = 0
    for k in p.keys():
        if k in LETTER_FREQUENCIES:
            tot += p[k] * LETTER_FREQUENCIES[k]
    return tot / len(_s)


def ex3(s, return_score=False):
    maxi = 0
    letter = 'A'
    decoded = ''
    for _i in range(0, 128):
        l = chr(_i)
        xored = char_xor(s, l.upper().encode('utf-8').hex())
        res = score_result(xored)
        if res > maxi:
            maxi = res
            letter = l
            decoded = xored
    if return_score:
        return letter, maxi, decoded
    return letter


def ex4(filename):
    with open(filename, "r") as txtfile:
        lines = txtfile.readlines()
    highest = 0
    line = ""
    xor_letter = ""
    for l in lines:
        l = l.strip()
        letter, maxi, decoded = ex3(l, True)
        if maxi > highest:
            highest = maxi
            line = decoded
            xor_letter = letter
    print(f"Most likely candidate is '{line.strip()}'")
    print(f"Which scored {highest}")
    print(f"And was XORed with the letter '{xor_letter}'")
    return xor_letter


if __name__ == '__main__':
    ex4("data4.txt")
