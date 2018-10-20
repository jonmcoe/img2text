import sys

import numpy as np
from PIL import Image


GRAY_CHARS = [' ', '.', ':', '|', '+', '=', '3', '#', '@']  # length must be power of 2 + 1
BOUNDS = list(range(0, 2**8, 2**8 // (len(GRAY_CHARS) - 1)))


def main():
    input_img_filename = sys.argv[1]
    pixel_scale = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    g = (
        (GRAY_CHARS[p - 1] for p in r)  # TODO: consider pixel scale and average the rectangle here
        for r in np.digitize(np.array(Image.open(input_img_filename).convert(mode='L')), BOUNDS)
    )
    # TODO: how to do this smart with iterator and not list cast? (or do above instead, then no need)
    sys.stdout.writelines(''.join(list(r)[::pixel_scale]) + '\n' for r in list(g)[::pixel_scale])
    sys.stdout.flush()


if __name__ == '__main__':
    main()