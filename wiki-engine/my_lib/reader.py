

def read_file_to_string_list(file_path):
    with open (file_path, "r") as file_stream:
        data = file_stream.readlines()
    return data

def read_file_to_string(file_path):
    string_list = read_file_to_string_list(file_path)
    res_string = ''
    for line in string_list:
        res_string += line
    return res_string
