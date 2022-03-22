## Prometeo Challenge Backend

This project uses the following endpoints from Prometeo API:

- /login/
- /logout/
- /client/
- /account/
- /account/{accountNumber}/movement/
- /credit-card/
- /credit-card/{cardNumber}/movements
- /transfer/destinations
- /transfer/preprocess
- /transfer/confirm
- /provider/
- /provider/{providerCode}/

## Installation

It requires Python v3.7.5+ to run.

Install the dependencies and run the project.

pip install -r requirements.txt


## Execution

Required env vars:

- BACKEND_URL: The URL of the Django backend (should be set for production execution)
- CORS_ALLOWED_ORIGINS: The list of allowed origins, separated by a semicolon (;) (should be set for production execution)
- DB_HOST: The database host
- DB_NAME: The database name
- DB_PASSWORD: The database password
- DB_PORT: The database port
- DB_USER: The database user
- DEBUG_MODE: Whether the app is running in debug mode or not (set TRUE for local execution)
- PROMETEO_API_KEY: The Prometeo API key
- PROMETEO_API_URL: The Prometeo API URL
- SECRET_KEY: The secret key used by Django
