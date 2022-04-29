# 🌍 IET_CDOE

## Follow the following 📃 steps to setup 🚀 project 

- The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ShadMirza/IET_CDOE.git
$ cd IET_CDOE
```

- Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv env
$ env/Scripts/activate
```

- Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
<i>Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.</i>

- Copy and paste .env file into the root folder (IET_CDOE) of project: <a href='https://drive.google.com/file/d/1MF9a4W3QpLZ2Qv8t0XMmerBJ0se4S4J0/view'>Ask author for the .env file</a>

- Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
- And navigate to `http://127.0.0.1:8000`.
