import os

os.system(
    "python -m grpc_tools.protoc -I./protos/ \\\n"
    "    --python_out=./generated \\\n"
    "    --grpc_python_out=./generated \\\n"
    "    ./protos/*.proto"
)