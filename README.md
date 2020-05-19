## **THE MUSIC DOWNLOADER-APP;**<br/>
​
 
 This is an Interactive Music app that enables a user to download and listent to the latest music upon registration<br/>
​
​
​
## BDD
​
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Registratin | Fill in the form in the registration page | Redirects to the login page |
| Login | Fill in the form to have access to the page| Redirects to the home page with the apps navigations |
| Downloading songs| 
| Updating and deleting blogs | Click the update button in the profile page or the delete button | Redirects the user to the updated comment or deletes the chosen comment |
| Updating profile picture | Click the select button then the update button | Redirects the user to where the photo is then automatically updates when the user clicks on the update button |
​
​
​
## **Team;**<br/>
The project was built with the help of Moringa school  of coding and their amazing team of Technical Mentors<br/>
technical mentors these include;<br/>
​
* Barclay <br/>
​
​
## Live link
​
​
## Set-up and Installation
​
### Prerequsites
    - Python 3.7
    - Ubuntu software
​
### Clone the Repo
Run the following command on the terminal:
``
​
Install [Postgres](https://www.postgresql.org/download/)
​
### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.7 -m venv virtual`
`source virtual/bin/activate`
​
### Install dependancies
Install dependancies that will create an environment for the app to run
`pip3 install -r requirements`
​
### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/blog'
export SECRET_KEY='Your secret key'
```
​
### Run Database Migrations
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
​
### Running the app in development
In the same terminal type:
`python3 manage.py server`
​
Open the browser on `http://localhost:5000/`
​
## Known bugs
​
```None so far but i'll be glad to be communicated to if there is one ```
​
​
## Technologies used
    - Python 3.7
    - HTML
    - Bootstrap 
    - Animate CSS
    - Heroku
    - Postgresql
​
​
​
​
## **Contributors;**<br/>
Incase of any trouble or you like what you see my contacts are ;<br/>  
* Name : Lorraine Kamanda 
* Name : Martin Mwikia
* Name : Salem Owino
* Name : Ruth Mugo
* Name : Daniella Chege
​
​
## **Operating Instructions;**<br/>
The programme should run on any pc provided you have internet connection.<br/>
Feel free to contact any of the contributors for any comments,reviews or advice<br/>
​
​
### License
Copyright (c) **Musica**
Co