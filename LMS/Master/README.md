## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Installing

You must have `python` and `pip` installed on your system, and in you `PATH`.
An activated virtual environment is also recommended.

Run the command in cmd with the *requirements.txt* in the proper suitable environment.

''' pip install -r requirements.txt'''

This will install all project dependencies.

Next, copy-paste `config.example.json` as `config.json` (do not delete the
original `config.example.json`) and open it in your
code editor and configure it according to your needs. Here are some of the ones
you would want to change. Ideally you would want to only the `path` key to
where your chromedriver is located. The rest should work out of the box.

## Starting the project

After you are done with the project setup, you can start it using
`python cheek/main.py`. If all your configurations are correct, then the
correct website would be launched and automation process should be under way.

[1]: https://github.com/python-poetry/poetry
