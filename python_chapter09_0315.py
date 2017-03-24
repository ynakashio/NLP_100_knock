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

	input_name = './sample.txt'
	# file_name = "./enwiki-20150112-400-r100-10576.txt"
	f = codecs.open(input_name, "r","utf-8")
	wiki_data = str(f.read()).decode("utf-8")
	f.close

	return wiki_data


def task_80(wiki_data):

	# これを参考にした
	# => http://qiita.com/segavvy/items/ea485e66dd96eee891da

	output_name = './80_sample.txt'

	word_list=[]
	for chunk in wiki_data.split(' '):
		token = chunk.strip('.,!?;:()[]\'"').strip()
		if len(token) > 0:
			word_list.append(str(token))

	output_str = ""
	for word in word_list:
		output_str = output_str + " " + word
	print output_str
	f = open(output_name,"w")
	f.write(output_str)
	f.close

	# 以下は正規表現でやろうとして失敗。誰か教えてくださいw
	# for tokenized_word in tokenize.word_tokenize(wiki_data):
	# 	word_list.append(re.sub(re.compile(".,!?;:()\[]"), "", str(tokenized_word)))

	return


def task_81():


	return



if __name__ == '__main__':
	wiki_data = data_loader()
	task_80(wiki_data)
