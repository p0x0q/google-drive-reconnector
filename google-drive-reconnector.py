import os
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "--google-drive-dir",
    nargs="+",
    required=True,
    help="google drive dir(ex.): /media/gdrive",
)
args = parser.parse_args()

if args.google_drive_dir:
    if not os.path.exists(args.google_drive_dir):
        subprocess.run("umount -d {}".format(args.google_drive_dir), shell=True)
        subprocess.run("mount -a", shell=True)
