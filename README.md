# Instagram
### Instagram 2.0 clone 

## Author
Juma Allan.

## Description
This is a simple website replication of the instagram application. A user first needs to  create an account and logging  in. 
Once you are logged in you can upload images.
Logged in users can view photos uploaded by other users in the home page of application.


## Set Up and Installations

### Prerequisites
1. Ubuntu Software
2. Python3.8.10
3. Postgres
4. python virtual environment

### Clone the  project Repo
Run the following command on the terminal:
`git clone https://github.com/juma-moringa/Instagram.git`
* cd Instagram

###  Install and activate virtual environment
Activate virtual environment using python3.8 
* python3 -m venv virtual
* source venv/bin/activate

### Install dependancies
Install  all dependancies that will make the app run/function
* pip install -r requirements.txt

### Create the Database
* psql
* CREATE DATABASE instagram;


### Make Migrations
* python3 manage.py makemigrations doubletap(App name)
* python3 manage.py migrate

### Run the app
* python3.6 manage.py runserver

## Testing the application
* python3 manage.py test doubletap

## Technologies used
    - Python 3.8.10
    - HTML
    - Django 3.2.5
    - Bootstrap 3
    - Heroku
    - Postgresql
    - GIT

## Enjoy :)


## Live Link

[View Live Site.](https://instagram2.0.herokuapp.com/)

## License

Instagram2.0 clone is under the [MIT](LICENSE) license.

@Jaycreations-2021.