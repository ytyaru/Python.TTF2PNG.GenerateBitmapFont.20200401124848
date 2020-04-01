#!/usr/bin/env python3
# coding: utf8
from PIL import Image, ImageFont, ImageDraw
import string, os
        
class BitmapFontGenerator:
    def __init__(self, fontfile='x8y12pxTheStrongGamer.ttf', w=8, h=12):
        self.__fontfile = os.path.abspath(fontfile)
        self.__letter_size = (w, h)
        self.__font = Font(self.__fontfile, self.__letter_size, self.Letters)
        self.__font.img.save(self.PngFile)
    @property
    def Letters(self):
        ascii_chars = string.punctuation + string.digits + string.ascii_letters
        hira = "".join(chr(c) for c in range(ord('ぁ'), ord('ゔ')+1))+"ー"
        kata = "".join(chr(c) for c in range(ord('ァ'), ord('ヶ')+1))+"ー"
# hankata = "".join(chr(c) for c in range(ord('ｧ')-6, ord('ﾞ')+2))
        return ascii_chars + hira + kata + "、。「」"
    @property
    def FontFile(self): return self.__fontfile
    @property
    def LetterSize(self): return self.__letter_size
    @property
    def Font(self): return self.__font
    @property
    def PngFile(self):
        return os.path.join(os.path.dirname(self.FontFile), os.path.splitext(os.path.basename(self.FontFile))[0] + '.png')

class Font:
    def __init__(self, file, size, letters):
        import numpy as np
        self.file = file
        self.size = size
        self.letters = letters
        px_w, px_h = size
        # pt_w, pt_h = (int(n * 0.75) for n in meta['size']) # 96 dpi
        font = ImageFont.truetype(file, size=px_h) # it must be pt_h, but px_h brings better result
        img = Image.new('1', size=(self.PyxelImgW, self.PyxelImgH))
        draw = ImageDraw.Draw(img)
        coords = {}
        x, y = 0, 0
        for c in letters:
            if x + px_w > self.PyxelImgW:
                x = 0
                y += px_h
            draw.text((x, y), c, font=font, fill=1)
            coords[c] = (x, y)
            x += px_w
        self.coords = coords
        self.img = img
        self.data = np.array(img.getdata()).reshape(self.PyxelImgW, self.PyxelImgH)
    @property
    def PyxelImgW(self): return 256
    @property
    def PyxelImgH(self): return 256

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='ビットマップフォント作成（.ttfから.pngを出力）', 
        add_help=False, 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--fontfile', default='x8y12pxTheStrongGamer.ttf', help='ttf形式ファイルパス')
    parser.add_argument('-w', '--width', type=int, default=8, help='png出力時における1字あたりのピクセル幅')
    parser.add_argument('-h', '--height', type=int, default=12, help='png出力時における1字あたりのピクセル高さ')
    parser.add_argument('--help', action='help', help='ヘルプ表示する')
    args = parser.parse_args()
    BitmapFontGenerator(args.fontfile, args.width, args.height)

