import asyncio
import grpc
import generated.service_pb2 as service_pb2
import generated.service_pb2_grpc as service_pb2_grpc

# Server Implementation
class ExampleService(service_pb2_grpc.ExampleServiceServicer):
    async def SendData(self, request, context):
        print(f"\rServer 收到數據: {request.message}\n請輸入數據: ",end='')
        return service_pb2.Response(reply="已收到: " + request.message)

async def serve(port):
    server = grpc.aio.server()
    service_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    server.add_insecure_port(f"[::]:{port}")
    print(f"gRPC 服務啟動在埠號 {port}")
    await server.start()
    await server.wait_for_termination()

# Client Implementation
async def send_requests(port):
    async with grpc.aio.insecure_channel(f"localhost:{port}") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        while True:
            user_input = await asyncio.to_thread(input, "請輸入數據: ")
            if user_input.lower() == "exit":
                print("結束輸入")
                break

            try:
                response = await stub.SendData(service_pb2.Request(message=user_input))
                # print(f"Client 收到回應: {response.reply}")
            except grpc.aio.AioRpcError as e:
                print(f"請求錯誤: {e.code()} - {e.details()}")

async def main():
    # 取得使用者輸入的連接埠
    port = input("請輸入連接埠 (50051 或 50052): ")
    try:
        port = int(port)
        if port not in [50051, 50052]:
            raise ValueError
    except ValueError:
        print("請輸入有效的連接埠號 (50051 或 50052)")
        return

    # 根據連接埠選擇 server 或 client
    if port == 50051:
        await asyncio.gather(serve(port), send_requests(50052))
    else:
        await asyncio.gather(serve(port), send_requests(50051))

if __name__ == "__main__":
    asyncio.run(main())
