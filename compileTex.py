#get directory and file name
curDir = open("curdir.txt", "r")
flName  = open("fileName.txt", "r")
directory = curDir.readline()
fileName = flName.readline()[:-1] #ignore newline character (\n)
curDir.close()
flName.close()

# setup files for compiling
curfile = open("cur"+fileName, "r")
firstLine = curfile.readline().split(';')
firstLine[-1] = firstLine[-1][:-1]
for i in range(len(firstLine)):
        firstLine[i] = firstLine[i].strip()
newfile = open(fileName, "w")

#Create, compile, and close  files
if ("documentclass" not in firstLine[0]):
    # Change document type (ex. letter, slides, book, report, beamer etc.) (note: [0] = doc type)
    if "letter" in firstLine[0]:
        if "[" in firstLine[0]: #mainly for font size (\documentclass[12pt]{article})
            newfile.write("\\documentclass[" + firstLine[0].split('[')[1] + "{letter}\n")
        else:
            newfile.write("\\documentclass{letter}\n")
    elif ( "beamer" in firstLine[0] ):
        if "[" in firstLine[0]: #mainly for font size (\documentclass[12pt]{article})
            newfile.write("\\documentclass[" + firstLine[0].split('[')[1] + "{beamer}\n")
        else:
            newfile.write("\\documentclass{beamer}\n")
    else: # default article
        newfile.write("\\documentclass{article}\n")

    # add any extra things to preamble (ex \title{example})
    for keyword in firstLine:
        if '\\' in keyword:
            newfile.write(keyword + "\n")

    # Choose write template and compile document. Can also not add a template.
    if "no preamble" not in firstLine[-1]:
        if "letter" in firstLine[0]:
            template = open("letterTemplate.tex", "r")
        elif ( "beamer" in firstLine[0] ):
            template = open("beamerTemplate.tex", "r")
        else: #default template is for "article"
            template = open("template.tex", "r")
        newfile.write(template.read())
        template.close()
    else:
        newfile.write("\\begin{document}\n")

    # create rest of file.
    newfile.write(curfile.read())
    newfile.write("\\end{document}")
else: #If tex file already has preamble
    newfile.write(firstLine[0] + '\n')
    newfile.write(curfile.read())
curfile.close()
newfile.close()
