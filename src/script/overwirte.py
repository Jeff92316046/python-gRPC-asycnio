import os
import re

def traverse_folder(folder_path):
    items = os.listdir(folder_path)
    find_grpc_file = []
    for i in items:
        if re.search("grpc",i)!= None:
            find_grpc_file.append(i)
    return find_grpc_file

def open_and_overwrite(file_name_list):
    print(file_name_list)
    for i in file_name_list:
        print(os.path.join(os.getcwd(),f'src{os.sep}generated{os.sep}{i}'))
        with open(os.path.join(os.getcwd(),f'src{os.sep}generated{os.sep}{i}'),"r") as file:
            lines = file.readlines()
        for jndex,j in enumerate(lines):
            if re.match(r'import (.*)_pb2 as (.*)__pb2*',j) != None:
                lines[jndex] = 'from . ' + lines[jndex]
        with open(os.path.join(os.getcwd(),f'src{os.sep}generated{os.sep}{i}'),"w") as file:
            file.writelines(lines)
