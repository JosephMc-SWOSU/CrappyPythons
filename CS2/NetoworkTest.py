# pip install speedtest-cli
import os
import subprocess
import speedtest

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        results = st.results.dict()
        print(f"Download speed: {results['download'] / 1_000_000:.2f} Mbps")
        print(f"Upload speed: {results['upload'] / 1_000_000:.2f} Mbps")
        print(f"Ping: {results['ping']} ms")
    except speedtest.ConfigRetrievalError as e:
        print("Failed to retrieve speedtest configuration. Please try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_ping(host):
    try:
        result = subprocess.run(["ping", "-c", "4", host], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{host} is reachable")
        else:
            print(f"{host} is not reachable")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_traceroute(host):
    result = subprocess.run(["traceroute", host], capture_output=True, text=True)
    print(result.stdout)

def main():
    while True:
        print("Network Analysis Tool")
        print("1. Speedtest")
        print("2. Ping")
        print("3. Traceroute")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            run_speedtest()
        elif choice == '2':
            host = input("Enter the host to ping: ")
            run_ping(host)
        elif choice == '3':
            host = input("Enter the host for traceroute: ")
            run_traceroute(host)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()