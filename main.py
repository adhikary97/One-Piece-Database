import sys
import cv2
import pytesseract
import argparse

# configurations
config = ('-l eng --oem 1 --psm 3')
# set path to tesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/5.1.0/bin/tesseract'


def text_extraction(image_file):
	# read image
	img = cv2.imread(image_file)
	file_name = image_file.split('.')[0]

	text = pytesseract.image_to_string(img, config=config)

	with open(f'{file_name}.txt', 'w+') as fil:
		fil.write(text)
		print(text)

def main(args):
	if not args.file.endswith(('.jpg', '.jpeg', '.png')):
		print('Invalid filname passed, file must end with .jpg, .jpeg, .png')
		sys.exit(1)
	
	print(f'Extracting text from "{args.file}", text output "{args.file.split(".")[0]}.txt"')
	print('------------------------')
	text_extraction(args.file)
	print('------------------------')
	print('Text extraction complete')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Extract text from provided image.')
	parser.add_argument('--file', type=str, help='filename for image to be extracted', required=True)
	args = parser.parse_args()
	main(args)