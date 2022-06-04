# One Piece Database Project

## Install dependencies

1. [Install Tesseract](https://tesseract-ocr.github.io/tessdoc/Installation.html)
2. Install requirements.txt: `$ pip install -r requirements.txt`

## Download all One Piece Chapters

[Download One Piece](https://drive.google.com/file/d/1sVP09rxeVV0JzIz5X8sMJyRXNHCgm_aw/view?usp=sharing)

Warning this is a large zip file ~4GB

## Text extraction

Remember to set your tesseract path in `main.py` line 9

For example:

`pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'`

Text is extracted to \<filename>.txt

For example img2.png will output to img2.txt

Example execution:

`$ python main.py --file img2.png`

## Automate text extraction for all chapters

Make sure the One_Piece folder is in the root directory of this project. This will output all the .txt files in each folder per manga panel.

`$ bash automate_extraction.sh`
