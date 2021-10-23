import os
import argparse

from PIL import Image
import imagehash


def parse_args():
    parser = argparse.ArgumentParser(description='image-duplicate-check')
    parser.add_argument('img_dir', help='img dir')
    return parser.parse_args()


args = parse_args()
userpath = args.img_dir

image_files = []
f = [os.path.join(userpath, path) for path in os.listdir(userpath)]
for i in f:
    if i.endswith('.jpg') or i.endswith('.png'):
        image_files.append(i)

imgs = {}
for img in sorted(image_files):
    hash = imagehash.average_hash(Image.open(img))
    if hash in imgs:
        print('Similar image :', img, imgs[hash])
    else:
        imgs[hash] = img
