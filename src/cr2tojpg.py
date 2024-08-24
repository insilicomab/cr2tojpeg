from argparse import ArgumentParser
from pathlib import Path

import cv2
import rawpy
from tqdm import tqdm


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-p", "--photo_dir", default="inputs")
    parser.add_argument("-o", "--output_dir", type=str, default="outputs")
    parser.add_argument("-e", "--extension", default="CR2")
    args = parser.parse_args()
    return args


def main(args):
    photo_dir = Path(args.photo_dir)

    photo_list = [file for file in photo_dir.glob(f"*.{args.extension}")]
    print(f"number of {args.extension} file: {len(photo_list)}")

    for photo_path in tqdm(photo_list):

        raw = rawpy.imread(str(photo_path))

        decoded = raw.postprocess()[:, :, [2, 1, 0]]

        basename = Path(photo_path).stem
        outfile = Path(args.output_dir) / f"{basename}.jpeg"

        cv2.imwrite(outfile, decoded)  # opencvでjpgを出力


if __name__ == "__main__":
    args = parse_args()
    main(args)
