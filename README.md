# Instructions to run app, and a description for decisions

## How to run code
Run docker-compose up -d --build

If you want to run tests run, docker run password_generator_app test.

### sample request to test the service
curl -X POST -H "Content-Type: application/json" -d
'{"password_length": "20", "include_lowercase_chars": "true"}'
`http://0.0.0.0:8000/api/v1/authentication/generate-password/`


### flowchart of app
https://lucid.app/lucidchart/68fa44d8-fe1b-447c-92ae-b00136337c4c/edit?view_items=q7NtnToLUGX9&invitationId=inv_8b09b236-58eb-4c93-a596-1510c626cd65#


## design decisions
I decided to use clean architecture to write the app because of its extensibility,
 and the well-defined and separated responsibility of each layer.

I use https://github.com/tiangolo/full-stack-fastapi-postgresql as a sample for
 designing the project layout.

Try my best to consider SOLID principles and DRY technique during this project.

Utilized pydantic for input data validation and also data of response. With the help of this library I'm able to run the
 put minimum and maximum password length.
 
Handled the all inputs null or all characters include false option for generated password in the main api body.

Decided to separating the password generator function to satisfy separation of concerns.
 
I put the configurable settings in env file and use it in config file.

With the help of routers I managed to differentiate the api versions and different possible apps. Here we have api
 version 1 and only authentication app which has a single endpoint generate password.
  
Decided to use async and uvicorn to make the api faster and able to handle more requests.

I also try to make generated password include characters from all characters list user wants to use and shuffle it at
 the end.

I write unit tests for all parts including rest api and also the password generator that's located in internal folder.


## deployment
Create the gitlab ci file to run CI. Run one stage to build the image, then run the tests in it and then push the
 image to dockerhub. It could be any registry or main server to achieve continues delivery and deployment(CD).

