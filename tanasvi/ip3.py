import geocoder
import json

location = geocoder.ip('me')
print(json.dumps(location.raw, indent=4))

# import geocoder
# import json

# def get_system_location_as_json():
#     try:
#         # Use the geocoder library to get location based on IP address
#         location = geocoder.ip('me')

#         # Access latitude, longitude, and country code
#         latitude, longitude = location.latlng
#         country_code = location.country

#         # Create a dictionary with the location information
#         location_dict = {
#             "latitude": latitude,
#             "longitude": longitude,
#             "country_code": country_code
#         }

#         # Convert the dictionary to a JSON-formatted string
#         location_json = json.loads(location_dict, indent=2)

#         print(location_json)
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     get_system_location_as_json()



# import socket
# import json

# def get_local_ip_info():
#     try:
#         # Get the local machine's hostname
#         host_name = socket.gethostname()

#         # Get the local machine's IP address
#         local_ip = socket.gethostbyname(host_name)

#         # Create a dictionary with the local IP information
#         local_info = {
#             "hostname": host_name,
#             "local_ip": local_ip,
#             # Add more properties as needed
#         }

#         # Convert the dictionary to a JSON-formatted string with indentation
#         local_json = json.dumps(local_info, indent=2)

#         print(local_json)
#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     get_local_ip_info()


