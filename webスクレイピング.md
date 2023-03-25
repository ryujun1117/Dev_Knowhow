barchec→branchedだっちゅうの

Webスクレイピング（参考：O’REILLY　退屈なことはPythonにやらせよう　より）

Pythonで簡単にwebスクレイピングをするのに役立つモジュール達
	webbrowser：Python付属のモジュール。指定したページをブラウザで開く
	Requests：ネットからファイルやwebページをダウンロードする
	Beautiful Soup：webページの記法であるHTMLをパース（文法的解釈）する
	Selenium：webブラウザ制御。ブラウザ上のフォームの記入やクリックもできる

BeautifulSoupオブジェクトのselect()メソッドを用いて要素を見つける
＜CSSセレクタの例＞	
select()に渡すセレクタ
マッチする対象
soup.select(‘div’)
すべての<div>要素
soup.select(‘#author’)
id属性がauthorである要素
soup.select(‘.notice’)
CSSクラス属性がnoticeである全要素
soup.select(‘div span’)
<div>要素の中のすべての<span>要素
soup.select(‘div > span’)
<div>要素の直下のすべての<span>要素
soup.select(‘input[name]’)
name属性（値は任意）を持つ全ての<input>要素
soup.select(‘input[type=”button”]’)
type属性の値がbuttonであるすべての<input>



tutorialプロジェクト：Google検索 “I’m Feeling Lucky”
※beautifulsoupがjavascriptのある動的なサイトを取れないっぽいのでchromeの設定でoffにしてから開発するのが良いかも。（見やすくなるし）
-googling.py-
#! python3
# googling.py - googleの検索結果をいくつか開く
import requests, sys, webbrowser, bs4
print("googling...")
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status
#上位の検索結果のリンクを取得する
soup = bs4.BeautifulSoup(res.text)
link_elems = soup.select('.kCrYT > a')
#各結果のブラウザのタブを開く
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))




twitter trend→slack：いまにゅさんのTwitter API講座
（参考：OAuth認証(modureのインストール)）


 Web APIの使い方：いまにゅさんのPythonでWebAPIを叩く
Web APIを用いればwebスクレイピングする必要がなく、かつ簡単に情報を取得することができる
※access key：d17efae006bb11f2d80f12960d7c8760
APIを叩く場所を「エンドポイント」という
	→リクエストパラメータをエンドポイントに渡してレスポンスを得る

-grunabi_api.py-

!pip install requests
import requests

#APIのurlを挿入
url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'

#パラメータkeyidが必須！
params = {}
params['keyid']='d17efae006bb11f2d80f12960d7c8760'
params['freeword'] = '札幌駅,肉'

#APIにリクエスト
response = requests.get(url, params)

#レスポンスの解析
#response.json()
import pprint
#pprint.pprint(response.json())
results = response.json()
#results['rest']
print(len(results['rest']))
restaurants = results['rest']
print(restaurants[0]['name'])
print(restaurants[0]['tel'])
  
  
  

webscraping【実践編】「ついっトレンド」からトレンドを抽出！
【環境設定】
#python version確認
$ python -V
Python 3.9.0
#仮想環境名
“twittrend”

【準備】
仮想環境を作成！→activate
仮想環境内で必要なモジュールをpipでインストール
【実装】
そのままjupyter labを起動。
webscraping　-chromeの検証ツールでhtmlを読んでみよう-
webscraping　-抽出順を考えよう（大→小）-
webscraping　-実装→必要な要素のみ段階的にを抽出-
【slackでチャンネルに通知！】
“incoming-webhook(slackのアプリ)”を投稿チャンネルに紐付ける
通知内容の作成→取得した”webhook url”を利用して投稿！
【準備】
仮想環境を作成！→activate【参考】
#新しいフォルダを作成→移動
cd：ディレクトリの移動, dir：ディレクトリ内の要素を確認, mkdir：ファイル・ディレクトリ作成

#内部に仮想環境を作成（適切か不明）
$ python -m venv twittrend
#仮想環境を起動（仮想環境内のactivateファイルを実行する）
$ .\twittrend\Scripts\activate
#仮想環境の停止
$ deactivate
仮想環境内で必要なモジュールをpipでインストール
#まずはpipをupgradeする
$ c:\users\ryuichi1117\dev\websc\twittrend\scripts\python.exe -m pip install --upgrade pip
(※以下のインストールコマンドをそのまま実行すると警告文が出てきてそこでupgradeを提案されます↑)
#今回は3つ。
#requests：サーバからhtmlファイルを取得するリクエストを送る
#beautifulsoup4：htmlファイルの解析と抽出
#slackweb：slackへのメッセージ送信用モジュール
pip install requests
pip install beautifulsoup4
pip install slackweb

【実装】
そのままjupyter labを起動。
$ jupyter lab
(※インストールは$ pip install jupyterlab)
webscraping　-chromeの検証ツールでhtmlを読んでみよう-
webscraping　-抽出順を考えよう（大→小）-
webscraping　-実装→必要な要素のみ段階的にを抽出-

#必要なモジュールのインストール
import requests
from bs4 import BeautifulSoup
 
 
#リンクを指定
twittrend = {
    "twittrend":"https://twittrend.jp/"
}
 
#webscraping...
r = requests.get(twittrend["twittrend"])
soup = BeautifulSoup(r.content, "html.parser")
japan = soup.select("#japan")
 
#トレンドの更新日時を取得→整形
time = japan[0].select(".box-header")
time = time[0].getText()
time = time.replace('\n', '')
 
#トレンドのテキストとリンクを取得
trend_title=[]
trend_link=[]
trendtitle = japan[0].select(".list-unstyled li .trend")
trendlink= japan[0].select(".list-unstyled li a")
for i in range(10):
    trend_title.append(trendtitle[i].getText())
    trend_link.append(trendlink[i].get("href"))
 
#slackで指定チャンネルに通知
import slackweb
slack = slackweb.Slack(url = "https://hooks.slack.com/services/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")
text_1 = "<"+ trend_link[0] +"|"+ trend_title[0] +">"
text_2 = "<"+ trend_link[1] +"|"+ trend_title[1] +">"
text_3 = "<"+ trend_link[2] +"|"+ trend_title[2] +">"
text_4 = "<"+ trend_link[3] +"|"+ trend_title[3] +">"
text_5 = "<"+ trend_link[4] +"|"+ trend_title[4] +">"
text_6 = "<"+ trend_link[5] +"|"+ trend_title[5] +">"
text_7 = "<"+ trend_link[6] +"|"+ trend_title[6] +">"
text_8 = "<"+ trend_link[7] +"|"+ trend_title[7] +">"
text_9 = "<"+ trend_link[8] +"|"+ trend_title[8] +">"
text_10 = "<"+ trend_link[9] +"|"+ trend_title[9] +">"
text_all = "*【Twitter_trend：" + time +"】*" +"\n"+ text_1+"\n" + text_2+"\n" + text_3+"\n" + text_4+"\n" + text_5+"\n" + text_6+"\n" + text_7+"\n" + text_8+"\n" + text_9+"\n" + text_10+"\n"
slack.notify(text =text_all, channel="#bot_test")
 
print("success!")

