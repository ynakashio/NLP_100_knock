#coding:utf-8

# 第1章: 準備運動

import string
import sys
from nltk.tokenize import word_tokenize
# from nltk import tokenize
# sys.setdefaultencoding('utf-8')


def task_00():

	# 00. 文字列の逆順
	# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

	input_string = "stressed"
	reversed_string = input_string[::-1]
	print "設問00"
	print "次の文字列を逆順にすると:",input_string,"->",reversed_string

	return

def task_01():

	# 01. 「パタトクカシーー」
	# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

	input_string = "パタトクカシーー"
	output_string = input_string[1]+input_string[3]+input_string[5]+input_string[7]

	# print input_string[1]
	# print input_string[3]
	# print input_string[5]
	# print input_string[7]

	print output_string

	return


def task_02():

	# 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
	# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ.

	input_1_string = "パトカー"
	input_2_string = "タクシー"

	return


def task_03():

	# 03. 円周率
	# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

	input_string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
	tokenized_list = word_tokenize(input_string)

	tmp=[]
	for i in tokenized_list:
		tmp.append(len(i))
	print tmp

	return


def task_04():

	# 04. 元素記号
	# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．


	return


def task_05():

	# 05. n-gram
	# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

	def n_gram(n,input_string):

		


		return




	return


if __name__ == '__main__':
	task_00()
	task_01()
	task_02()
	task_03()
	task_04()
	task_05()


