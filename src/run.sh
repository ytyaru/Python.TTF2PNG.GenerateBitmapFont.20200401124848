#!/bin/bash
Run() {
	local FILE='x8y12pxTheStrongGamer'
	local TTF="${FILE}.ttf"
	local PNG="${FILE}.png"
	[ ! -f "$TTF" ] && wget http://www17.plala.or.jp/xxxxxxx/00ff/"$TTF"
	[ ! -f "$PNG" ] && python3 GenerateBitmapFont.py
}
Run
