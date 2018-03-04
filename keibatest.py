import bs4
import urllib.request
import re
import datetime
import os
import codecs

#url = "http://db.netkeiba.com/race/201808020611/"
url = "http://db.netkeiba.com/race/201808020603/"
html = urllib.request.urlopen(url).read()

soup1 = bs4.BeautifulSoup(html, "html.parser")
sss = str(soup1.prettify())

pattern = r"<table cell.*</table>\n<script"
table = re.findall(pattern,sss,flags=re.DOTALL)
#print(table[0])

soup= bs4.BeautifulSoup(table[0], "html.parser")
#print(soup.prettify())
#while (soup.td):
#	soup.td.unwrap()

while (soup.a):
    soup.a.unwrap()

#while (soup.tr):
 #   soup.tr.unwrap()

while (soup.span):
    soup.span.unwrap()

while (soup.div):
    soup.div.unwrap()

while (soup.diary_snap_cut):
    soup.diary_snap_cut.unwrap()

while (soup.br):
    soup.br.unwrap()

while (soup.th):
    soup.th.unwrap()

while (soup.img):
    soup.img.unwrap()

while (soup.img):
    soup.img.unwrap()
#print(soup.prettify())
#print(type(soup))
trlist = soup.find_all("tr")
del trlist[0]
#print(trlist)
for l in trlist:
	lstr = str(l.prettify())
	lstr = lstr.replace('<tr>\n','').replace('\n</tr>','')
	#print(lstr)
	elems = lstr.splitlines()
	#print(elems[9])
	
	for i in range(len(elems)):
		elems[i] = elems[i].strip()
		#print('['+elems[i]+']')
	print(str(len(elems)))
	#print(elems)
	i=0
	conti = 1
	while conti==1:
		m = re.match(r'<td.*>',elems[i])
		if m and elems[i+1] == '</td>':
			elems.insert(i+1,'none')
		i+=1
		if len(elems)-1<i:
			conti=0

	print(str(len(elems)))
	#print(elems[8])
	f = codecs.open('keibaout.csv', 'a','cp932') # 書き込みモードで開くcp932
	write=''
	j = 0
	#print(elems)
	while j < len(elems):
		m = re.match(r'<td.*>',elems[j])
		if m or elems[j] == '</td>':
			write+=''
		else :
			write+=elems[j]+','
		j+=1
	f.write(write+'\n') # 引数の文字列をファイルに書き込む
	f.close()
		 # ファイルを閉じる
	#print(str(len(elems)))
	#print(elems)
	#for elem in elems:
	#	print('a'+elem)
	#print('a'+lstr+'a')

#while (soup.table):
 #   soup.table.unwrap()
#print(soup)

#st = soup.prettify()
#print("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+str(st)+"uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
#s=str(soup.prettify())
#s = s.replace(u'\xa0', u' ')
#s = s.replace(u'\xa9', u' ')
#print(s)

#rows = re.findall(r'<tr>.*</tr>',s,flags=re.DOTALL)		
#print(rows)



#s=st.replace('\xa.*','')

#s= s.replace('<!DOCT'+pattern+'<table cell','')

#f = codecs.open('keibatext.txt', 'w','utf-8') # 書き込みモードで開く
#f.write(s) # 引数の文字列をファイルに書き込む
#f.close() # ファイルを閉じる

#table = re.findall('<table cell.*</table>',s)
#print(table)
#for t in table:
 # print(t)