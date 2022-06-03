from tokenizer import SvgTokenizer

tokenizer = SvgTokenizer()
tensor = tokenizer.parseSvg("gt_00.svg", normalize=False)
tokenizer.saveSvg(tensor, 1)