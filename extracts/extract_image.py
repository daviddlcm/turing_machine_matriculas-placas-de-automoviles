from PIL import Image
import pytesseract

def extract_text_image (image_path):
    from PIL import Image
    import pytesseract
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text