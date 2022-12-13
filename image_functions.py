import cv2 as cv

# Grayscale function
def grayscale(img, h, w):
    i = 0
    j = 0
    while i < h:
        while j < w:
            b = img.item(i, j, 0)
            g = img.item(i, j, 1)
            r = img.item(i, j, 2)

            avg = round((b + g + r) / 3.0)
            img.itemset((i, j, 0), avg)
            img.itemset((i, j, 1), avg)
            img.itemset((i, j, 2), avg)
            j += 1
        i += 1
        j = 0
    return img

def sepia(img, h, w):
    i = 0
    j = 0
    while i < h:
        while j < w:
            b = img.item(i, j, 0)
            g = img.item(i, j, 1)
            r = img.item(i, j, 2)

            sb = round((0.272 * r) + (0.534 * g) + (0.131 * b))
            sg = round((0.349 * r) + (0.686 * g) + (0.168 * b))
            sr = round((0.393 * r) + (0.769 * g) + (0.189 * b))

            if sb > 255:
                sb = 255
                img.itemset((i, j, 0), sb)
            else:
                img.itemset((i, j, 0), sb)
            if sg > 255:
                sg = 255
                img.itemset((i, j, 1), sg)
            else:
                img.itemset((i, j, 1), sg)
            if sr > 255:
                sr = 255
                img.itemset((i, j, 2), sr)
            else:
                img.itemset((i, j, 2), sr)
            j += 1
        i += 1
        j = 0
    return img

def mirror(img, h, w):
    i = 0
    j = 0
    while i < h:
        while j < w / 2:
            swap = img[i, j]
            img[i, j] = img[i, w - 1 - j]
            img[i, w - 1 - j] = swap
            j += 1
        i += 1
        j = 0
    return img

def reflect(img, h, w):
    return img

def scale(img, h , w):
    factor = float(input('Do you want to increase or decrease the photo size?\nTo decrease put a number greater than 1\nTo increase put a number between 0 and 1\nNumber: '))

    resized = cv.resize(img, (int(w/factor), int(h/factor)))
    return resized