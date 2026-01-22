def mask_area(image, coords):
    x,y,w,h = coords
    image[y:y+h, x:x+w] = 255
    return image
