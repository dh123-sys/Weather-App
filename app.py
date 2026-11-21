
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

def find_temperature(city):
    with open("temperatures.txt", "r", encoding="utf-8") as file:
        for line in file:
            if "," in line:
                name, temp = line.strip().split(",", 1)
                if name.lower() == city.lower():
                    return {"found": True, "city": name, "temperature": temp}

    return {"found": False}


class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/temperature?city="):
            city = self.path.split("city=")[1]
            result = find_temperature(city)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(result).encode())
        else:
            super().do_GET()


print("Server chalu hai: http://localhost:8000")
HTTPServer(("", 8000), Handler).serve_forever()
