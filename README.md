# spell-checker

This repository contains the code for a simple API that can be used to check whether a word is in a predetermined dictionary of words, and spelled according to certain standards.

For exact the problem statement, please see [this document](exercise/spellchecker.md).

## Implementation

The application consists of a [Flask](https://flask.palletsprojects.com/en/1.1.x/) JSON API backed by a [Redis](https://redis.io/) instance.

Flask was chosen given that it is a relatively lightweight framework without much unnecessary boilerplate, and thus seemed suited for the scope of this microservice.

Redis was chosen as the data store given that the application really only needs to know about a set of accepted word strings and have the ability to access them quickly.

## Usage

The API has a single endpoint for checking words which accepts HTTP GET requests: `/spellcheck/{word}`

##### Example 1: Correctly spelled and formatted word

```
# Request
GET /spellcheck/apples

# Response
Status Code: 200
Body: {"correct": true, "suggestions": []}
```

##### Example 2: Correctly spelled but incorrectly formatted word 

```
# Request
GET /spellcheck/aPpLeS

# Response
Status Code: 200
Body: {"correct": false, "suggestions": ["apples", "applies"]}
```

##### Example 3: Incorrectly spelled word

```
# Request
GET /spellcheck/appplessss

# Response
Status Code: 200
Body: {"correct": false, "suggestions": ["apples", "applies"]}
```

##### Example 4: Nonexistent word

```
# Request
GET /spellcheck/foobar

# Response
Status Code: 404
```

## Logic

The general spell-checking logic as follows:

1. Check for a valid match right away.
    - "Valid" means exactly matches the spelling of a word in the dictionary *and* is of an accepted format (read: capitalization). 
    - No need to proceed with finding suggestions if the user has provided a valid query.
    - If valid, return a 200 response with a body noting that the word is correct.

2. If no valid match found off the bat, build a regular expression (regex) to search the dictionary for possible spelling suggestions per allowable mistakes (see [specifications](exercise/spellchecker.md)).
    - If there is at least one word in the dictionary that matches the regex, the query word is considered "found". Return a 200 response with a body noting that the word is incorrect but suggestions were found.
    - If no dictionary words match the regex, the query word is considered "not found" and a 404 response is returned.

## Running the Application

The application has been dockerized for portability. To spin up an instance of the application, follow these steps: 

1. Ensure you have [`docker`](https://www.docker.com/) and [`docker-compose`](https://docs.docker.com/compose/) installed.

2. Clone the repository and change directory into the project.

```
$ git clone https://github.com/ellisandrews/spell-checker.git
$ cd spell-checker
```

3. From the `spell-checker/` directory, run the following command to start the application:

```
$ docker-compose up -d --build
```

This builds the project docker image and then spins up 3 services in networked docker containers:

1. The Flask JSON API
2. The Redis instance
3. A Python script to seed the redis instance with the dictionary of acceptable words (see: [dictionary.txt](/exercise/dictionary.txt)). 

The data seeding script will finish quickly and exit. The other two services will continue running in respective docker containers.

The API will be accessible at [http://localhost:31337/](http://localhost:31337/) (Remember there is currently only one supported endpoint!)
