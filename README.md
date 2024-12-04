# YVVLE
1. Backlog: [(https://docs.google.com/spreadsheets/d/1QXsTZB_xjxKfIW40T6v8yH378ybaFEUcBSehMxtYBSs/edit?usp=sharing)](https://docs.google.com/spreadsheets/d/1QXsTZB_xjxKfIW40T6v8yH378ybaFEUcBSehMxtYBSs/edit?usp=sharing)
2. [![CI Workflow Badge](https://github.com/imsyc75/YVVLE/workflows/CI/badge.svg)](https://github.com/imsyc75/YVVLE/actions)
3. Test coverage:
   
   ![image](https://github.com/user-attachments/assets/64a43875-aab0-4d7a-984d-e7443067c0bf)


# Definition of done
1. User stories are accepted
2. The maintainability of the code should be as good as possible:
- sensible naming
- reasonable/clear and justified architecture
- consistent code style 
3. Automatic testing is accepted
4. The customers can see the status of the code and tests at all times from the CI service

# User's instruction
Let's launch the application locally. Clone this repository to your machine and go to its folder. Activate the virtual environment with commands.
```python
$ cd <file>
$ poetry install
$ poetry shell
```
The application requires a PostgreSQL database to run. In the root directory of the application, you must create a file called .env that defines environment variables with the following content:
```python
DATABASE_URL=postgresql://xxx
TEST_ENV=true
SECRET_KEY=random_string
```

Please note that, before starting the application for the first time, you must run the command of the database table used by the application:
```python
python3 src/db_helper.py
```

Use the following command to launch the application in the Poetry virtual environment：
```python
python src/index.py
```

Use the following command to execute the robot tests:
```python
robot src/story_tests
```




