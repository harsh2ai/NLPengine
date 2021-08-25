import ast

def read_txt_files(file_path):
    data = open(file_path, "r", encoding="utf8", errors='replace').read()
    return data

def get_dict_from_txt(file_path):
    file = open(file_path, "r")
    contents = file.read()
    dictionary = ast.literal_eval(contents)
    file.close()
    return dictionary
