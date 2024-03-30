from google.cloud import vision
import io, os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Haeju/OneDrive/Documents/bowling_project/concise-clock-416019-89f5e8c52164.json'

def detect_text(path):
    """Detects text in the image file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        return texts[0].description
    else:
        return None

# Example usage
image_path = 'test_score.jpg'
extracted_text = detect_text(image_path)
if extracted_text:
    print(extracted_text)
else:
    print("No text found.")