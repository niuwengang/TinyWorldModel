import sys



def main():
    print("Welcome to TinyWorldModel!")


if __name__ == "__main__":
    if sys.version_info < (3, 12):
        raise RuntimeError("This program requires Python 3.12 or higher.")
    main()