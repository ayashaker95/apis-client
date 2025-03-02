import requests

class APIClient:
    base_url = "https://jsonplaceholder.typicode.com"

    def get(self, endpoint, id=None):
        url = f"{self.base_url}{endpoint}"
        if id is not None:
            url += f"/{id}"
        
        response = requests.get(url)
        return response  # Returns a Response object

    def post(self, endpoint, json=None):
        # Perform validation only if the endpoint includes "/posts"
        if "/posts" in endpoint:
            required_fields = ['title', 'body', 'userId']
            missing_fields = [field for field in required_fields if field not in json]

            if missing_fields:
                # Return a response with status_code 400
                response = requests.Response()
                response.status_code = 400
                response._content = f"Error: Missing required fields: {', '.join(missing_fields)}".encode('utf-8')
                return response
        
        url = f"{self.base_url}{endpoint}"
        
        response = requests.post(url, json=json)
        return response  # Returns a Response object

    def put(self, endpoint, json=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=json)
        return response  # Returns a Response object

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url)
        return response  # Returns a Response object
