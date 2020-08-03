# Modify String
This application takes in an input, casts it into a string (if current type is int or float) and returns every third
element from the original string.

# Prerequisites
We use pipenv as a a dependency manager. Ensure that you have pipenv installed. If not, install using:
```
brew install pipenv
```
To upgrade pipenv:
```
brew upgrade pipenv
```

# Installation
Clone this repo and cd into the directory
```
git clone git@github.com:cinxmo/modify_string.git dir-name && cd dir-name
```
Install all dependencies including ones required for dev
```
pipenv shell
pipenv install --dev
```

# Running Locally
In a terminal, run:
```
uvicorn app.main:app --reload 
```
To test the endpoint, in another terminal, run:
```
curl -X POST  http://127.0.0.1:8000/test/ --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
```
The command above should return  `{"return_string":"muydv"}`

**Note:**
The original endpoint `https://lyft-interview-test.glitch.me/test` does not accept integers as input data,
but this application does. For example, if we pass in the integer `123`, it will return `{"return_string":"3"}` because
`123` is casted as a string due to Pydantic, and `3` is the third element in `"123"`
```
curl -X POST  http://127.0.0.1:8000/test/ --data '{"string_to_cut": 123}' -H 'Content-Type: application/json'
```
returns 
```
{"return_string":"3"}
```

# Tests
To run all tests:
```
pytest
```