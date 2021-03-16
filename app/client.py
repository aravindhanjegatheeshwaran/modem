from websocket import create_connection
import asyncio
import websockets
import json



class SocketServer():
    def datasend(a):
        try:
            ws=create_connection("ws://localhost:7000")
            print(a)
            ws.send(json.dumps(a))
            while True:
                result = ws.recv()
                result=json.loads(result)
                print(result)
        except Exception as e:
            print(e)
        return result
    
    def message(conname,com,li, msg, name, limit):
        try:
            dic={}
            dic.setdefault("data",[]).append(conname)
            dic.setdefault("data",[]).append(com)
            dic.setdefault("data",[]).append(li)
            dic.setdefault("data",[]).append(msg)
            dic.setdefault("data",[]).append(name)
            dic.setdefault("data",[]).append(limit)
            sms="multisms"
            ws=create_connection("ws://localhost:7000")
            ws.send(json.dumps(sms))
            result1 = ws.recv()
            result1=json.loads(result1)
            print(dic)
            ws.send(json.dumps(dic))
            result = ws.recv()
            result=json.loads(result)
            print(result)
        except Exception as e:
            print(e)
        return result1





























#     def __init__(self):
#         self.all_conn = set()
#         self.local_client_conn_list = []
#         self.web_client_conn_list = []
#         self.connReqResp = {
#             "internalComm": {
#                 'action': 'localClientComm',
#                 'token': "",
#                 'command': "",
#                 'msg': ""
#             },
#             "webClientComm": {
#                 'action': 'webClientComm',
#                 'token': "",
#                 'command': "",
#                 'msg': ""
#             }
#         }
    

#         # - Manage Incoming Conn
#     async def register(self, websocket):
#         self.all_conn.add(websocket)
#         print(f"Client - {websocket.remote_address} connected")

#      # - Manage Closed Conn or Failed Conn
#     async def unregister(self, websocket):
#         self.all_conn.remove(websocket)

#         # - Manage Incoming Local Client Conn List of Users
#     async def localClientList(self, websocket, data):
#         # print("++++++++++localClientList+++++++++++++")
#         # - If client not present, then add
#         #- Check whether client connection already persist or not
#         # - <Need to check self.all_conn>
#         if self.local_client_conn_list == []:
#             payload = {'socketData':websocket, 'token':data['token']}
#             self.local_client_conn_list.append(payload)
#         else:
#             for localClient in self.local_client_conn_list:
#                 if localClient['token'] != data['token']:
#                     payload = {'socketData':websocket, 'token':data['token']}
#                     self.local_client_conn_list.append(payload)
#         # print(self.local_client_conn_list)
#         # print("++++++++++++++++++++++++++++++++++++++")

#     # - Manage Incoming Web Client Conn List of Users
#     async def webClientList(self, websocket, data):
#         # print("++++++++++webClientList+++++++++++++")
#         # - If client not present, then add
#         #- Check whether client connection already persist or not
#         # - <Need to check self.all_conn>
#         if self.web_client_conn_list == []:
#             payload = {'socketData':websocket, 'token':data['token']}
#             self.web_client_conn_list.append(payload)
#         else:
#             for webClient in self.web_client_conn_list:
#                 if webClient['token'] != data['token']:
#                     payload = {'socketData':websocket, 'token':data['token']}
#                     self.web_client_conn_list.append(payload)
#         # print(self.web_client_conn_list)
#         # print("++++++++++++++++++++++++++++++++++++++")

#     # - Send Message from Local Client To Web Client
#     async def localToWebMsg(self, websocket, data):
#         # print("++++++++++localToWebMsg+++++++++++++")
#         # print(self.web_client_conn_list)
#         # print("+++++++++++middlesssss++++++++++++++++")
#         # - Check for respective web client
#         webClient = ''
#         for webClientUser in self.web_client_conn_list:
#             if webClientUser['token'] == data['token']:
#                 webClient = webClientUser['socketData']
#         # print(webClient)
#         # print("++++++++++++++++++++++++++++++++++++++")
#         if webClient != '':
#             await webClient.send(json.dumps(data))
    
#     # - Send Message from Web Client To Local Client
#     async def webToLocalMsg(self, websocket, data):
#         # print("++++++++++webToLocalMsg+++++++++++++")
#         # print(self.local_client_conn_list)
#         # print("+++++++++++middlesssss++++++++++++++++")
#         # - Check for respective local client
#         localClient = ''
#         for localClientUser in self.local_client_conn_list:
#             if localClientUser['token'] == data['token']:
#                 localClient = localClientUser['socketData']
#         # print(localClient)
#         # print("++++++++++++++++++++++++++++++++++++++")
#         if localClient != '':
#             await localClient.send(json.dumps(data))

#     # - Create message payloads
#     def generatePayload(self, payloadData=[]):
#         if payloadData != []:
#             self.connReqResp[payloadData[0]]['command'] = payloadData[1]
#             self.connReqResp[payloadData[0]]['msg'] = payloadData[2]
#             return json.dumps(self.connReqResp[payloadData[0]])
#         return False

#      # - Initiate connections
#     async def startConn(self, websocket, path):
#         # - Register local and web clients
#         await self.register(websocket)
#         try:
#             async for message in websocket:
#                 data = json.loads(message)
#                 # print(f"1. data-----{data}")
#                 if data['action'] == "register":
#                     # print('2. register ----------')
#                     await self.localClientList(websocket, data)
#                     payload = json.dumps({'action':"serverResp", 'status':'u r connected!'})
#                     # print(f'2. register payload------{payload}')
#                     await websocket.send(payload)
#                 elif data['action'] == "webclientregister":
#                     # print('3. webclientregister ----------')
#                     await self.webClientList(websocket, data)
#                     payload = json.dumps({'action':"serverResp", 'status':'u r connected!'})
#                     # print(f'3. webclientregister payload------{payload}')
#                     await websocket.send(payload)
#                 elif data['action'] == "webClientComm":
#                     # print('4. webClientComm ----------')
#                     await self.localToWebMsg(websocket, data)
#                 elif data['action'] == "localClientComm":
#                     # print('5. localClientComm ----------')
#                     await self.webToLocalMsg(websocket, data)
#                 else:
#                     print("no Resp matches!")
#         except:
#             print('Exception dream')
#         finally:
#             pass

# # - Run infinite loop for persisting connection of socket
# ws= create_connection("ws://127.0.0.1:7000")
# print('Server Started and Running...')
# SocketServer(ws)





