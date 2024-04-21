
must use virtual environment for execution;
 set up instructions for VS terminal:

    1. python -m venv venv
    2. .\venv\Scripts\Activate.ps1
    3. pip install -r requirements.txt

exectue python files:
    1. python "name_of_file.py"

    when done
    4. deactivate

Adding libraries/dependancies in venv:
    1. pip install requirements.txt
    2. pip install library
    2. pip freeze > requirements.txt

if you encounter problems with activation or running:
    1. Set-ExecutionPolicy -Scope CurrentUser Unrestricted

Delete venv in folder explorer before pushing to Git
