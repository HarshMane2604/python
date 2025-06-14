import requests
def fetch_random_user_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    respose = requests.get(url)
    data = respose.json()
    # print(data)
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_Location = user_data["location"]["country"]
        return user_name, user_Location
    else:
        raise Exception("Failed to fetch userdata")
    
def main():
    try:
        username, country= fetch_random_user_freeApi()
        print(f"Username: {username}\n Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
