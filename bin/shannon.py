import Image
import math
import sys


def image_entropy(img):

    # calculate the shannon entropy for an image

    histogram = img.histogram()
    histogram_length = sum(histogram)

    samples_probability = [float(h) / histogram_length for h in histogram]

    return -sum([p * math.log(p, 2) for p in samples_probability if p != 0])


if __name__ == '__main__':

    import sys

    path = sys.argv[1]

    img = Image.open(path)
	
    print image_entropy(img)
