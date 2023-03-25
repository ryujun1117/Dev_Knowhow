def triangle(bottom: float, heigth: float) -> float:
    """三角形の面積を求める関数"""
    area = (bottom * height) / 2
    return area


area = triangle('3', 4.5)


# 上記の実行
# C:\Users\ryury\Desktop\mypy>mypy src/mypy_sample.py
# 上記の出力結果
# src\mypy_sample.py:3: error: Name 'height' is not defined
# src\mypy_sample.py:7: error: Argument 1 to "triangle" has incompatible type "str"; expected "float"
# Found 2 errors in 1 file (checked 1 source file)

