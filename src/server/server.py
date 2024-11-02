import grpc
import utils.utils as util
import generated.service_pb2 as service_pb2
import generated.service_pb2_grpc as service_pb2_grpc


class ExampleService(service_pb2_grpc.ExampleServiceServicer):
    async def SendData(self, request, context):
        print(f"\rServer 收到數據: {request.message}\n請輸入數據: ",end='')
        return service_pb2.Response(reply="已收到: " + request.message)
    
async def serve(port):
    server = grpc.aio.server()
    service_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    ip = util.get_internal_ip()
    server.add_insecure_port(f"{ip}:{port}")
    await server.start()
    await server.wait_for_termination()