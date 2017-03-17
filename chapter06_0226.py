#coding:utf-8

import codecs
import corenlp
import csv
import nltk
import pandas as pd
import pydot
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
	tree = ET.parse(xml_file_name)
	root = tree.getroot()

	return tree,root



def task_54(tree):

	"""
	54. 品詞タグ付け
	Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
	(参照) http://qiita.com/segavvy/items/4d55805352089332828e
	"""

	for token in tree.iter("token"):
		print token.findtext("word"),"\t",token.findtext("lemma"),"\t",token.findtext("POS")

	return


def task_55(tree):

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
	for token in tree.iter("token"):
		if token.findtext("NER") == "ORGANIZATION" or token.findtext("NER") == "PERSON":
			nerList.extend([token.findtext("word")])
	print set(nerList)
	# この結果だとなんかandとかofが入っている・・・・

	return


def task_56(nlp_data,tree,root):
	"""
	56. 共参照解析
	Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．

	(参考) 	http://kenichia.hatenablog.com/entry/2016/02/15/192635
			http://qiita.com/segavvy/items/0340d3d71c9151265bcb
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
	# for mention in root.iter("coreference"):
	# 	print mention[0][4].text


	# 56について以下は、ここからほぼ借用しています => http://qiita.com/segavvy/items/0340d3d71c9151265bcb

	# 修正に必要な情報をまとめる。キーは参照元の名詞句、値は参照先の名詞句のアドレスを何らかの形で。
	modify_dic={}
	for coreference in root.iterfind('./document/coreference/coreference'):

		# 代表参照表現の取得
		refered_text = coreference.findtext('./mention[@representative="true"]/text')

		# 代表参照表現以外のmention列挙、辞書に追加
		for mention in coreference.iterfind('./mention'):
			if mention.get('representative', 'false') == 'false':

			# 必要な情報の抽出
				sent_id = int(mention.findtext('sentence'))
				start_index = int(mention.findtext('start'))
				end_index = int(mention.findtext('end'))

				if not (sent_id, start_index) in modify_dic:
					modify_dic[(sent_id, start_index)] = (end_index, refered_text)

	# ここから修正しながら表示する
	for sentence in root.iterfind('./document/sentences/sentence'):
		sent_id = int(sentence.get('id'))       # sentenceのid
		org_rest = 0                            # 置換中のtoken数の残り
		string_array = ""

		# token列挙
		for token in sentence.iterfind('./tokens/token'):
			token_id = int(token.get('id'))     # tokenのid

			# 置換対象？
			if org_rest == 0 and (sent_id, token_id) in modify_dic:

            	# 辞書から終了位置と代表参照表現を取り出し
				(end, rep_text) = modify_dic[(sent_id, token_id)]

				# 代表参照表現＋カッコを挿入
				string_array = string_array + '[' + refered_text + ']' + " "
				# print '[' + refered_text + ']'
				org_rest = end - token_id       # 置換中のtoken数の残り

			# token出力
			string_array = string_array + token.findtext('word') +" "
			# print token.findtext('word')

	        # 置換の終わりなら閉じカッコを挿入
			if org_rest > 0:
				org_rest -= 1
			# if org_rest == 0:
				# string_array = string_array + ')'
				# print(')')

		print string_array

	return



def task_57(root):

	"""
	57. 係り受け解析
	Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
	"""
	"""
	具体的には、ROOTと各単語、依存関係の発生している方向を各エッジについて読み込んで、それを描画すればok.
	"""

	# ひとまず、依存関係を各文章毎に書き出してみる
	edge_list=[]
	for i,sentence in enumerate(root[0][0]):
		print i,"番目の文の依存関係は..."
		tmp=[]
		for dependency in sentence[3]:
			print dependency[0].text,"->",dependency[1].text
			tmp.append(tuple([dependency[0].text,dependency[1].text]))
		edge_list.append(tmp)
		print "\n"

	# 同じディレクトリ以下にgraph_pngという書き出し用のディレクトリを作成。。。
	for i,edges in enumerate(edge_list):
		g=pydot.graph_from_edges(edges, directed=True)
		file_name = "./graph_png/nlp_"+str(i)+".png"
		g.write_png(file_name, prog='dot')

	return


def task_58(root):

	"""
	58. タプルの抽出
	Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

    述語: nsubj関係とdobj関係の子（dependant）を持つ単語
    主語: 述語からnsubj関係にある子（dependent）
    目的語: 述語からdobj関係にある子（dependent）

	(参照) 	http://qiita.com/segavvy/items/f100fc38e350ad14b679
			http://kenichia.hatenablog.com/entry/2016/02/15/192635
	"""

	"""
	処理の内容:
	各文に対して、述語をfixして、それに紐づく主語と目的語を抽出する
	"""

	for i,sentence in enumerate(root[0][0]):
		for dep in sentence[3]:

			if "nsubj" in dep.get("type"):
				nsubj_govnr = dep.find('./governor').text
				nsubj_dep = dep.find('./dependent').text

			if "dobj" in dep.get("type"):
				dobj_govnr = dep.find('./governor').text
				dobj_dep = dep.find('./dependent').text

				if nsubj_govnr == dobj_govnr:
					print nsubj_dep,"\t",dobj_govnr,"\t",dobj_dep

	return



def task_59(root):

	"""
	59. S式の解析
	Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
	"""

	"""
	S式の中身はこんなん。
	<parse>(ROOT (S (ADVP (RB Increasingly)) (, ,) (ADVP (RB however)) (, ,) (NP (NN research)) (VP (VBZ has) (VP (VBN focused) (PP (IN on) (NP (NP (JJ statistical) (NNS models)) (, ,) (SBAR (WHNP (WDT which)) (S (VP (VBP make) (NP (JJ soft) (, ,) (JJ probabilistic) (NNS decisions)) (PP (VBN based) (PP (IN on) (S (VP (VBG attaching) (NP (JJ real-valued) (NNS weights)) (PP (TO to) (NP (DT each) (NN input) (NN feature)))))))))))))) (. .))) </parse>
	このNPを取ってくる。正規表現を適当に使う。
	NPのすぐ左の(から、任意の数の()セットを終えて、)が得られるまでを取ってくる。
	"""

	NP_list=[]
	for i,sentence in enumerate(root[0][0]):

		_S = sentence.find("./parse").text,"\n"
		tmp_list = re.findall(r"(\(NP\s(\((JJ|NN|NNS)\s\w+\)\s*)(\((JJ|NN|NNS)\s\w+\)\s*)+\))" ,_S[0])
		if not len(tmp_list) ==0:
			NP_list.extend(tmp_list)

	for i in NP_list:
		print i

	return


if __name__ == '__main__':
	nlp_data = data_loader()
	sentence_list = task_50(nlp_data)
	word_list = task_51(sentence_list)
	task_52(word_list)
	task_53(nlp_data)
	tree,root = xml_loader()
	task_54(root)
	task_55(root)
	task_56(nlp_data,tree,root)
	task_57(root)
	task_58(root)
	task_59(root)



