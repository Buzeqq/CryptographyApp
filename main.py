import os
import random
import sys


def main():
    if len(sys.argv) < 2:
        print('Please specify key path!')
        return

    path = sys.argv[1]
    with open(path, 'rb') as key, open(os.path.dirname(path) + "/new_key.bin", 'wb') as new_key:
        key = key.read()
        print(key, len(key))
        new_key_bytes = []
        for byte in key:
            if random.random() < 0.3:
                byte = byte ^ int.from_bytes(os.urandom(1), 'big')
            new_key_bytes.append(byte)
        new_key_bytes = bytes(new_key_bytes)
        print(new_key_bytes, len(key))
        new_key.write(new_key_bytes)


if __name__ == '__main__':
    main()
