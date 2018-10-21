import sys

import numpy as np
from PIL import Image


GRAY_CHARS = np.array([' ', '.', ':', '|', '+', '=', '3', '#', '@'])  # length must be power of 2 + 1
BOUNDS = list(range(0, 2**8, 2**8 // (len(GRAY_CHARS) - 1)))


def make_text_from_image(input_img_filename, pixel_scale):
    return GRAY_CHARS[
        np.digitize(np.array(Image.open(input_img_filename).convert(mode='L')), BOUNDS)[::pixel_scale, ::pixel_scale]
    ]


def main():
    input_img_filename = sys.argv[1]
    pixel_scale = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    sys.stdout.writelines(
        ''.join(r) + '\n'
        for r in
        make_text_from_image(input_img_filename, pixel_scale)
    )
    sys.stdout.flush()


if __name__ == '__main__':
    main()