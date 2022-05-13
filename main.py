from crypto_functions import *


def main():
    file = open('/home/buzeqq/Dokumenty/test.txt', 'r+b')
    data = bytearray(file.read())
    file.close()

    print('ECB:')
    output = encrypt('AES', 'ECB', 32, data)
    print('key:', output['key'])
    print('ciphertext:', output['ciphertext'])
    data = decrypt('AES', 'ECB', output['key'], output['additional'], output['ciphertext'])
    print(f'data: {data}\n')

    print('CBC:')
    output = encrypt('AES', 'CBC', 32, data)
    print('key:', output['key'])
    print('initialization vector:', output['additional'])
    print('ciphertext:', output['ciphertext'])
    data = decrypt('AES', 'CBC', output['key'], output['additional'], output['ciphertext'])
    print(f'data: {data}\n')

    print('CTR:')
    output = encrypt('AES', 'CTR', 32, data)
    print('key:', output['key'])
    print('nonce:', output['additional'])
    print('ciphertext:', output['ciphertext'])
    data = decrypt('AES', 'CTR', output['key'], output['additional'], output['ciphertext'])
    print(f'data: {data}\n')

if __name__ == '__main__':
    main()
