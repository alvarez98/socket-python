import socketio
import eventlet
import eventlet.wsgi
from flask import Flask
from flask import render_template

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.hbs')

# with Namespaces
@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

# send data to specific client
@sio.on('rpi message')
def message(sid, data):
    sio.emit('chat_message',data={'data': 'hola'})
    print("message ", data)

# # without Namespaces, send data to all clients
# @sio.on('everybody')
# def metrics(sid, metrics):
#     from random import random
#     sio.emit('metrics', { 'metrics': random() })
#     print("message ", metrics)

# listen disconnections
@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
