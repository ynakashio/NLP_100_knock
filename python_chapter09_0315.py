#coding:utf-8

import csv
import codecs
import numpy as np
from nltk import tokenize
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
import pandas as pd


# ひとまず早いのでnltkで実装してみる。
# 余裕があれば Stanford coreNLPを使ってみるということで。。


def data_loader():

	file_name = "./sample.txt"
	# file_name = "./enwiki-20150112-400-r100-10576.txt"
	f = codecs.open(file_name, "r","utf-8")
	wiki_data = str(f.read()).decode("utf-8")
	f.close

	return wiki_data


def task_80(wiki_data):

	tmp_tokenized_data = tokenize.word_tokenize(wiki_data)

	for word in tmp_tokenized_data:
		print re.sub(re.compile('.,!?;:()[]'), '', word)
		

	return


def task_82():


	return



if __name__ == '__main__':
	wiki_data = data_loader()
	task_80(wiki_data)
