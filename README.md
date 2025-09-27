# System-Monitor
Parfait ✅ je vais te générer un **README.md** clair et bien structuré pour ton projet **System Monitor**.
Voici une première version :

````markdown
# 🖥️ System Monitor

System Monitor is a lightweight web application built with **Python (Flask)** and **HTML** that lets you **view your PC’s key system information in real time**.

It displays:
- 🧮 CPU usage (%)
- 🗂️ RAM (total & used, in GB)
- 💾 Disk space (total & used, in GB)
- 🌐 Hostname & IP address
- 🖥️ Operating system (name & version)

---

## 🚀 Features
- Simple and lightweight interface
- Real-time system resource monitoring
- Runs locally on your machine
- Extensible (easy to add more metrics like network usage, temperature, etc.)

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Gston45/System-Monitor.git
cd System-Monitor
````

### 2. Install dependencies

```bash
pip install flask psutil
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in your browser

Go to: [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
System-Monitor/
│── app.py              # Main Flask application
│── templates/
│   └── index.html      # Frontend HTML template
│── README.md           # Documentation
```

---

## 🖼️ Example Output

When running the app, you’ll see a dashboard like:

| Metric     | Value           |
| ---------- | --------------- |
| CPU Usage  | 12 %            |
| RAM Used   | 4.5 GB / 8 GB   |
| Disk Used  | 120 GB / 256 GB |
| Hostname   | MyComputer      |
| IP Address | 192.168.1.10    |
| OS         | Windows 11      |

---

## 🔮 Future Improvements

* Auto-refresh with JavaScript (live updates without reloading)
* Add charts for CPU & memory usage
* Monitor network activity (upload/download)
* Export system info as JSON/CSV
* Notifications on high resource usage

---

## 📜 License

This project is licensed under the MIT License.
Feel free to use and improve it! 🚀
