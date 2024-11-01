import os
import overwirte

os.system(
    """ python -m grpc_tools.protoc -I./src/protos/ \
        --python_out=./src/generated \
        --grpc_python_out=./src/generated \
        ./src/protos/*.proto"""
)


folder_path =  os.path.join(os.getcwd(),f"src{os.sep}generated")

overwirte.open_and_overwrite(overwirte.traverse_folder(folder_path))
