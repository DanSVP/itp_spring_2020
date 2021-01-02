import sys
from file_handling import read_complete_file

def main(filepath):
    print(read_complete_file(filepath))

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 1:
        main(args[0])
    else:
        print("too many/few args, should just be the file path")