import sys
import cv2
import pytesseract
import argparse

# configurations
config = ('-l eng --oem 1 --psm 3')
# set path to tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'

def return_txt(filename):
	return filename.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')

def text_extraction(image_file):
	# read image
	img = cv2.imread(image_file)
	file_name = return_txt(image_file)

	text = pytesseract.image_to_string(img, config=config)

	with open(file_name, 'w+') as fil:
		fil.write(text)
		print(text)

def main(args):
	if not args.file.endswith(('.jpg', '.jpeg', '.png')):
		print('Invalid filname passed, file must end with .jpg, .jpeg, .png')
		sys.exit(1)
	
	print(f'Extracting text from "{args.file}", text output "{return_txt(args.file)}"')
	print('------------------------')
	text_extraction(args.file)
	print('------------------------')
	print('Text extraction complete\n')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Extract text from provided image.')
	parser.add_argument('--file', type=str, help='filename for image to be extracted', required=True)
	args = parser.parse_args()
	main(args)