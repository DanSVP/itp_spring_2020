def read_complete_file(file_path):
    with open(file_path) as fh: #default for "with" is in r mode
        return fh.read()