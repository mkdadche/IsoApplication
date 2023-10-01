# FrontEndApplication
This application is the user interface of the ISO code application

## Dependencies

Before running the FrontEndApplication, make sure the following two microservices are up and running:

* [Matched Country service application](https://github.com/mkdadche/MatchedCountriesApplication)
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
docker build -t frontend-app .
```

### Run the container
```
docker run -p 4000:4000 frontend-app
```

### Now, we should have the FrontEndApplication up and running. Access it in your browser at http://127.0.0.1:4000.