import os
import sys
import chardet
import re


def to_eng(file):
    text_bytes = open(file, 'rb').read()
    # Decode & Turn to list
    code_type = chardet.detect(text_bytes)['encoding']
    if 'gb' in code_type.lower():
        code_type = 'gbk'
    content = text_bytes.decode(code_type.lower())
    content = content.split('\r\n')

    # Make new list only contain English
    content_eng = []
    pattern = ',{.*?N{'
    for line in content:
        if line[:8] == 'Dialogue':
            if 'N{' in line:
                del_text = re.search(pattern, line).group()[1:-1]
                line = line.replace(del_text, '')
                line = line.replace('说话人', 'speaker')
                # Change English Font
                line = line.replace('Tahoma', 'Monaco')
        content_eng.append(line)
    # write to .ass file
    new_file_name = file[:-4] + '.eng' + file[-4:]
    with open(new_file_name, 'w', encoding='utf-8') as new_ass_file:
        for line_eng in content_eng:
            new_ass_file.write(line_eng + '\n')


def explore(location):
    for root, dirs, files in os.walk(location):
        for file in files:
            path = os.path.join(root, file)
            to_eng(path)
    print('*************** All jobs done! ***************')


def main():
    path = ''
    for i in sys.argv[1:]:
        path += (i + ' ')
    path = path[:-1]
    print('*************** Working on path ' + path + '***************')
    if os.path.isfile(path):
        to_eng(path)
    elif os.path.isdir(path):
        explore(path)


if __name__ == "__main__":
    main()
