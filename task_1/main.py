from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class CalcHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(405)
        self.end_headers()
        response = json.dumps({"error": "Method Not Allowed"})
        self.wfile.write(response.encode('utf-8'))
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
            a = float(data['A'])
            b = float(data['B'])
            path = self.path
            match path:
                case '/add/':
                    answer = a + b
                case '/subtract/':
                    answer = a - b
                case '/multiply/':
                    answer = a * b
                case '/divide/':
                    if b != 0:
                        answer = a / b
                    else:
                        self.send_response(400)
                        self.end_headers()
                        response = json.dumps({"error": "Division by zero!"})
                        self.wfile.write(response.encode('utf-8'))
                        return
                case _:
                    self.send_response(400)
                    self.end_headers()
                    response = json.dumps({"error": "400"})
                    self.wfile.write(response.encode('utf-8'))
                    return
            response = json.dumps({'answer': answer})
            self.send_response(200)
            self.end_headers()
            self.wfile.write(response.encode('utf-8'))
        except:
            self.send_response(400)
            self.end_headers()
            response = json.dumps({'error': 'invalid data'})
            self.wfile.write(response.encode('utf-8'))
        
        

if __name__ == '__main__':
    server_address = ('localhost', 8000)
    url = HTTPServer(server_address, CalcHandler)
    url.serve_forever()
