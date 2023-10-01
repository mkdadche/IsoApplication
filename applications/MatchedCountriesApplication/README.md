# MatchedCountriesApplication
This application is the used to pull the ISO code of the given countries from the API https://restcountries.com/v3/name/ and return the countries that matching the given ISO code.

## Dependencies

To make the applictaion fully running, make sure the following two microservices are up and running:

* [FrontEndApplication](https://github.com/mkdadche/FrontEndApplication)
* [DownloadFile application](https://github.com/mkdadche/DownloadFileApplication)

# Steps to run the application
## Running without Docker
**The below steps should be taken with each of the above repository.**
### Python

FrontEndApplication was build and run on Python 3.11.5.

* Install [Python](https://www.python.org/downloads/)

### Create virtual environment

The `venv` module is used for dependency management. Run these commands to create a virtual environment and activate it:

```
python -m venv env
.\env\Scripts\activate
```

If the virtual environment was activated, your command prompt should begin with `(env)`.

**The rest of these instructions assume your virtual environment is activated.**

### Install required modules

```
pip install -r requirements.txt
```

### then Run the below command
```
flask run
```

## Running with Docker
**Execute the below two steps and they should be taken with each of the above repository.**
### Build the docker image
```
docker build -t match-app .
```

### Run the container
```
docker run -p 4001:4001 match-app
```


## Running only the API
If you would like only to use the API (without running the whole web application), you can run only this microservice and use the API by accessing http://127.0.0.1:4001/apidocs as swagger API

## Running the test
**Please follow the below steps.**
* Make sure the virtual enviroment is activated.
* Run the command `pytest`, you should get all the tests passed.

**For test coverage**
* After running the command `pytest` run the command `coverage run -m pytest` and then the command `coverage report -m`. then you will get the below table

| Name         | Stmts | Miss | Cover |
|--------------|-------|------|-------|
| model.py     | 40    | 0    | 100%  |
| test_model.py| 25    | 0    | 100%  |
| TOTAL        | 65    | 0    | 100%  |

## Caching with cachetools

In this project, we utilize the `cachetools` module to implement caching for improved performance and reduced API calls. Here's how it works:

- We initialize a TTL (Time-to-Live) cache with the following parameters:
  - Maximum cache size: 100 items
  - Expiration time: 3600 seconds (1 hour)

- When we need to fetch the ISO code for a country based on its name, we first check if the country name is already present in the cache.

- If the country name is found in the cache, we retrieve the ISO code from the cache, eliminating the need to make an API request to [https://restcountries.com/v3/name/](https://restcountries.com/v3/name/). This optimization helps reduce unnecessary API hits and improves overall system performance.
