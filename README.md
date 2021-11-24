# Python App Exercise

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)

## Running the app
This app requires some dependecies to be run.
Pipenv has been used to manage those depdnecies as it generates a lockfile to ensure all
transitive dependencies are compatible and that everybody installs the same dependencies.

## Implementation approach
The download of the json uses is streamed and creates a generator. That avoids loading the
whole JSON in memory. Although that not seems a big problem right now it could become big
with the time and you asked for an implementation that looked a bit ahead.

Also api request and file persistance have been developed in a way they are extensible to
other endpoints, objects, folder structures and filenames. 


