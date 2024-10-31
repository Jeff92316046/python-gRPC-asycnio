import grpc
import generated.message_pb2_grpc as pb2_grpc
import generated.message_pb2 as pb2
class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8787

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            f'{self.host}:{self.server_port}')

        # bind the client and the server
        self.stub = pb2_grpc.MessageSenderStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        data = pb2.Message(message=message)
        return self.stub.GetMessageResponse(data)