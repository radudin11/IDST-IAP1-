#!.venv/bin/python3

import argparse         # argument parsing
import struct           # data unpacking
from PIL import Image   # image processing

def main():
    # parse cli arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', help='input image file')
    parser.add_argument('--dst', help='data destination',
                        default='/dev/fb0', metavar='/dev/fb*')
    parser.add_argument('--width', help='screen width [px]',
                        type=int, default=1920, metavar=' INT')
    parser.add_argument('--height', help='screen height [px]',
                        type=int, default=1080, metavar='INT')
    parser.add_argument('--hoff', help='horizontal offset [px]',
                        type=int, default=0, metavar='INT')
    parser.add_argument('--voff', help='vertical offset [px]',
                        type=int, default=0, metavar='INT')

    cfg = parser.parse_args()

    img = Image.open(cfg.FILE)
    frameBuffer = open(cfg.dst, "wb")
    
    alpha = 1
    data = img.load()
    for i in range(cfg.width - cfg.hoff):
        for j in range(cfg.height- cfg.voff):
            frameBuffer.write( (int(data[i, j][2])).to_bytes(1, "little"))
            frameBuffer.write( (int(data[i, j][1])).to_bytes(1, "little"))
            frameBuffer.write( (int(data[i, j][0])).to_bytes(1, "little"))
            frameBuffer.write(alpha.to_bytes(1, "little"))
    img.close()
    frameBuffer.close()

if __name__ == '__main__':
    main()