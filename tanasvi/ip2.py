import requests

def get_public_location():
    try:
        # Make a request to the ipinfo.io API to get information about the public IP
        response = requests.get('https://ipinfo.io/json')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and return the location information
            return f"Public Location: {data['city']}, {data['region']}, {data['country']} ({data['loc']})"
        else:
            return f"Error: Unable to fetch public location. Status code: {response.status_code}"

    except Exception as e:
        return f"Error: {e}"

# Call the function to get the public location
public_location = get_public_location()

print(public_location)
