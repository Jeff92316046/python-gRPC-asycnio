import os

os.system(
    """ python -m grpc_tools.protoc -I./src/protos/ \
        --python_out=./src/generated \
        --grpc_python_out=./src/generated \
        ./src/protos/*.proto"""
)