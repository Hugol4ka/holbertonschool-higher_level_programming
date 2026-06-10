#!/usr/bin/python3

import http.server
import json

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    
   def do_GET(self):
        # Route 1 : La racine du site "/"
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API!".encode("utf-8"))
            
        elif self.path == "/data":
            self.send_response(200)
            # On change le Content-type pour du JSON !
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            # Notre dictionnaire
            sample_data = {"name": "John", "age": 30, "city": "New York"}
            # On le transforme en texte JSON avec la fonction json.dumps
            json_string = json.dumps(sample_data)
            # On l'envoie au client
            self.wfile.write(json_string.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("OK".encode("utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Endpoint not found".encode("utf-8"))

if __name__ == '__main__':
    # On définit l'adresse et le port (8000)
    server_address = ('', 8000)
    
    # On crée le serveur HTTP en lui associant notre SimpleAPIHandler
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    
    print("Serveur lancé sur http://localhost:8000 ...")
    
    # On dit au serveur de tourner en boucle sans s'arrêter
    httpd.serve_forever()