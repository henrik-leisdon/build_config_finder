import argparse
import os


def parse_args():
    """
    parses input arguments. Valid arguments are:
    -npm: search all npm config files
    -gradle: search all gradle config files
    no arguments: search for NPM and Gradle config files
    :return: arguments
    """
    parser = argparse.ArgumentParser(description="Tool search NPM or Gradle files")
    parser.add_argument("-npm", help="search for NPM files only", action="store_true")
    parser.add_argument("-gradle", help="search for Gradle files only", action="store_true")
    args = parser.parse_args()

    if args.npm is True and args.gradle is True:
        parser.error("Please provide only one or no argument")
    return args


def search_config_files(args):
    """
    search for NPM files, gradle files or both
    """
    if args.npm is True:
        search_npm()

    elif args.gradle is True:
        search_gradle()

    else:
        search_npm()
        search_gradle()


def search_npm():
    """
    search npm files: package.json and package-lock.json
    """
    package = search_file("package.json")
    package_lock = search_file("package.json")
    if package is False and package_lock is False:
        print("Found no NPM package files in the current directory")


def search_gradle():
    """
    search gradle files: build.gradle and
    """
    build_gradle = search_file("build.gradle")
    gradle_props = search_file("gradle.properties")
    if build_gradle is False and gradle_props is False:
        print("Found no Gradle package files in the current directory")


def search_file(filename):
    """
    :param filename: name of file to search in directory
    :return: True if file is found, else False
    """
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            print("Found a {} file in the directory.".format(filename))
            return True
    return False


if __name__ == "__main__":
    args = parse_args()
    search_config_files(args)
