import read_file


content = read_file.read_file_safe("nonexistent.txt")
if content is None:
    print("Reading file failed.")