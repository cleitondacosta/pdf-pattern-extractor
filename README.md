# PDF Pattern Extractor

<p align="center">
<img src="https://raw.githubusercontent.com/cleitondacosta/pdf-pattern-extractor/master/examples/pdf-pattern-extractor.png" alt="printscreen" />
</p>

A software to automate a boring and error prone manual task:
Extract pdf pages containing a pattern in one or more pdf files. 
Those pages are extracted into a new pdf file.

## Features

- Pattern as a text
- Pattern as a regular expression 
(<a href="https://docs.python.org/3/library/re.html#regular-expression-syntax">
Python regex syntax
</a>)
- There is a command line version (cli.py), but it only supports regex.

## Running

Make sure that you have git and python >=3.6 installed.
Also, you may need to install a tk package. 
Refer to your distribution package manager.

### Install dependencies

```
sudo pip3 install PyPDF2
```

### Clone and run

```
git clone https://github.com/cleitondacosta/pdf-pattern-extractor.git
cd pdf-pattern-extractor/src
chmod +x app.py
./app.py
```

If you want to distribute this software, take a look at 
<a href="https://www.pyinstaller.org">pyinstaller</a>
or similar.

## Limitations :warning:

This project uses PyPDF2 module to handle pdf files, so it may not work
since this module has some issues:
<a href="https://pythonhosted.org/PyPDF2/PageObject.html#PyPDF2.pdf.PageObject.extractText">extractText() may fail.</a>

## Usage examples

### Extract any page containing a CPF (Brazilian SSN)

<p align="center">
<img src="https://raw.githubusercontent.com/cleitondacosta/pdf-pattern-extractor/master/examples/example1.png" alt="printscreen-example1" />
</p>

### Extract any page containing a sequence of five numbers

<p align="center">
<img src="https://raw.githubusercontent.com/cleitondacosta/pdf-pattern-extractor/master/examples/example2.png" alt="printscreen-example2" />
</p>

### Extract any page containing my name

<p align="center">
<img src="https://raw.githubusercontent.com/cleitondacosta/pdf-pattern-extractor/master/examples/example3.png" alt="printscreen-example3" />
</p>

## License

MIT.
