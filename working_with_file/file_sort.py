import os
import shutil

file_categories = {'music': ['mp3', 'wav', 'ogg'],
                   'video': ['avi', 'mp4', 'mkv'],
                   'pictures': ['jpg', 'bmp', 'psd'],
                   'documents': ['doc', 'txt', 'rtf']}

def file_sort(path: str):
    for dir_name in file_categories:
        if not os.path.exists(os.path.join(path, dir_name)):
            os.mkdir(os.path.join(path, dir_name))
    count = 0
    for file in os.listdir(path):
        for targ_dir, file_ext in file_categories.items():
            if os.path.isfile(os.path.join(path, file)) and (file.rsplit('.', 1)[1] in file_ext):
                shutil.move(os.path.join(path, file), os.path.join(path, targ_dir, file))
                count += 1
    print(f'Операция завершена!\nБыло перемещено {count} файлов')

if __name__ == '__main__':
    file_sort('example')