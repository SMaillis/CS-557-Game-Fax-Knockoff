# GameFAQs Knockoff Site (Name WIP)

# How to Setup MySQL + Django.
1. Clone the repo.
2. Ensure you have a MySQL (server) installed and running on your machine.
3. Enter MySQL (on Linux the command is `mysql -u *username* -p`).
4. Create the database by running `CREATE DATABASE IF NOT EXISTS *database_name*;`. You can see if it worked as well as existing databases with `SHOW DATABASES;`.
5. Take the example.env, name it .env, and replace the placeholder data with the correct information like database name, user, etc. etc.

# Running the project.
Within PyCharm you can add a new run configuration and simply use Django Run Server to run the project. It should just work if you've installed all the requirements. e.g. `pip install -r requirements.txt`.

Else to run using CLI you do `manage.py runserver 127.0.0.1:8000` after entering the Python virtual environment `source .venv/bin/activate`.

Then go to the URL in the browser and you should have access to the site.