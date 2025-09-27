from flask import Flask, render_template
import psutil, platform, socket

app = Flask(__name__)

def get_system_info():
    return {
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "os": platform.system() + " " + platform.release(),
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_total": round(psutil.virtual_memory().total / (1024**3), 2),
        "ram_used": round(psutil.virtual_memory().used / (1024**3), 2),
        "disk_total": round(psutil.disk_usage('/').total / (1024**3), 2),
        "disk_used": round(psutil.disk_usage('/').used / (1024**3), 2)
    }

@app.route("/")
def index():
    info = get_system_info()
    return render_template("index.html", info=info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
