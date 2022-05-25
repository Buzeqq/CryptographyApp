import os
import random
import sys


def main():
    if len(sys.argv) < 2:
        print('Please specify ciphertext path!')
        return

    path = sys.argv[1]
    output_extension = os.path.splitext(path)[1]
    print(os.path.splitext(path))
    with open(path, 'rb') as ciphertext, \
            open(os.path.dirname(path) + "/new_ciphertext" + output_extension, 'wb') as new_ciphertext:
        ciphertext = ciphertext.read()
        print('Old ciphertext:', ciphertext, len(ciphertext))
        new_ciphertext_bytes = []
        for byte in ciphertext:
            if random.random() < 0.3:
                byte = byte ^ int.from_bytes(os.urandom(1), 'big')
            new_ciphertext_bytes.append(byte)
        new_ciphertext_bytes = bytes(new_ciphertext_bytes)
        print('New ciphertext', new_ciphertext_bytes, len(ciphertext))
        new_ciphertext.write(new_ciphertext_bytes)


if __name__ == '__main__':
    main()
