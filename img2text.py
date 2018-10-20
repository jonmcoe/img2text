import sys

import numpy as np
from PIL import Image


GRAY_CHARS = [' ', '.', ':', '|', '+', '=', '3', '#', '@']  # length must be power of 2
BOUNDS = list(range(0, 2**8, 2**8 // len(GRAY_CHARS)))


def main():
    input_img_filename = sys.argv[1]
    pixel_scale = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    g = (
        (GRAY_CHARS[p - 1] for p in r)
        for r in np.digitize(np.array(Image.open(input_img_filename).convert(mode='L')), BOUNDS)
    )
    for l in list(g)[::pixel_scale]:  # TODO: how to do this smart with iterator and not list cast?
        print(''.join(list(l)[::pixel_scale]))


if __name__ == '__main__':
    main()