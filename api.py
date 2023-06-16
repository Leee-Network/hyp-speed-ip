import http.server
import socketserver
import subprocess
import json
import requests
import socket
import time

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api':
            ping_hypixel = ping('mc.hypixel.net')
            ping_china = ping('www.baidu.com')
            data = {
                'ping_hypixel': ping_hypixel,
                'ping_china': ping_china,
                'ping_total': ping_hypixel + ping_china,
                'public_ip': '',
                'location': ''
            }
            r = requests.get('https://ifconfig.me/all.json')
            if r.status_code == 200:
                result = r.json()
                data['public_ip'] = result['ip_addr']
                data['location'] = result['city'] + ', ' + result['country']
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_error(404, 'Not Found')

def ping(host):
    start_time = time.time()
    try:
        socket.gethostbyname(host)
    except socket.error:
        return -1
    else:
        end_time = time.time()
        return int((end_time - start_time) * 1000)

PORT = 8080

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
