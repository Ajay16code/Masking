import cv2
import os

class VisionAgent:
    def __init__(self):
        self.name = "VisionAgent"
        # Load Haar Cascade for face detection
        # Ensure the file is in the root or provide absolute path
        cascade_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "haarcascade_frontalface_default.xml")
        self.face_cascade = cv2.CascadeClassifier(cascade_path)

    def process(self, image):
        """
        Detects faces in the image.
        Returns: { 'regions': list, 'log': list }
        """
        log = []
        log.append(f"[{self.name}] Scanning visual spectrum for biological identities (Faces)...")
        
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            regions = []
            for (x, y, w, h) in faces:
                regions.append({
                    'x': x, 'y': y, 'w': w, 'h': h, 'label': 'FACE'
                })
            
            if len(regions) > 0:
                log.append(f"[{self.name}] Target acquired. {len(regions)} identities detected.")
            else:
                log.append(f"[{self.name}] No biological identities found in scan.")
                
            return {'regions': regions, 'log': log}

        except Exception as e:
            log.append(f"[{self.name}] Visual processing error: {str(e)}")
            return {'regions': [], 'log': log}
