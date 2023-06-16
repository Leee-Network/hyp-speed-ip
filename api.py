import http.server
import socketserver
import subprocess
import json
import requests

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api':
            ping_hypixel = subprocess.run(['ping', '-c', '1', 'mc.hypixel.net'], capture_output=True, text=True)
            ping_china = subprocess.run(['ping', '-c', '1', 'www.baidu.com'], capture_output=True, text=True)
            ping_hypixel_result = float(ping_hypixel.stdout.split('\n')[-3].split(' = ')[-1].split('/')[0])
            ping_china_result = float(ping_china.stdout.split('\n')[-3].split(' = ')[-1].split('/')[0])
            data = {
                'ping_hypixel': ping_hypixel_result,
                'ping_china': ping_china_result,
                'ping_total': ping_hypixel_result + ping_china_result,
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
            super().do_GET()

PORT = 8080

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
