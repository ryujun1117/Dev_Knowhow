開発環境構築（version管理と仮想環境を適切に利用し、持続可能な開発環境を整える）

pythonのインストール（参考：windows版: python 仮想環境管理 venvとanaconda）
	https://www.python.org/downloads/windows/
	Windows x86-64 executable installer のExeファイルからインストール（Python 3.9.0）
	→パスをつなぐ（C:\Users<自分のユーザー名>\AppData\Local\Programs\Python\Python39）
	※バージョン確認：python -v

pipのインストール（※python 3.9.0には最初から入っている）

pipを最新状態に更新する（参考：pipでインストールしたライブラリの更新方法）
py -m pip install --upgrade pip
→installed pip-20.2.4

仮想環境を作る準備
virtualenvのインストール
pip install virtualenv

virtual envで、仮想環境を作って使う
	C:\Users\<ユーザー名>py -m venv tutorial-env
C:\Users\<ユーザー名>tutorial-env\Scripts\activate.bat

→(tutorial-env) C:\Users\ryuichi1117\Dev>
先頭に(仮想環境名)がつけばok
	※仮想環境を抜けるには：deactivate

Jupyter labのインストール（参考：図解！Jupyter Labを徹底解説！(インストール・使い方・拡張機能)）
(AnacondaをいれずにJupyter Labだけをいれます)
	インストール：pip install jupyterlab
	起動：jupyter lab
Jupyter labはjupyter notebookの上位互換らしい。ページ内でターミナル開けたり、実行結果を合わせて市ファイルとしてシェアが可能なので便利です。（公式ドキュメント）

※Numpyのインストール
	Numpy1.19.4が調子悪いのでバージョンを一つ下げるので対応
	pip install numpy==1.19.3






