from random import randint as ri, choice as ch, randbytes as rb
from string import ascii_lowercase #импорт английских букв в нижнем регистре
import os

def gen_file_bytes(name_dir: str, extention: list[str], min_len_name: int = 6, max_len_name: int = 30, min_bytes: int = 256, max_bytes: int = 4096, quantity: int = 42):
    if not os.path.exists(name_dir):
        os.mkdir(name_dir)
    for _ in range(quantity):
        file_name = ''
        for _ in range(ri(min_len_name, max_len_name)):
            file_name += ch(ascii_lowercase)
        ext = ch(extention)
        path = os.path.join(name_dir, file_name + '.' + ext)
        while True:
            if os.path.exists(path):
                file_name += '_1'
                path = os.path.join(name_dir, file_name + '.' + ext)
            else:
                break
        with open(path, 'wb') as file:
            file.write(rb(ri(min_bytes, max_bytes)))




if __name__ == '__main__':
    gen_file_bytes(name_dir = 'example',
               extention = ['txt', 'jpg', 'mp3', 'doc', 'exe', 'csv', 'avi', 'wav', 'rtf', 'mp4', 'mkv'],
               quantity=100)