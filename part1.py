from base64 import b64encode
from score_function import get_english_score


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


def ex3(s, return_score=False):
    res = []
    for _i in range(0, 256):
        l = chr(_i)
        decoded = char_xor(s, l.encode('utf-8').hex())
        score = get_english_score(decoded)
        res.append((l, score, decoded))
    res = sorted(res, key=lambda x: x[1], reverse=True)
    if return_score:
        return res[0]
    return res[0][0]


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
