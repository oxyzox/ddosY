# 💣 ddosY - DDoS Attack Tool 🚀

**ddosY** is a customizable tool designed for simulating DDoS (Distributed Denial of Service) attacks. It allows you to send HTTP requests to a target server with options like fake IPs, attack limits, and multi-threading for high-speed attacks.

⚠️ **WARNING:** This tool is for educational purposes only. Unauthorized DDoS attacks are illegal and unethical. Use it responsibly.

---

## 🚀 Features

- 💻 **Multi-Threading Support**: Launch multiple threads to simulate heavy traffic.
- 🌍 **Customizable Fake IP**: Option to spoof the IP address of requests.
- 🛠️ **Configurable Attack Parameters**: Customize target IP, port, attack count, and thread count.
- 💥 **Real-Time Attack Status**: Live updates on attack progress and stats.

---

## 🔧 Setup Guide

### Prerequisites

Before you start, ensure you have the following:

- 🐍 **Python 3.8+**: [Download here](https://www.python.org/downloads/)
- 📦 **Required Python Libraries**: Install necessary libraries using `pip`
    - `socket`
    - `threading`
    - `os`

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/ddoY.git
    cd ddoY
    ```

2. **Install dependencies** (Optional):

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the tool**:

    Start the tool by running:

    ```bash
    python main.py
    ```

4. **Usage**:

    When prompted, input the following parameters:

    - **Target IP**: The server's IP address.
    - **Fake IP**: Optionally, provide a fake IP.
    - **Port**: The port to attack (default is 80).
    - **Attack Limit**: Number of requests to send (default is 200,000).
    - **Thread Count**: Number of threads (default is 500).

---

## 🔄 Usage Example

1. Run the script:

    ```bash
    python main.py
    ```

2. Input the details when prompted:

    ```
    Enter target IP address: 192.168.1.1
    Enter fake IP address (default: 182.21.20.32):
    Enter target port (default: 80):
    Enter number of attacks (default: 200000):
    Enter number of threads (default: 500):
    ```

3. The tool will start the attack and display the real-time progress.

---

## 🤝 Contributing

Want to add new features or fix bugs? Feel free to fork the repo and submit a pull request!

1. **Fork the repository**
2. **Create a branch** (`git checkout -b feature-name`)
3. **Make your changes**
4. **Commit** (`git commit -am 'Add feature'`)
5. **Push** (`git push origin feature-name`)
6. **Submit a pull request**

---

## ⚠️ Legal Disclaimer

This tool is for **educational purposes only**. Unauthorized DDoS attacks are illegal. Always get permission before testing.

---

## ❤️ Credits

- Developed by **oxyzox**


**Use responsibly and test your servers safely!**
