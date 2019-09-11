def h():
    pass
def g():
    pass
def m1():
    pass
def m2():
    pass


""" 
WebSockets

send()
receive()
connect()
close()
join_group()
exit_group()

connection
    - accept()
    - reject()
    - id

connection_id (proxy to connection.id)
"""

class WebsocketConnection():
    def accept(self):
        pass
    def reject(self):
        pass

    @property
    def id(self):
        return ''

class WebSocket():
    def __init__(self):
        self.connection = WebsocketConnection()
    def send(self, msg):
        pass
    def receive(self, msg):
        pass
    def connect(self):
        pass
    def close(self):
        pass

    def join_group(self, group_name, cb=send):
        pass 

    def exit_group(self, group_name):
        pass

    

class FooSocket(WebSocket):
    def connect(self, req):
        self.connection.accept()
        room = f'room-{req.params["id"]}'
        self.join_group(room)
        self.join_group('general-bcast', self.custom_bcast_cb)
    
    def receive(self, msg):
        self.send({'okie': 'dokie'})

        if msg['payload'] == 'disconnect':
            self.exit_group('general-bcast')
    
    def close(self):
        pass

    def custom_bcast_cb(self, msg):
        msg['more'] = 'custom behavior'
        self.send(msg)
    

http_config = {
    'routing': {
        'api/v1': {
            'middle': [m1, m2],
            'handler': h,
            '/': {
                'stores': {
                    'handler': h,
                    '/': {
                        '$': {
                            'param_name': 'id',
                            'pattern': r'/d+',
                            'type': str,
                            'handler': { 'get': h, 'post': h },
                            '/': {
                                'destroy': { 'handler': h } 
                            }
                        }
                    }
                },
                'gadgets': {
                    'handler': g,
                }
            }
        }
    }
}

ws_config = {
    'routing': {
        'ws/v1': {
            '/': {
                'chatroom': {
                    'handler': FooSocket,
                    '/': {
                         '$': {
                            'param_name': 'room_id',
                            'handler': FooSocket
                        }
                    }
                }
            }
        }
    }
}

def f1(evt):
    pass
def f2(evt):
    pass

subscriptions = {
    'topic_a': [
        f1, 
        {
            'handler': f2,
            'machine_type': 'n2-standard-l2',
        }
    ],
}