import grpc
import asyncio
import utils.utils as util
import generated.service_pb2_grpc as service_pb2_grpc
import generated.service_pb2 as service_pb2


async def send_requests(port,ip):
    ip = util.get_internal_ip()
    async with grpc.aio.insecure_channel(f"{ip}:{port}") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        while True:
            user_input = await asyncio.to_thread(input, "請輸入數據: ")
            if user_input.lower() == "exit":
                print("結束輸入")
                break
            try:
                await stub.SendData(service_pb2.Request(message=user_input))
                # print(f"Client 收到回應: {response.reply}")
            except grpc.aio.AioRpcError as e:
                print(f"請求錯誤: {e.code()} - {e.details()}")