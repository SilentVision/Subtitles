import os
import shutil


new_path = 'D:\\Eric\\Google Drive (Eric)\\Subtitles\\'

def move_files(old, aa, bb):
    new = new_path + aa + '.' + bb
    shutil.copyfile(old, new)


for root, dirs, files in os.walk('E:\Friends'):
    for file in files:
        if file[-4:] == '.ass':
            path = os.path.join(root, file)
            aa,bb = file.split('.')
            move_files(path, aa, bb)
