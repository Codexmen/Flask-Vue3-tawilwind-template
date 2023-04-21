# This is Flask + Vue 3 + SQLAlchemy boilerplate project

### What included:
- Flask app
- REST API Login flow - TBD
- DB migrations for Users table
- Vue 3 project with basic structure (API level, Login Form, Private routes) - TBD

### How to start project

- install Python dependencies 
- install Vue dependencies see `How to install Client` section 
- connect DB
- run migrations


### how to start server
- `cd server`
- `export FLASK_CONFIG=development`
- `export FLASK_APP=run.py`
- `flask run`

### How to install client
- `cd client`
- `nvm use v14.19.3`
- `npm i`

### How to start client
- `npm run dev` -- // start dev server,
- `npm run build` -- // build for production
- `npm run serve` -- // locally preview production build



### How to start everything - TBD

## What I used as tutorials
 - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
 - https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
 - 
Login flow: 
- https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-5-creating-user-models
- https://betterprogramming.pub/a-detailed-guide-to-user-registration-login-and-logout-in-flask-e86535665c07


Dockerization:
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#nginx
https://www.patricksoftwareblog.com/how-to-configure-nginx-for-a-flask-web-application/

Flask login:
https://github.com/flatcoke/flask-structure
https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy#prerequisites
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-6-configuring-the-database
https://www.freecodecamp.org/news/how-to-authenticate-users-in-flask/