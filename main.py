from crypto_functions import *


def main():
    data = b'super duper hiper top secret message!'

    file_loc = '/home/buzeqq/Dokumenty/test.txt'
    add_header(file_loc, 'AES', 'ECB')
    algo, mode = read_header(file_loc)
    print(algo, mode)
    # print('ECB:')
    # ct, key = ecb_encrypt(data)
    # print(f'key: {key}\n'
    #       f'ciphertext: {ct}')
    # data = ecb_decrypt(ct, key)
    # print(f'data: {data}\n')
    #
    # print('CBC:')
    # ct, iv, key = cbc_encrypt(data)
    # print(f'key: {key}\n'
    #       f'initialization vector: {iv}\n'
    #       f'ciphertext: {ct}')
    # data = cbc_decrypt(ct, iv, key)
    # print(f'data: {data}\n')
    #
    # print('CTR:')
    # ct, nonce, key = ctr_encrypt(data)
    # print(f'key: {key}\n'
    #       f'nonce: {nonce}\n'
    #       f'ciphertext: {ct}')
    # data = ctr_decrypt(ct, nonce, key)
    # print(f'data: {data}\n')


if __name__ == '__main__':
    main()
