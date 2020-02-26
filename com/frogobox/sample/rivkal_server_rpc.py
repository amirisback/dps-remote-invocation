# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler 
class RequestHandler(SimpleXMLRPCRequestHandler):
    # batasi pada path /RPC2 saja
    rpc_paths = ('/RPC2',)

# buat server serta register fungsi register_introspection_functions()
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    # Buatlah fungsi kalkulasi dasar (tambah, kurang, kali, bagi, pangkat), 
    # anda dapat memilih ataupun menggunakan ketiga cara berikut:
    # cara 1 untuk memasukkan fungsi dalam server adalah dengan langsung memasukkan namanya
    # fungsi pow() merupakan fungsi build in pada pyhton, tinggal dipanggil saja
    

    # cara 2 untuk register fungsi: buat fungsinya kemudian register
    # a. buat fungsi
    def tambah(x,y):
        return x + y

    def kali(x,y):
        return x*y

    def bagi(x,y):
        return x/y

    def kurang(x,y):
        return x - y

    def pangkat(x,y):
        return pow(x,y)
    # b. register fungsinya
    
    # cara 3: tidak hanya fungsi, class juga bisa diregisterkan
    server.register_function(tambah, 'tambah')
    server.register_function(kali, 'kali')
    server.register_function(bagi, 'bagi')
    server.register_function(kurang, 'kurang')
    server.register_function(pangkat, 'pangkat')
    # jalankan server
    server.serve_forever()
    