import pytesseract
import cv2
import os

class AnalysisAgent:
    def __init__(self):
        self.name = "AnalysisAgent"
        if os.name == "nt":
            tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            if os.path.exists(tess_path):
                pytesseract.pytesseract.tesseract_cmd = tess_path

    def process(self, image):
        """
        Scans the image using OCR.
        Returns: { 'text_data': dict, 'log': str }
        """
        log = []
        log.append(f"[{self.name}] Starting OCR scan...")
        
        try:
            # We use image_to_data to get coordinates
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
            word_count = len([x for x in data['text'] if x.strip()])
            log.append(f"[{self.name}] Scan complete. Found {word_count} text elements.")
            return {'text_data': data, 'log': log}
        except Exception as e:
            log.append(f"[{self.name}] Error during scan: {str(e)}")
            return {'text_data': None, 'log': log}
