#pip install speedtest-cli https://github.com/sivel/speedtest-cli/wiki#python-api

# import os https://python-forum.io/thread-14529.html
import subprocess #https://www.datacamp.com/tutorial/python-subprocess
import speedtest

def run_speedtest():
    try:
        st = speedtest.Speedtest()  # create a speedtest object
        st.get_best_server() # get the best server
        st.download()  # download speed
        st.upload(pre_allocate=False)  # upload speed
        results = st.results.dict()  # get the results as a dictionary
        print(f"Download speed: {results['download'] / 1_000_000:.2f} Mbps")  # convert to Mbps
        print(f"Upload speed: {results['upload'] / 1_000_000:.2f} Mbps")  # convert to Mbps
        print(f"Ping: {results['ping']} ms")  # ping in milliseconds
    except speedtest.ConfigRetrievalError as e:
        print(f"Failed to retrieve speedtest configuration. Please try again later. Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_ping(host):
    try:
        result = subprocess.run(["ping", "-n", "4", host], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{host} is reachable")
        else:
            print(f"{host} is not reachable")
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

def run_traceroute(host):
    try:
        result = subprocess.run(["tracert", host], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {e}")

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