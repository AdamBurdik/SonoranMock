# Sonoran Mock

Application for simulating sonoran cad server.

## Disclaimer
This is only API implementation. No frontend

Only the following endpoints are implemented:
- /general/get_version
- /general/get_account
- /civilian/get_characters
- /civilian/edit_character

> Character data is written for my specific usage. Its custom record from sonoran. If you want to use this for your specific project, please edit it first.

## How to run
1. Clone the repository
```bash
git clone https://github.com/adamBurdik/SonoranMock
```
2. Start program using uv
```java
uv run python src/main.py
```
Sonoran will be running on `http://127.0.0.1:5000`

## How to use
Just send request to the specific endpoint. 

For example, for version use `http://127.0.0.1:5000/general/get_version`

> The API_KEY is not used for anything. You can use anything.

> COMMUNITY_ID is used for saving data to files.

For further information check [sonoran docs](https://docs.sonoransoftware.com/cad/api-integration/api-endpoints/general/get-version)