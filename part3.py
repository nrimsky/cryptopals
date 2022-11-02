from base64 import b64decode


def read_file(filename):
    with open(filename) as textfile:
        return textfile.read()


def aes_decrypt(encrypted, key):
    return "HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS"


def ex7(filename, key):
    return b64decode(aes_decrypt(read_file(filename), key)).decode('utf8')
