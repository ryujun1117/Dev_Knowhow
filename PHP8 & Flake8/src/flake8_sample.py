#samplecode
def greeting(name):
    return "hello, " +name
#関数の間が2行空いていない
def add(x,y): #カンマの後ろに空白がない
    return x +y #演算子の前後に空白がない
########################################################################
# flake8_sample.py:1:1: E265 block comment should start with '# '
# flake8_sample.py:3:23: E225 missing whitespace around operator
# flake8_sample.py:4:1: E265 block comment should start with '# '
# flake8_sample.py:5:1: E302 expected 2 blank lines, found 0
# flake8_sample.py:5:10: E231 missing whitespace after ','
# flake8_sample.py:5:14: E261 at least two spaces before inline comment
# flake8_sample.py:5:15: E262 inline comment should start with '# '
# flake8_sample.py:6:15: E225 missing whitespace around operator
# flake8_sample.py:6:16: E261 at least two spaces before inline comment
# flake8_sample.py:6:17: E262 inline comment should start with '# '
# flake8_sample.py:7:1: W391 blank line at end of file
########################################################################

# エラーなし↓※#あとに半角スペース一つ入れる
def greeting(name):
    return "hello, " + name


def add(x, y):
    return x + y
