"""Creates a project skeleton for a new python project, per the recommended steps
in Learn Python the Hard Way Exercise #46 (http://learnpythonthehardway.org/book/ex46.html)"""

from __future__ import print_function

import argparse
import os

from scaffold import projectfiles
from scaffold import projectfolders


parser = argparse.ArgumentParser(
    description='Scaffolding tool for simple Python projects',
    epilog='Report any issues to [Github url]',
)
parser.add_argument(
    '-p',
    '--project',
    required=True,
    nargs=1,
    help='The name of the project to create',
)
parser.add_argument(
    '-d',
    '--dir',
    required=False,
    nargs=1,
    help='The directory in which to create the project (creates in current directory by default)',
)

args = parser.parse_args()  # Unpack the commandline arguments

# Get the current working directory as our default root project directory
target_dir = os.getcwd()

if args.dir is not None:  # If the user set an explicit output directory
    target_dir = args.dir[0]


def main():
    try:
        # Creates all of the project folders we need
        projectfolders.create_folders(args.project[0], target_dir)
        # Creates all of the project files we need
        projectfiles.create_files(args.project[0], target_dir)
    except IOError as e:
        print(e)

if __name__ == "__main__":
    main()
