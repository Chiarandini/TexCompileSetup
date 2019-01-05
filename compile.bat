python compileTex.py
type fileName.txt | lualatex -synctex=1 -interaction=nonstopmode -aux-directory=/tmp/ > C:/Users/Chiarandini/MyPrograms/ActiveScripts/latex/tmp/tmp.log 2>&1
rm curDir.txt
rm fileName.txt
