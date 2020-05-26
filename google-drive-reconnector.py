import os
import argparse
import subprocess

import random,string
def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    "--google-drive-dir",
    required=True,
    help="google drive dir(ex.): /media/gdrive",
)
args = parser.parse_args()
print(args)
if args.google_drive_dir:
    mount_dir = str(args.google_drive_dir)
    chk_flag1 = True
    r_text = randomname(12)
    try:
        filepath = "{}/.google-drive-reconnector-fuse_{}".format(mount_dir,r_text)
        fw = open(filepath,"fw",encoding='utf-8')
        fw.write("1")
        fw.close()
        if os.path.exists(filepath):
            os.remove(filepath)
        else:
            chk_flag1 = False
    except:
        chk_flag1 = False
        print("Error, chk_flag1 = False")
        import traceback
        traceback.print_exc()
    if not os.path.exists(mount_dir) and chk_flag1 == False:
        print("{} is not available.".format(mount_dir))
        print("umount -d {}".format(mount_dir))
        subprocess.run("umount -d {}".format(mount_dir), shell=True)
        print("mount -a")
        subprocess.run("mount -a", shell=True)
    else:
        print("{} is available.".format(mount_dir))
