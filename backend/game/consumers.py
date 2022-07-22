from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GameConsumer(AsyncWebsocketConsumer):
    ## conect
    async def connect(self):
        ## connect the user to the game group
        self.game_id = self.scope['url_route']['kwargs']['game_id']
        await self.channel_layer.group_add(
            self.game_id,
            self.channel_name,

        )

        
        await self.accept()
    ## disconnect
    async def disconnect(self, close_code):
        ## disconnect the user from the game group
        await self.channel_layer.group_discard(
            self.game_id,
            self.channel_name
        )
    ## receive messages from the frontend
    async def receive(self, text_data):
        payload_json = json.loads(text_data)

    

        ## Send message to each user in the group based on what received
        if payload_json['method'] == "click":
            data = payload_json['data']
            await self.channel_layer.group_send(
                self.game_id,
                {
                    'type': 'send_click',
                    'data': data
                }
            )



    ## handlers

    ## click method handler
    async def send_click(self, event):
        data = event['data']

        ## Send message to WebSocket
        await self.send(text_data=json.dumps({
            'method':'click',
            'data': data
        }))