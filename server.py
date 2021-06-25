from xmlrpc.server import SimpleXMLRPCServer
import datetime

server_ip = "0.0.0.0"
server_port = 8008

with SimpleXMLRPCServer((server_ip, server_port), allow_none=True) as server:
    server.register_introspection_functions()

    class ATMServer:
        def __init__(self):
            self.nasabah = [
                {
                    "nama": "ABC DEF",
                    "nomor_kartu": "1234123412341234",
                    "nomor_rekening": "123123123",
                    "pin": "123456",
                    "saldo": 1000000,
                    "history": [
                        {"tanggal": "01/06/2021", "uraian": "transfer dari ZER LPO", "nominal": 20000},
                        {"tanggal": "04/06/2021", "uraian": "tarik tunai", "nominal": -150000},
                        {"tanggal": "06/06/2021", "uraian": "top up echannel kartu", "nominal": -50000},
                        {"tanggal": "10/06/2021", "uraian": "transfer ke FED CBA", "nominal": -120000},
                        {"tanggal": "10/06/2021", "uraian": "top up echannel", "nominal": -130000},
                        {"tanggal": "17/06/2021", "uraian": "top up gopay", "nominal": -100000},
                        {"tanggal": "20/06/2021", "uraian": "transfer dari LL PAK", "nominal": 56000},
                        {"tanggal": "21/06/2021", "uraian": "top up echannel", "nominal": -250000},
                    ]
                },
                {
                    "nama": "FED CBA",
                    "nomor_kartu": "4321432143214321",
                    "nomor_rekening": "321321321",
                    "pin": "654321",
                    "saldo": 2000000,
                    "history": [
                        {"tanggal": "01/06/2021", "uraian": "biaya administrasi", "nominal": -5000},
                        {"tanggal": "09/06/2021", "uraian": "top up echannel", "nominal": -120000},
                        {"tanggal": "10/06/2021", "uraian": "transfer dari ABC DEF", "nominal": 130000},
                        {"tanggal": "11/06/2021", "uraian": "top up echannel", "nominal": -100000},
                        {"tanggal": "17/06/2021", "uraian": "transfer ke POPLO", "nominal": -20000},
                        {"tanggal": "20/06/2021", "uraian": "top up shopeepay", "nominal": -350000},
                    ]
                },
            ]
