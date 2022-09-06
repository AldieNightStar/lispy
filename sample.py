from lispy import parse

src = """
    (
        # 1
        2
        3
    )
    (func a b c (do
        (return (add a b c))
    ))
    (func 1 2 3 hello\\ world!:-\\) 111)
"""

for i in parse(src):
    print(i)