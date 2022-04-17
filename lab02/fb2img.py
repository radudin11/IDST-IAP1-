#!.venv/bin/python3

import argparse         # argument parsing
import struct           # data unpacking
from PIL import Image   # image processing

def main():
    # parse cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help='output image file')
    parser.add_argument('--src', help='data source',
                        default='/dev/fb0', metavar='/dev/fb*')
    parser.add_argument('--width', help='screen width [px]',
                        type=int, default=1920, metavar=' INT')
    parser.add_argument('--height', help='screen height [px]',
                        type=int, default=1080, metavar='INT')
    cfg = parser.parse_args()

    # TODO 1: read contents of cfg.src (the frame buffer)
    frameBuff = open(cfg.src, "rb")
    # TODO 2: split data in groups of 4 bytes
    
    # create a new PIL Image object
    img = Image.new('RGB', (cfg.width, cfg.height))
    px  = img.load()

    # set each pixel value
    for i in range(cfg.width):
        for j in range(cfg.height):
            # TODO 3: write each pixel value in px[i,j] as a RGB tuple
            # NOTE  : the four bytes in the groups that you split previously
            #         are in fact in BGRA format; we don't need the Alpha
            #         value but the other three bytes must be revered
            blue = int.from_bytes(frameBuff.read(1), "little")
            red = int.from_bytes(frameBuff.read(1), "little")
            green = int.from_bytes(frameBuff.read(1), "little")
            alpha = int.from_bytes(frameBuff.read(1), "little")

            px[i, j] = (red ,green, blue) 
    
    # save image do disk
    # NOTE: format will be determined from the file's extension
    img.save(cfg.FILE, None)

    # clean up PIL Image object
    img.close()

if __name__ == '__main__':
    main()