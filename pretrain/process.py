__shop__ = 'AINLP'
__link__ = 'https://item.taobao.com/item.htm?id=660447713149'
__date__ =  2022 / 4 / 24

import os


def process(path):
    outf = open('train.txt', 'w', encoding='utf8')
    all_lines = {}
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            print(f'process file: {name}')
            try:
                with open(os.path.join(root, name), 'r', encoding='utf8') as f:
                    lines = f.readlines()
            except:
                with open(os.path.join(root, name), 'r', encoding='gb18030') as f:
                    lines = f.readlines()
            for idx, line in enumerate(lines):
                line = line.strip()
                if not line:
                    continue
                if line not in all_lines:
                    all_lines[line] = 0
                    outf.write(f'{line}\n')
    outf.close()


if __name__ == '__main__':
    process('data')
