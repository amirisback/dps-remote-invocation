# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler
from com.frogobox.config import *


class RequestHandler(SimpleXMLRPCRequestHandler):
    # batasi pada path /RPC2 saja
    rpc_paths = (BASE_CONFIG_PATH)


# buat server serta register fungsi register_introspection_functions()
rpcServer = SimpleXMLRPCServer((BASE_CONFIG_IP_ADDRESS, BASE_CONFIG_PORT), requestHandler=RequestHandler)
rpcServer.register_introspection_functions()


# Buatlah fungsi kalkulasi dasar (tambah, kurang, kali, bagi, pangkat),
# anda dapat memilih ataupun menggunakan ketiga cara berikut:
# cara 1 untuk memasukkan fungsi dalam rpcServer adalah dengan langsung memasukkan namanya
# fungsi pow() merupakan fungsi build in pada pyhton, tinggal dipanggil saja

# cara 2 untuk register fungsi: buat fungsinya kemudian register
# a. buat fungsi
def plusMath(number1, number2):
    return number1 + number2


def minusMath(number1, number2):
    return number1 - number2


def multipleMath(number1, number2):
    return number1 * number2


def divideMath(number1, number2):
    return number1 / number2


def powMath(number1, number2):
    return pow(number1, number2)


# b. register fungsinya
# cara 3: tidak hanya fungsi, class juga bisa diregisterkan
rpcServer.register_function(plusMath, 'plusMath')
rpcServer.register_function(multipleMath, 'multipleMath')
rpcServer.register_function(divideMath, 'divideMath')
rpcServer.register_function(minusMath, 'minusMath')
rpcServer.register_function(powMath, 'powMath')
# jalankan server
rpcServer.serve_forever()
