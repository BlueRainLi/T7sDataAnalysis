# -*- coding:utf-8 -*-
import os
import json
import re
from collections import defaultdict

ignore_list = ['settings']


def testing(p_filename):
    with open(p_filename) as f:
        count, note = 0, False
        for line in f:
            matching = re.search(r"\((\'|\")(.+)(\'|\")\)\,", line)
            if matching:
                data = re.split(r'(?:\'|\"),(?:\'|\")', matching.group(2))
                lens = len(data)
                for i in range(lens):
                    title[lst[i]].append(data[i])
                count += 1
            elif not note:
                matching = re.search(r"(REPLACE|INSERT) INTO `(.+)` ?\((.+)\)", line)
                if matching:
                    title = defaultdict(list)
                    name = matching.group(2)
                    lst = re.split(r'[\`\,]+', matching.group(3))
                    del lst[len(lst) - 1]
                    del lst[0]
                    for item in lst:
                        title[item]
                    note = True
    print('Count:', count)
    with open(name + '.json', 'w') as f2:
        json.dump(title, f2)
        print('Finished')


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.json' and os.path.splitext(file)[0] not in ignore_list:
                os.remove(file_dir + '/' + file)
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.sql':
                print(file)
                testing(file_dir + file)


def main():
    file_name('/Users/lizhuoyu/Documents/Deconde Files/')  # 输入文件夹地址，会对文件夹下所有文件与文件夹操作）


if __name__ == "__main__":
    main()
