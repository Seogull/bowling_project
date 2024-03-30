import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext('test_score.jpg')

for (bbox, text, prob) in results:
    print(text)
