from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os


def add_padding(data):
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data)
    return padded_data + padder.finalize()


def remove_padding(data):
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    return unpadder.update(data) + unpadder.finalize()


def get_key_size(option):
    # not working properly different modes offer key sizes,
    # TODO update key len combobox dependent on mode combobox content
    key_dic = {16: 0, 24: 1, 32: 2}
    print([size for size in algorithms.AES.key_sizes][key_dic[option]])
    return [size for size in algorithms.AES.key_sizes][key_dic[option]] // 8


def ecb_encrypt(data, key_size=32):
    key = os.urandom(get_key_size(key_size))
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    data = add_padding(data)

    ct = encryptor.update(data) + encryptor.finalize()

    return ct, key


def ecb_decrypt(ct, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    return remove_padding(padded_data)


def cbc_encrypt(data, key_size=3):
    key = os.urandom(get_key_size(key_size))
    iv = os.urandom(algorithms.AES.block_size // 8)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    data = add_padding(data)

    ct = encryptor.update(data) + encryptor.finalize()

    return ct, iv, key


def cbc_decrypt(ct, iv, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    return remove_padding(padded_data)


def ctr_encrypt(data, key_size=3):
    key = os.urandom(get_key_size(key_size))
    nonce = os.urandom(algorithms.AES.block_size // 8)
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    encryptor = cipher.encryptor()

    ct = encryptor.update(data) + encryptor.finalize()

    return ct, nonce, key


def ctr_decrypt(data, nonce, key):
    cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()


def add_header(file_localization, algorithm: str, mode: str):
    os.setxattr(file_localization, 'user.alg', bytes(algorithm.encode('ascii')))
    os.setxattr(file_localization, 'user.mode', bytes(mode.encode('ascii')))


def read_header(file_localization):
    return os.getxattr(file_localization, 'user.alg').decode('ascii'), os.getxattr(file_localization, 'user.mode').decode('ascii')


def encrypt(algorithm: str, mode: str, key_len: int, data):
    if algorithm == 'AES':
        if mode == 'ECB':
            return ecb_encrypt(data, key_len)
        elif mode == 'CBC':
            return cbc_encrypt(data, key_len)
        elif mode == 'CTR':
            return ctr_encrypt(data, key_len)
        else:
            print('Cannot resolve mode:', mode)
            return None
    else:
        print('Cannot resolve algorithm:', algorithm)
        return None

