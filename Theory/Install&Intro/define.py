"""
Flask - Flask is a lightweight Python web framework used to build APIs and web apps quickly with full control.

Flask → You build things yourself
Django → Everything is already built for you

Before we start to build web apps we must activate virtual environment (venv)
Beacuse,
Keeps packages separate, Each project gets its own Flask, Django, TensorFlow, etc.
Think of it like a separate Python room just for one project.

Imagine this situation

You have 3 Python projects:

Project A → needs Flask 2.0
Project B → needs Flask 3.0
Project C → needs Django

If you don't use venv:

All packages install globally
Versions clash
One project breaks another

After that we need to activate that venv using this command (recommended command prompt):

venv\Scripts\activate (or) "C:/Users/THIS PC/Desktop/flask_app/venv/Scripts/activate.bat"

how to know wether its activated or not?
 
(venv) C:\Users\THIS PC\Desktop\flask_app> if it activates usually it shows (venv) at the starting of the path
and also check if you have doubt not cleared just type
(venv) C:\Users\THIS PC\Desktop\flask_app> python --version it shows version then ready to install flask framework on this venv.
 
So, just type " pip install flask "
if it needs any update version of pip then type this command 
python.exe -m pip install --upgrade pip

Last check flask version to confirm
flask --version
"""

