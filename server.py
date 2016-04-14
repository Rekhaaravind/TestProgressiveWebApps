#!C:\Python34\python.exe
import http.server
import socketserver
import mimetypes

PORT = 3000

Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map['.appcache']='text/cache-manifest'
httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()
