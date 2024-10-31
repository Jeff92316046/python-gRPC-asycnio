from concurrent import futures
from generated.message_pb2 import (
    Message,
    MessageResponse
)
import generated.message_pb2_grpc as message_pb2_grpc
import grpc

class MessageSender(message_pb2_grpc.MessageSender):
    def __init__(self):
        pass

    def GetMessageResponse(self, request, context):

        # get the string from the incoming request
        message = request.message
        result = f'received `{message}` message from you'
        print(result)
        return MessageResponse(message=result)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageSenderServicer_to_server(MessageSender(), server)
    server.add_insecure_port('[::]:8787')
    server.start()
    server.wait_for_termination()

