# --------------------------------------------------------------------
# Example Code for Shaping Deffraction Pattern Descriptor Generation
# Licensed under The MIT License
# Written by CSRC, KIST
# --------------------------------------------------------------------
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import natsort
import numpy as np
import os
import sys
from PIL import Image
from Shaped_DP import Shaped_DP


def call_Descriptor(sd, folder, f):
    mp_id = f.split("_")
    filename = str(os.path.join(folder, f))
    img = Image.open(filename)
    img.load()
    data = np.asarray(img, dtype=np.float32)
    img.close()

    lDP = Shaped_DP(data)

    if mp_id[1] == 'x.png':
        result_r = lDP.create_descriptor(1)
        img = Image.fromarray(result_r.astype(np.uint8), 'RGB')
        img.save('Sample Dataset/Sample Result/' + sd + '/x/' + mp_id[0] + '_x.jpg')
    elif mp_id[1] == 'y.png':
        result_r = lDP.create_descriptor(2)
        img = Image.fromarray(result_r.astype(np.uint8), 'RGB')
        img.save('Sample Dataset/Sample Result/' + sd + '/y/' + mp_id[0] + '_y.jpg')
    elif mp_id[1] == 'z.png':
        result_r = lDP.create_descriptor(3)
        img = Image.fromarray(result_r.astype(np.uint8), 'RGB')
        img.save('Sample Dataset/Sample Result/' + sd + '/z/' + mp_id[0] + '_z.jpg')
        print('Sample Dataset/Sample Result/' + sd + '/' + mp_id[0] + ' done!')


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', help='Test dataset path.', default='Sample Dataset')

    return parser.parse_args(argv)


def main(args):
    d = args.test_dir + '/Sample Raw Data'
    direct = os.listdir(d)
    direct.sort()
    sorted(direct)
    print('Generating Descriptor:')

    for sd in direct:
        if os.path.isdir(args.test_dir + '/Sample Result/' + sd) is False:
            os.mkdir(args.test_dir + '/Sample Result/' + sd)
            os.mkdir(args.test_dir + '/Sample Result/' + sd + '/x')
            os.mkdir(args.test_dir + '/Sample Result/' + sd + '/y')
            os.mkdir(args.test_dir + '/Sample Result/' + sd + '/z')

        folder = os.path.join(d, sd)

        if os.path.isdir(folder):
            directFiles = os.listdir(folder)
            files = natsort.natsorted(directFiles)

            for f in files:
                call_Descriptor(sd, folder, f)


if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))
