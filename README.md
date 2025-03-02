
# APIs Client

A Python-based client for interacting with various APIs. This repository contains methods for performing common API operations such as GET, POST, PUT, and DELETE.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ayashaker95/apis-client.git
   ```

2. Navigate to the project directory:
   ```bash
   cd apis-client
   ```

3. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. **GET Request**:
   Use the `get` method to retrieve data from an endpoint.
   
   ```python
   api_test.get('/posts')
   ```

### 2. **POST Request**:
   Use the `post` method to send data to an endpoint.

   ```python
   payload = {"title": "New Post", "body": "This is a new post.", "userId": 1}
   api_test.post('/posts', json=payload)
   ```

### 3. **PUT Request**:
   Use the `put` method to update data on an endpoint.

   ```python
   payload = {"id": 1, "title": "Updated Post", "body": "This is an updated post.", "userId": 1}
   api_test.put('/posts/1', json=payload)
   ```

### 4. **DELETE Request**:
   Use the `delete` method to remove data from an endpoint.

   ```python
   api_test.delete('/posts/1')
   ```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
