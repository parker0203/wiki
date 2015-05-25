

def read_md(file_path):
    with open (file_path, "r") as md_file:
        data = md_file.readlines()

    return data
