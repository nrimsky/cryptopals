from part1 import ex1, ex2, ex3, ex4


def test_ex1():
    s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    ans = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert ex1(s) == ans


def test_ex2():
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    ans = "746865206b696420646f6e277420706c6179"
    assert ex2(s1, s2) == ans


def test_ex3():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ans = "X"
    assert ex3(s) == ans


def test_ex4():
    filename = "data4.txt"
    ans = "5"
    assert ex4(filename) == ans
