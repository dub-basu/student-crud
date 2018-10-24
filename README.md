# Assignment for Project
Problem explained in [problem description](/problem_statement.pdf).

 * The assignment is coded in **Python** using **Flask** web framework.
 * The app broadly fulfills two functional requirements
     - **Add** a student
     - **View** all the saved student records 
 * **Merge Sort**: Everytime the user requests to view the student records, the records are fetched from the database and sorted in ascending order of their `name`. The merge sort implementation is present as the `merge_sort` function in [utils.py](src/utils.py).
 * Attempt has been made to make the Python code compliant with **[PEP 8](https://www.python.org/dev/peps/pep-0008/) - Style Guide for Python** and **[PEP 257](https://www.python.org/dev/peps/pep-0257/) - Docstring Conventions**. 

## Dependencies
 - Python3 [Not tested on other versions. Should be compatible]
 - Other [python3 dependencies](/requirements.txt)

## How to run
Ensure that the dependencies are installed properly.
Change directory to `src`
```bash
    cd src
```
Run the `run.sh` script to run the app on localhost.
```
    ./run.sh
```
The app runs on localhost at port 5000 by default.<br>
Once the app is running, open the web browser and navigate to `localhost:5000` to use the app.

The run script essentially runs two commands. 
 - `export FLASK_APP=app.py`
 - `flask run`

# Directory Structure

### /
```
/
├── LICENSE
├── problem_statement.pdf
├── README.md
├── requirements.txt
└── src
```
Root directory of the assignment
 - `LICENSE`
 - `problem_statement.pdf`: Original description of the problem
 - `README.md`: This doc that you are reading
 - `requirements.txt`: Python requirements
 - `src`: The source code of the assignment


### src
```
src
├── app.py
├── db.py
├── db.sqlite3
├── forms.py
├── run.sh
├── schema.sql
├── static
│   ├── css
│   ├── img
│   └── js
├── templates
│   ├── add.html
│   ├── back-icon.html
│   ├── base.html
│   ├── _formhelpers.html
│   ├── home.html
│   ├── messages.html
│   └── view_all.html
└── utils.py
```
Source code of the assignment:
 - `app.py`: Contains the web(Flask) app code.
 - `db.py`: Module containing `DBHandler` class to handle database.
 - `db.sqlite3`: SQLite database file. Will be created after first run of the program.
 - `forms.py`: Contains description of a WTForms form class. Used to get student data.
 - `run.sh`: Utility script to run the app.
 - `schema.sql`: SQL statement to create a `student` table(if does not exist already).
 - `static`: Directory containing javascript, css and image files used in the app.
 - `templates`: Directory containg templates(pages) used in the web app.
 - `utils.py`: Module containing utility functions and classes. Currently includes `Student` class and the `merge_sort` implementation.
