# python3 -m venv clingo-env
# source clingo-env/bin/activate
# pip install clingo
import clingo

ctl = clingo.Control()
ctl.add("base", [], """
parent(john, mary).
parent(mary, susan).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
""")
ctl.ground([("base", [])])

# Solve and print models (answer sets)
with ctl.solve(yield_ = True) as handle:
    for model in handle:
        print("Answer Set:", model.symbols(shown=True))