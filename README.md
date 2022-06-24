# asciiartjsondb
A collection of ASCII art, stored in a single JSON file.

**If you want to look at the ascii art, click on the asciiartdb-asciiarteu.txt file.**

# Description of Files in This Repo

*downloadasciiartsites.bat* - A Windows batch file that uses wget to download the ascii art files. These commands can also be run on Linux/Mac machines.

*asciiArtEuExtractArt.py* - Extracts ascii art from the downloaded mirror of asciiart.eu and writes it to asciiartdb-asciiarteu.json.

*asciiArtEuConvertAsciiArtJsonToText.py* - Converts the ascii art in the json file asciiartdb-asciiarteu.json to an easier to read asciiartdb-asciiarteu.txt text file.

*asciiartdb-asciiarteu.json* - The ascii art from asciiart.eu in json format, where it can be parsed by programs.

*asciiartdb-asciiarteu.txt* - The ascii art from asciiart.eu in text format, where it can be easily viewed by humans.
