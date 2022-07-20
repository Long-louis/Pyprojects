# -- coding:utf-8 -- #

"""
Project:PyProject
File:ascii.py.py
Author:halongbay
Date:2022/7/19 23:35

"""

from PIL import Image
import argparse

# 使用argparse设置命令行参数

parser = argparse.ArgumentParser()
# type是要传入的参数的数据类型  help是该参数的提示信息
parser.add_argument('file', help='输入图片的路径')
parser.add_argument("-w", '--width', type=int, default=80, help='输出字符串的宽度')
parser.add_argument('--height', type=int, default=80, help='输出字符串的高度')
parser.add_argument("-o", '--output', help='输出文件路径')

args = parser.parse_args()

INPUT = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

# 设置字符串所使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    # 获取字符集长度
    length = len(ascii_char)
    # 转换为灰度值
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(INPUT)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
    # *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

    text = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            text += get_char(*im.getpixel((j, i)))

        text += '\n'

    print(text)

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(text)
    else:
        with open("output.txt", 'w') as f:
            f.write(text)
