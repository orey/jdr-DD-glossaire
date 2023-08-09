#--------------------------------------------------
# Builds the md file
# Copyleft: Olivier Rey
# Date: August 2023
#--------------------------------------------------
#!/bin/python3
import glob
import json
from datetime import datetime

# Global grammar
VERSION = "version"
LETTER = "letter"
GLOSSARY = "glossary"

# Record grammar
EN = "en"
FR = "fr"
TYPE = "type"
SOURCE = "source"
DDVERSION = "dd-version"


def format_md(parsed,output):
    letter = parsed[LETTER]
    output.write("## " + letter.capitalize() + "\n\n")
    gloss = parsed[GLOSSARY]
    for e in gloss:
        en = e[EN]
        fr = e[FR]
        typ = e[TYPE]
        source = e[SOURCE]
        ddv = e[DDVERSION]
        output.write("**" + en.capitalize() + "** : " + fr + ". " + typ.capitalize() + ". D&D version " + str(ddv) + "\n\n")    
        


if __name__ == "__main__":
    files = glob.glob('*.json')
    with open("GLOSSAIRE.md", "w") as output:
        output.write("# GLOSSAIRE D&D\n\n")
        output.write("Généré le " + str(datetime.now()) + "\n\n")
        for f in files:
            with open(f, "r") as user_file:
                file_contents = user_file.read()
                print(file_contents)
                parsed = json.loads(file_contents)
                format_md(parsed,output)



