"""Latexify root package."""
    from latexify import _version

    __version__ = _version.__version__
except:
    __version__ = ""

get_latex = frontend.get_latex

function = frontend.function
expression = frontend.expression

# Deprecated
with_latex = frontend.with_latex
