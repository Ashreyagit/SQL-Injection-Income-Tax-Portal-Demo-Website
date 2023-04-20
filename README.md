# SQL injection demo

![Header SQL injection](./src/app/static/img/header.png "SQL injection Demo header")

A python-flask Income Tax Portal web application to demonstrate SQL injection.

_Note: Has two parts showing- a bypassing login SQL injection as well as retrieving Tax details database records in the Search page._ 

On running the application, it is accessible at  http://127.0.0.1:8080/login 

# Working

In the models.py file of our flask project, two tables have been created: users and records to store information related to users and their Tax records. Both tables have several columns that will be used by the application. The web pages are served from the views.py file which includes a login, logout, and index page (which is only accessible to logged-in users). The HTML code is located in the templates folder and utilizes JINJA2 as a text processor, which enables macros and reduces repetition in the HTML code. In addition, static folder contains resources such as CSS to enhance the visual appeal of the pages, as well as images and other assets.

![Web capture_20-4-2023_14054_](https://user-images.githubusercontent.com/56057427/233308586-48706f64-6daf-4e72-a7e2-e577e7f54f41.jpeg)








