from paddleocr import PaddleOCR
import cv2


class Rect:
    def __init__(self, x1, y1, x2, y2, text):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.center = (x1 + x2) / 2
        self.text = text

    def __str__(self):
        return "Rect[%d, %d, %d, %d]" % (self.x1, self.y1, self.x2, self.y2)

    def __repr__(self):
        # return "center: %d, text: %s" % (self.center, self.text)
        return "%s, " % self.text


def grouper(iterable):
    prev = None
    group = []
    for item in iterable:
        if prev is None or item.center - prev <= 7:
            group.append(item)
        else:
            yield group
            group = [item]
        prev = item.center
    if group:
        yield group


ocr = PaddleOCR(use_angle_cls=True, lang='en')
img_path = 'img2.png'
result = ocr.ocr(img_path, cls=True) or []
# result.sort(key=lambda x: x[0][1])
rectangles = []
for i in result:
    rectangles.append(Rect(i[0][0][0], i[0][0][1], i[0][2][0], i[0][0][1], i[1][0]))
print(len(result))
rectangles.sort(key=lambda x: x.center)

groups = dict(enumerate(grouper(rectangles), 1))
for i in groups.keys():
    groups[i].sort(key=lambda x: x.y1)
print(groups)

with open('without_grouping.txt', 'w+') as fil:
    for line in result:
        fil.write(f'{line[1][0]}\n')

with open('with_grouping.txt', 'w+') as fil:
    for g in groups.keys():
        for i in groups[g]:
            fil.write(f'{i.text}\n')

img = cv2.imread('img.png')

for i in result:
    cv2.rectangle(img, (int(i[0][0][0]), int(i[0][0][1])), (int(i[0][2][0]), int(i[0][2][1])), (0, 255, 0), 2)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
