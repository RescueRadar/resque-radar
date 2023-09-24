## Installation

### Prerequisites

- [Django](https://www.djangoproject.com/)
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
  
### Clone

- Clone this repo to your local machine using the following command:

```shell
https://github.com/RescueRadar/resque-radar
```

### Setup

- You can either create a virtual environment or install the dependencies globally. We recommend using a virtual environment. To create a virtual environment, run the following command:

```shell
python -m venv venv
source venv/bin/activate
```

- Download the dependencies using the following command:

```shell
pip install -r requirements.txt
```

- Create a `.env` file in the root directory and add the following environment variables:

```shell
DB_USER="your_db_username"
DB_HOST="your_db_host"
DB_PASSWORD="your_db_password"
DB_NAME="your_db_name"
```

- Run the following commands to create the database and apply migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```

- Create a superuser to access the admin dashboard using the following command:

```shell
python manage.py createsuperuser
```

- Run the following command to start the server:

```shell
python manage.py runserver 0.0.0.0:8000
```

- You can now access the site at `http://localhost:8000/`.