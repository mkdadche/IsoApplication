# IsoApplication
IsoApplication is a tool that retrieves ISO codes for specified countries and returns a list of countries matching the provided ISO code.

# Getting Started
**To run the IsoApplication, you have two options, both of which rely on three microservices: [FrontEnd service](https://github.com/mkdadche/IsoApplication/tree/main/applications/FrontEndApplication) , [Matched Countries service](https://github.com/mkdadche/IsoApplication/tree/main/applications/MatchedCountriesApplication) , [Download File service](https://github.com/mkdadche/IsoApplication/tree/main/applications/DownloadFileApplication) , therefore, there are the below two ways o run the application.**

## Option 1: Using Docker Compose
Running the application with Docker Compose is the quickest way to get started. It will automatically build and launch containers for all three microservices. Follow these steps:

* Make sure you have Docker and Docker Compose installed on your system.

* Navigate to the root directory of IsoApplication.

* Run the following command to start the application:
 ```
docker-compose up
```

* Access the application in your web browser at http://127.0.0.1:4000.

## Option 2: Manual Setup
If you prefer to set up the microservices manually, you can do so by following these steps for each individual service:
* [FrontEnd service](https://github.com/mkdadche/IsoApplication/tree/main/applications/FrontEndApplication)
* [Matched Countries service](https://github.com/mkdadche/IsoApplication/tree/main/applications/MatchedCountriesApplication)
* [Download File service](https://github.com/mkdadche/IsoApplication/tree/main/applications/DownloadFileApplication)

## **Each application has README file provides detailed instructions on how to set up and run the respective service. Additionally, you will find test scenarios specified in these README files for the Matched Countries and Download File services.** 