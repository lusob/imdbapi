## Overview

This flask application implements a REST API feeded from imdb datasets https://datasets.imdbws.com/. 

It uses flask_restless, a model driven library that expose the sqlalchemy models as endpoints resolving pagination, filtering, sorting, etc.

The endpoinst and routing is manage by the framework, so we can write all the code is in just a file (app.py) for simplicity

You can use docker to try the project or install it locally in your workstation:

## Docker installation:

    $ docker build -t imdbapi https://github.com/lusob/imdbapi.git
    $ docker run -p 5000:5000 imdbapi


## Locally installation

### To install it:

In the top-level directory:

    $ ./init_db.sh # To import the datasets and build the sqlite db (it requires sqlite3 installed in your system)
    $ python3 -m venv env && source env/bin/activate
    $ pip3 install -r requirements.txt 

### To run it:

In the top-level directory:

    $ export FLASK_APP=app.py
    $ flask run

### To test it:


#### Manually from the terminal:

##### Filtering:

You can use in the name argument any field of the table, The query parameter q must be a JSON string. It can have the following mapping:

    {"name": <fieldname>, "op": <operatorname>, "val": <argument>}

More info: https://flask-restless.readthedocs.io/en/stable/searchformat.html#query-format
    
Sample query of movies with "matrix" word in the title:
    
    $curl -H "Accept: application/vnd.api+json" "http://127.0.0.1:5000/api/imdb_title_basics?q=\{\"filters\":\[\{\"name\":\"primaryTitle\",\"op\":\"like\",\"val\":\"%matrix%\"\}\]\}"

Sample query of movies with "Documentary" word in the genres:
    
    $curl -H "Accept: application/vnd.api+json" "http://127.0.0.1:5000/api/imdb_title_basics?q=\{\"filters\":\[\{\"name\":\"genres\",\"op\":\"like\",\"val\":\"%Documentary%\"\}\]\}"

Sample query of movies with 30 runtime minutes:
     
     $curl -H "Accept: application/vnd.api+json" "http://127.0.0.1:5000/api/imdb_title_basics?q=\{\"filters\":\[\{\"name\":\"runtimeMinutes\",\"op\":\"eq\",\"val\":\"%30%\"\}\]\}"

#### Pagination: 
This line loads page number 2 of the total resultset:

    $curl -H "Accept: application/vnd.api+json" "http://127.0.0.1:5000/api/imdb_title_basics?page=2"

#### Sorting: 
This line loads total results sorted by startYear, you can change by any other table field what you want to sort by:

     $curl -H "Accept: application/vnd.api+json" "http://127.0.0.1:5000/api/imdb_title_basics?sort=startYear"

Also there is a simple test script in the top-level directory, to run it:

    $ python test_app.py

### ToDo List:

- Authotization: Flask-Restless doesn't suppor authentification, but it could be used combined with flask-auth with this workaround https://stackoverflow.com/questions/42533259/python-flask-using-flask-restless-with-flask-httpauth
- Get directors names, I forgot to import the name.basics table and make the model associated and now I'm running out of time.
- Creation action, for some reason the creating is a failing (see commented test in test_app.py) and I didn't have time to debug it. 
