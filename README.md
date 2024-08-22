# lntips
Simple lightning app to receive tips using getalby API

## Requirements

- Python 3.10 or higher
- Python dependencies `Flask`,`decouple`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/bitao36/lntips.git
cd lntips
```

2. Create a virtual environment and activate it:

**For Linux:**

install these dependencies to crate virtual environment
```
sudo apt-get install python3-dev
```

Install virtual environment just the first time

```bash
python3 -m venv venv
```

Activate the virtual environment (activate the environment every time you go to run the endpoint)


```bash
source venv/bin/activate
```

**For Windows:**


Install virtual environment just the first time


```bash
virtualenv venv
```

Activate the virtual environment (activate the environment every time you go to run the endpoint)

```bash
venv\Scripts\.\activate
```


3. Install the required dependencies:

```bash
pip install -r requirements.txt
```


### Environment Variables

To test the project you must create a file .env and to add the following environment variables to connect to getalby

```bash=
API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
GETALBY_URL=https://api.getalby.com/

```

## Access the application

### Server execution

```
flask run
```

### Web client

Go to browser 
```
http://localhost:5000
```
