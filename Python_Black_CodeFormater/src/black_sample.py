
'Python'

def some_long_function(ham: int, spam: str, eggs: List[str], foo: Dict[str, str], bar: bool=True, baz: bool=False):
    pass


# 実行コマンド↓
# C:\Users\ryury\Desktop\black>black --diff src/black_sample.py

# 出力結果
# --- src\black_sample.py 2021-08-13 21:27:59.364841 +0000
# +++ src\black_sample.py 2021-08-13 21:31:41.764635 +0000
# @@ -1,8 +1,13 @@
# +"Python"

# -'Python'

# -def some_long_function(ham: int, spam: str, eggs: List[str], foo: Dict[str, str], bar: bool=True, baz: bool=False):
# +def some_long_function(
# +    ham: int,
# +    spam: str,
# +    eggs: List[str],
# +    foo: Dict[str, str],
# +    bar: bool = True,
# +    baz: bool = False,
# +):
#      pass

# -
# -
# reformatted src\black_sample.py
# All done! ✨ 🍰 ✨
# 1 file reformatted.