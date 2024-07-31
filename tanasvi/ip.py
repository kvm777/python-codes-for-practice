import socket

def get_ip_address():
    # Get the hostname
    hostname = socket.gethostname()

    # Get the IP address associated with the hostname
    ip_address = socket.gethostbyname(hostname)

    return ip_address

# Call the function to get the IP address
ip_address = get_ip_address()

print(f"The IP address of the system is: {ip_address}")
