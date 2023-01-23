# EUDP

Encrypted UDP

<p align="right"> <img src="https://komarev.com/ghpvc/?username=merwin-eudp&label=Project%20views&color=0e75b6&style=flat" alt="darkmash-org" /> </p>

<hr>

## Install

      pip install EUDP
      
      
## Features

- Cross platform (i think)
- RSA and AES Encryption


## Usage/Examples

```python
import EUDP

```


### Server Side
```python

def client_loop(server,cli):
  pass # do stuff

server = pyE2EE.Server(port,client_loop) # client_loop will be called giving args server-obj and client 

server.TotalCons        # gives number of total connections
server.clients          # is a list of all [client, AES-key-of-the-cli]
server.send(client,msg) # sends msg
server.recv(client)     # recvs msg
server.sendall(msg)     # send all connected clients
server.close(client)    # close a connection
```

### Client Side
```python
client = pyE2EE.Client(server_ip,port) 

client.send(msg)  # send msg to server
client.recv()     # recv msg from server
client.close()    # close connection with server

```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@Merwin](https://www.github.com/mastercodermerwin)
