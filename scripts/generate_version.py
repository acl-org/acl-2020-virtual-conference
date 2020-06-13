import json
import subprocess
import sys
from time import strftime


def getVersionInfo():
    now = strftime("%Y-%m-%d %H:%M:%S")
    # If we would like the short form, add '--short' option
    # sha = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"])
    # For Python3, convert bytes to str
    if isinstance(sha, bytes):
        sha = sha.decode()
    sha = sha.strip()
    version = {"date": now, "sha": sha}
    json_string = json.dumps(version, indent=4)
    return json_string


def showUsage():
    print("Usage: python[3] %s output_file" % sys.argv[0])


def writeFile(path, string):
    f = open(path, "w")
    f.write(string)
    f.close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
    else:
        showUsage()
        exit()

    json_string = getVersionInfo()
    writeFile(file_path, json_string)
