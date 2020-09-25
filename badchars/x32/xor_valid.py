def valid_xor(string, xor_value):
    output = ''
    badchars = 'xga.'
    for char in string:
        output += chr(ord(char) ^ xor_value)
    for char in badchars:
        if char in output:
            return False
    return True

target = "flag.txt"
for xor in xrange(10):
    if valid_xor(target, xor):
        print('Valid: {}'.format(hex(xor)))
