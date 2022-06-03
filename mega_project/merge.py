import svgutils.transform as sg
import sys
import re
import string
import cairosvg

path_list = []

alphabet_string_l = string.ascii_lowercase
alphabet_string_U = string.ascii_uppercase

alphabet_list_l = list(alphabet_string_l)
alphabet_list_U = list(alphabet_string_U)

alphabet_list = alphabet_list_U + alphabet_list_l

word = sys.argv[1]
font = "0004"
capital = []
for letter in word:
    i = alphabet_list.index(letter)
    if i < 10:
        path = 'results/%s/svgs/syn_0%d_18.svg' % (font, i)

    else:
        path = 'results/%s/svgs/syn_%d_18.svg' % (
            font, i)

    if i < 26:
        capital.append("c")
    else:
        capital.append("s")

    path_list.append(path)

newsvg = sg.SVGFigure(100, 100)
newsvg = sg.SVGFigure(1, 1)
i = 0
for path in path_list:
    logo = sg.fromfile(path)
    root = logo.getroot()
    root.moveto(i, 0)
    newsvg.append([root])
    index = path_list.index(path)
    if capital[index] == "s":
        i = i + 12
    elif capital[index] == "c":
        i = i + 16

newsvg.save('%s%s.svg' % (word, font))