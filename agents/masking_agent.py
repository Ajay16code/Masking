import cv2
import numpy as np

class RedactionAgent:
    def __init__(self):
        self.name = "RedactionAgent"

    def process(self, image, regions):
        """
        Applies masks to the image.
        Returns: { 'masked_image': img, 'log': str }
        """
        log = []
        log.append(f"[{self.name}] Received {len(regions)} redaction targets.")
        
        out_img = image.copy()
        
        if not regions:
             log.append(f"[{self.name}] No regions to mask.")
             return {'masked_image': out_img, 'log': log}

        for r in regions:
            x, y, w, h = r['x'], r['y'], r['w'], r['h']
            
            # Draw White Rectangle
            cv2.rectangle(out_img, (x, y), (x+w, y+h), (255, 255, 255), thickness=-1)
            
            # Overlay "XXXXX" pattern
            mask_text = "XXXXX"
            font = cv2.FONT_HERSHEY_SIMPLEX
            # Scale font to fit height
            scale = max(0.4, h / 30) 
            thickness = 1
            (tw, th), _ = cv2.getTextSize(mask_text, font, scale, thickness)

            tx = x + (w - tw) // 2
            ty = y + (h + th) // 2
            
            if tx > x and ty < y+h: # Check bounds
                cv2.putText(out_img, mask_text, (tx, ty), font, scale, (0, 0, 0), thickness, cv2.LINE_AA)

        log.append(f"[{self.name}] Applied {len(regions)} redaction masks.")
        return {'masked_image': out_img, 'log': log}
