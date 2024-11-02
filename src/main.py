import asyncio
import utils.utils as utils
import client.client as client
import server.server as server
import generated.service_pb2 as service_pb2
import generated.service_pb2_grpc as service_pb2_grpc


async def main():
    # 取得使用者輸入的連接埠
    print(f"自己的ip: {utils.get_internal_ip()}")
    try:
        port = int(input("請輸入自己的連接埠: "))
        utils.is_valid_port(port)
        other_side_ip = input("請輸入對方的 IP: ")
        other_side_port = int(input("請輸入對方的連接埠: "))
        utils.is_valid_port(other_side_port)
    except ValueError as e:
        print(e)
    
    await asyncio.gather(server.serve(port), client.send_requests(other_side_port,other_side_ip))

if __name__ == "__main__":
    asyncio.run(main())