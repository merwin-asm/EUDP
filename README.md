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

server = EUDP.EUDPServer(IP, Port, "key") # client_loop will be called giving args server-obj and client 

server.send(client,msg) # sends msg
server.recv()     # recvs msg
server.close()    # close connection
```

### Client Side
```python
client = EUDP.EUDPClient(IP, Port, "key") 

client.send(msg)  # send msg to server
client.recv()     # recv msg from server
client.close()    # close connection with server

```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@Merwin](https://www.github.com/mastercodermerwin)
