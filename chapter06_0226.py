#coding:utf-8

import csv
import nltk
import pandas as pd
import numpy as np
import re

def data_loader():

	f = open("./nlp.txt","rb")
	nlp_data = f.read()
	print nlp_data

	return nlp_data


def task_50(nlp_data):

	# 50. 文区切り
	# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

	




	return



if __name__ == '__main__':
	nlp_data = data_loader()