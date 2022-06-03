from tokenizer import SvgTokenizer
from random import randrange
import string

alphabet_string_l = string.ascii_lowercase
alphabet_string_U = string.ascii_uppercase

alphabet_list_l = list(alphabet_string_l)
alphabet_list_U = list(alphabet_string_U)

alphabet_list = alphabet_list_U + alphabet_list_l

MAX_FONT_ID = 14
long_glyphs = "hbdfijlkt"

lower_glyphs = "gqpy"


def make_svg_text_v2(text, svgs, to):
    tokenizer = SvgTokenizer()
    cur_width = 10
    cur_blank = 20
    res = tokenizer.empty_svg_tensor()
    for i in range(len(text)):
        if text[i] == " ":
            cur_width = cur_width + cur_blank
            continue
        svg = svgs[i]
        if text[i].isupper():
            max_width, max_height = tokenizer.get_max_width(svg, scale=1)
            tokenizer.tranlsate(svg, cur_width, 0)
            cur_width = cur_width + max_width + 9
        else:
            if text[i] in lower_glyphs:
                max_width, max_height = tokenizer.get_max_width(svg, scale=1)
                tokenizer.tranlsate(svg, cur_width, 0)
            elif text[i] in long_glyphs:
                max_width, max_height = tokenizer.get_max_width(svg, scale=1)
                tokenizer.tranlsate(svg, cur_width, 0)
            else:
                max_width, max_height = tokenizer.get_max_width(svg, scale=1)
                tokenizer.tranlsate(svg, cur_width, 0)
            cur_width = cur_width + max_width + 9
        res = tokenizer.concat_svg_tensors(res, svg)
    tokenizer.saveSvg(res, filename=to)


def drawSvgTextTo(text, to, fontid=None, z=None):
    if fontid is None:
        fontid = randrange(MAX_FONT_ID)
    svgs = []
    tokenizer = SvgTokenizer()

    if fontid < 10:
        fontstr = "000" + str(fontid)
    elif fontid < 100:
        fontstr = "00" + str(fontid)
    elif fontid < 1000:
        fontstr = "0" + str(fontid)
    else:
        fontstr = str(fontid)

    for w in text:
        if w == " ":
            svgs.append(tokenizer.empty_svg_tensor())
            continue
        i = alphabet_list.index(w)

        if i < 10:
            path = 'results/%s/svgs/syn_0%d_00.svg' % (fontstr, i)

        else:
            path = 'results/%s/svgs/syn_%d_00.svg' % (fontstr, i)
        svg = tokenizer.parseSvg(path, normalize=False, norm_y=False)
        svgs.append(svg)

    make_svg_text_v2(text, svgs, to)


for i in range(600):
    try:
        drawSvgTextTo("Wordmark", "output1/{}.svg".format(i), fontid=i)
    except:
        continue
