# introduction

windows has a weird khmer font (unicode), this causes issue when you have telegram install on your computer
and some of your group chat using khmer language,

the problem:
font appear to small for unicode.

to temporary resolve the issue,
you need to make change in windows registry under `FontSubstitutes` --> `MS Shell Dlg 2` with the value of new khmer font ex: `Khmer OS`

this script will do all of that for you.

## installation

install pre-req

```
pip install winregistry
```

and on line 20 of main.py file choose whatever font name you prefer

```
set_run_key("MS Shell Dlg 2", "Khmer OS")
```
