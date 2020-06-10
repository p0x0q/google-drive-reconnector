import os
import argparse
import subprocess

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
print(args)
if args.google_drive_dir:
    mount_dir = str(args.google_drive_dir)
    if not os.path.exists(mount_dir):
        print("{} is not available.".format(mount_dir))
        print("umount -d {}".format(mount_dir))
        subprocess.run("umount -d {}".format(mount_dir), shell=True)
        subprocess.run("fusermount -u  {}".format(mount_dir), shell=True)
        print("mount -a")
        subprocess.run("mount -a", shell=True)
    else:
        print("{} is available.".format(mount_dir))
