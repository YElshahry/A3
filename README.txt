Name: Yousuf Elshahry
Student I.D.: 101201262
Assignment: 3 Q1

.env file:

PGHOST=127.0.0.1
PGPORT=5432
PGDATABASE=a3
PGUSER=postgres
PGPASSWORD=changeme

Steps to run:

- Open pgAdmin and create a database named 'a3'.
- Open db/schema.sql in the query tool and execute it.
- Open the project folder in VS Code.
- Create the .env file copy the prompt that I gave.
- Change the 'changeme' section to whatever password you want.
- Go back to pgAdmin and expand a3 then expand Login/Group Roles.
- Scroll down until you see 'postgres' right click it and click properties.
- Click 'Definition' at the top and set the password that you put in the .env file.
- Click save and go back to VS Code.
- Open a new terminal and run: .\.venv\Scripts\Activate.ps1
- run: cd app
- Then install dependencies by: pip install -r requirements.txt
- Run the python app by: python app.py
- In pgAdmin, right click the 'students' table then click View/Edit Data.
- Then All Rows and press refresh to see INSERT, UPDATE, and DELETE changes.


Video Demonstration:

https://youtu.be/rrN58opfOzg
