# -*- coding:utf-8 -*-
import os
import sys
import chardet
import char

def convert(filename):
    if filename[-4:] == '.ass':
        print("convert " + filename)
        bytes_c = open(filename, 'rb').read()
        code_type = chardet.detect(bytes_c)['encoding']
        if 'gb' in code_type.lower():
            code_type = 'gbk'
        content = bytes_c.decode(code_type.lower())
        open(filename, 'w', encoding='utf-8').write(content)
        print('Done')
    else:
        pass


def explore(d):
    for root, dirs, files in os.walk(d):
        for file in files:
            path = os.path.join(root, file)
            convert(path)
    print('*************** All jobs done! ***************')


def main():
    # print(sys.argv[1:])
    # print(type(sys.argv[1:]))
    # print(len(sys.argv[1:]))
    path = ''
    for i in sys.argv[1:]:
        path += (i + ' ')
    path = path[:-1]
    print('*************** Working on path ' + path + '***************')
    # print(os.path.isfile(path))
    # print(os.path.isdir(path))
    if os.path.isfile(path):
        convert(path)
    elif os.path.isdir(path):
        explore(path)


if __name__ == "__main__":
    main()
