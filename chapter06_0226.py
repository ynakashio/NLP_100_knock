#coding:utf-8

import codecs
import corenlp
import csv
import nltk
import pandas as pd
import numpy as np
import re
import subprocess
from stemming.porter2 import stem
import xml.etree.ElementTree as ET


# (参考) https://m-note.github.io/100knock/100knock_Chap%206.html


def data_loader():

	f = open("./nlp.txt","rb")
	nlp_data = f.read()
	# print nlp_data

	return nlp_data


def task_50(nlp_data):

	# 50. 文区切り
	# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

	pattern = r'\.\s[A-Z]|\;\s[A-Z]|\:\s[A-Z]|\?\s[A-Z]|\!\s[A-Z]'
	sentences = re.finditer(pattern, nlp_data)

	index_list=[]
	sentence_list = []
	for i,so in enumerate(sentences):
		if i == 0:
			_0_index = so.end()-1
			sentence_list.extend([nlp_data[:_0_index].rstrip()])

			print nlp_data[:_0_index].rstrip()
			index_list.extend([_0_index])

		else:
			start_index = index_list[i-1]
			end_index = so.end()-1
			sentence_list.extend([nlp_data[start_index:end_index]])

			print nlp_data[start_index:end_index]
			index_list.extend([end_index])

	"""
	* パターンの定義の仕方
	pattern = r'\.\s[A-Z]|\;\s[A-Z]|\:\s[A-Z]|\?\s[A-Z]|\!\s[A-Z]'

	(参照) http://kenichia.hatenablog.com/entry/2016/02/15/174813

	* 正規表現の意味
	\ => ここから始まり
	\s => スペース(空白文字)
	[A-Z] => 英大文字
	| => または

	つまり、".などの記号+スペース+英大文字"の組み合わせをorで4種類作っているということ
	若干これは冗長な気がする。記号の部分をひとつにまとめられたらきっともっとすっきりするはず。
	"""

	"""
	* 正規表現で文字列を探すとき
	(参照)http://qiita.com/wanwanland/items/ce272419dde2f95cdabc
		- re.split()は、patternを削除して分割する
		- re.match/search/findall/finditer とかの使い分けが大事
	"""

	return sentence_list


def task_51(sentence_list):

	"""
	51. 単語の切り出し
	空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
	"""

	word_list = []
	for sentence in sentence_list:
		for word in re.split(" ", sentence):
			if word[:-1] == ".":
				# print word,"\n"

				eos_word = word+"\n"
				word_list.extend([eos_word])
			else:
				# print word
				word_list.extend([word])

	return word_list


def task_52(word_list):

	"""
	52. ステミング
	51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
	(参照) https://pypi.python.org/pypi/stemming/1.0
	ダウンロードして、"python setup.py install"を叩く！！
	"""
	for word in word_list:
		print word,"\t",stem(word)

	return


def task_53(nlp_data):

	"""
	mecabなどと同様にanaconda以下のpipでインストールする。以下のコマンドでok。
	.pyenv/versions/anaconda2-2.5.0/bin/pip install corenlp-python

	(参照) http://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5
		corenlpのダウンロードするversionが古いと、エラー等で動かないことがある
	"""

	"""
	xmlの作成には、以下のコマンドでok。
	java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref -file input.txt
	-file "input.txt"の部分を、インプットするファイル名に変える。
	"""

	xml_file_name = "./nlp.txt.xml"
	root = ET.parse(xml_file_name)
	for word in root.iter('word'):
		print word.text

	"""
	 "subprocess" のモジュールを使うことで、コマンドラインでの作業を再現できるらしい。
	 (参照) http://qiita.com/segavvy/items/ab6bb2b994aac061f51f

	corenlp_dir = "/Users/yuko/stanford-corenlp-full-2015-04-20/"
	parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

	input_file_name = "sample_nlp.txt"
	parsed_file_name = "parsed_nlp_data.xml"
	f = open(parsed_file_name, "wb")

	subprocess.check_output(
			'java -cp "/Users/yuko/stanford-corenlp-full-2015-04-20/*"'
			' -Xmx2g'
			' edu.stanford.nlp.pipeline.StanfordCoreNLP'
			' -annotators tokenize,ssplit,pos,lemma,ner,parse,dcoref'
			' -file ' + input_file_name + ' 2>parse.out',
			shell=True,     # shellで実行
			check=True      # エラーチェックあり
			)

	ただし、subprocess.run()はpython3系列からの関数
	"""

	return

