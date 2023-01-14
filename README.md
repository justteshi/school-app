# PGPCHE UI
Mainly Html and Css styles applied.
## About
[Django](https://www.djangoproject.com/) project with:
## Screenshots
![PGPCHE Razgrad](https://user-images.githubusercontent.com/45295214/212446324-26d8127c-99c2-4840-ac1d-847a5f608886.png)

## Installation
 * Python 3.10
### Back-end
 1. Clone the repo
 ```bash
 git clone https://github.com/justteshi/school-app.git
 ```
 2. Create virtualenv
 ```bash
 cd my-project
 virtualenv env
 ```
 3. Activate virtualenv
* Mac OS / Linux
 ```bash
 source env/bin/activate
 ```
* Windows
 ```bash
 env\Scripts\activate
 ```
 4. Add dependencies
 ```bash
 pip install -r requirements.txt
 ```
 5. Navigate to the inner folder
 ```bash
 cd excelsiorclinic\
 ```
 6. Run migrations and create superuser for admin
 ```bash
 python manage.py migrate
 python manage.py createsuperuser
 ```
 7. Start development server
 ```bash
 python manage.py runserver
 ```
 8. Open browser and go to ```http://localhost:8000 ```
