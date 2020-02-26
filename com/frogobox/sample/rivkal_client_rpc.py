# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

# buat stub/skeleton (proxy) pada client
s = xmlrpc.client.ServerProxy('http://localhost:8000')

# panggil fungsi kalkulasi dasar (tambah, kurang, kali, bagi, pangkat) yang ada di komputer remote 
print(s.tambah(2,3))
print(s.kurang(2,3))
print(s.kali(2,3))
print(s.bagi(2,3))
print(s.pangkat(2,3))
# print semua fungsi yang ada di komputer remote 
print(s.system.listMethods())
