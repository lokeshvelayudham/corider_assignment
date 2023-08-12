An appliction for CRUD operations on MongoDB using flask+python backend and build  REST API, The REST API endpoints should be accessible via HTTP requests and tested using Postman.


The application should connect to a MongoDB database.
The application should provide the following REST API endpoints:

    -1.GET /users - Returns a list of all users.
    -2.GET /users/<id> - Returns the user with the specified ID.
    -3.POST /users - Creates a new user with the specified data.
    -4.PUT /users/<id> - Updates the user with the specified ID with the new data.
    -5.DELETE /users/<id> - Deletes the user with the specified ID.


Setup and installation
1. Create a virtual environment 
   1.  ```python3 -m venv venv```
   2.  ```source venv/bin/activate```
   3.  create a new file in the directoty named app.py 


2.  To install Flask and pyMongo using **pip install**
    1.  ```pip install Flask pymongo```
    2.  import the flask and pymongo into the app.py


3. Install & Setup MongoDb Databsae using **homebrew**
   1. install MongoDb community in the local
      1. ```brew install mongodb-community@6.0``` 
   2. To Start mongoDb server 
      1. ```brew services start mongodb-community@6.0```
   3. After starting the server open a new terminal
      1. ```mongosh```
      2. ```use Collection```
      3. ```db.createCollection("users")```
   4. To insert the data into the db
        ```db.users.insert({
            "name": "John Doe",
            "email": "john@example.com",
            "password": "secretpassword"
            })```

4. Run the Application.
* flask run

1. Testing the Application using CRUD
   1. Test in the POSTMAN
   2. install postman desktop agent
      1. The REST API endpoints:
         1. GET /users - Returns a list of all users.
         2. GET /users/<id> - Returns the user with the specified ID.
         3. POST /users - Creates a new user with the specified data.
         4. PUT /users/<id> - Updates the user with the specified ID with the new data.
         5. DELETE /users/<id> - Deletes the user with the specified ID.


6. To Dockerize :
   1. Create a file named Dockerfile
   2. requirements.txt
        ```Flask==2.0.1
        Flask-PyMongo==2.3.0```
    3. create a yml file
    4. Build and run 
      docker-compose build
      docker-compose up
    5. push the docker into hub
       1. list the docker images - ``` docker images```
       2. login into docker - ```docker login``` enter username and password
       3. create a image tag docker tag IMAGE NAME HUBNAME/IMAGE NAME - ```docker tag corider_assignment-app lokeshbx/corider_assignment-app```
       4. docker push IMAGE - docker push lokeshbx/corider_assignment-app 