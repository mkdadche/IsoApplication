# DownloadFile application
This application is used to download the result for the users.

## Dependencies

To make the applictaion fully running, make sure the following two microservices are up and running:

* [FrontEndApplication](https://github.com/mkdadche/FrontEndApplication)
* [MatchedCountriesApplication](https://github.com/mkdadche/MatchedCountriesApplication)

# Steps to run the application
## Running without Docker
**The below steps should be taken with each of the above repository.**
### Python

DownloadFile application was build and run on Python 3.11.5.

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
docker run -p 4002:4002 match-app
```

## Running the test
**Please follow the below steps.**
* Make sure the virtual enviroment is activated.
* Run the command `pytest`, you should get all the tests passed.

**For test coverage**
* After running the command `pytest` run the command `coverage run -m pytest` and then the command `coverage report -m`. then you will get the below table

| Name         | Stmts | Miss | Cover |
|--------------|-------|------|-------|
| model.py     |  6    | 0    | 100%  |
| test_model.py| 11    | 0    | 100%  |
| TOTAL        | 17    | 0    | 100%  |