def xml_loader():

	# 53で書き出したxmlファイルをロードする

	xml_file_name = "./nlp.txt.xml"
	root = ET.parse(xml_file_name)

	return root



def task_54(root):

	"""
	54. 品詞タグ付け
	Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
	(参照) http://qiita.com/segavvy/items/4d55805352089332828e
	"""

	for token in root.iter("token"):
		print token.findtext("word"),"\t",token.findtext("lemma"),"\t",token.findtext("POS")

	return root


def task_55(root):

	"""
	55. 固有表現抽出
	入力文中の人名をすべて抜き出せ．
	(参考) http://qiita.com/segavvy/items/32b3a35825ec32586f33
	"""
	"""
	PERのタグに含まれているタグは以下の8種類。
	{'DATE', 'DURATION', 'LOCATION', 'MISC', 'NUMBER', 'ORDINAL', 'ORGANIZATION', 'PERSON'}
	このうち固有表現に当たるのは、"ORGANIZATION"と"PERSON"なので、今回はこの2つを抜き出す。
	ところで、"MISC"ってなんですかね！調べたけどわからなかったです。

	※ NER = Named Entity Recognition
	"""
	nerList=[]
	for token in root.iter("token"):
		if token.findtext("NER") == "ORGANIZATION" or token.findtext("NER") == "PERSON":
			nerList.extend([token.findtext("word")])
	print set(nerList)
	# この結果だとなんかandとかofが入っている・・・・

	return


def task_56(root):
	"""
	56. 共参照解析
	Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
	(参考) http://kenichia.hatenablog.com/entry/2016/02/15/192635
	"""

	"""
	指示語を元の語に復元する。
	xmlファイルの構造は2つ => <sentences>と<coreference>

	=> <coreference>の部分をいじくる。
	例えば...
	<coreference>
	<mention representative="true">		=> 参照元となっている、元の単語・フレーズ
          <sentence>20</sentence>		=> 20文目の
          <start>17</start>				=> 17単語目から始まり
          <end>25</end>					=> 25単語目で終わる
          <head>19</head>				=> 係り受けでこのフレーズで核をなす単語は19単語目。今回なら"rules"
          <text>hard if-then rules similar to existing hand-written rules</text>
        </mention>
        <mention>						=> 二つ目以降のmentionが、一つ目のmentionを参照している
          <sentence>20</sentence>		=> 具体的には、20文目の7~8単語目にある"algorithms"
          <start>7</start>
          <end>8</end>
          <head>7</head>
          <text>algorithms</text>
        </mention>
      </coreference>					=> ここで参照関係の記述終わり。
	こんな感じの中身。

	=> 具体的に行う処理は、mention(2つ目以降)にある単語を特定して、そこにmention representative="true"を代入する、という作業になりそう。
	"""

	# 例えば、参照されている元の表現はこれで全部
	for mention in root.iter("coreference"):
		print mention[0][4].text

	return

def task_57():

	"""
	57. 係り受け解析
	Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
	"""

	return



if __name__ == '__main__':
	# nlp_data = data_loader()
	# sentence_list = task_50(nlp_data)
	# word_list = task_51(sentence_list)
	# task_52(word_list)
	# task_53(nlp_data)
	root = xml_loader()
	# task_54(root)
	# task_55(root)
	task_56(root)



