# Zerolab

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 	![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

![Alt Text](https://github.com/Vadzim-py/Zerolab/blob/main/static/img/slides/index.png?raw=true)

## Description

It is my first django project, which is a website with articles and short descriptions referring to documentation from official sources or forums with which it was created.

![Alt Text](https://github.com/Vadzim-py/Zerolab/blob/main/static/img/slides/articles.png?raw=true)

Registration, user management and bookmarks are written with functional view.

![Alt Text](https://github.com/Vadzim-py/Zerolab/blob/main/static/img/slides/profile.png?raw=true)

Besides django admin the project has its own crud by users, products and categories. These parts of the project are written in class-based views.

![Alt Text](https://github.com/Vadzim-py/Zerolab/blob/main/static/img/slides/admin.png?raw=true)

The project has reviews and ratings from registered users.

![Alt Text](https://github.com/Vadzim-py/Zerolab/blob/main/static/img/slides/reviews.png?raw=true)


## Installation

1. Clone the repository:

```bash
git clone https://github.com/Vadzim-py/Zerolab.git
```

2. Navigate to the project directory:

```bash
cd Zerolab
```

3. Create a virtual environment:

```bash
python3 -m venv env
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate # On Unix or MacOS
.\env\Scripts\activate  # On Windows
```

5. Install the requirements:

```bash
pip install -r requirements.txt
```

6. Run migrations:

```bash
python manage.py migrate
```

7. Start the server:

```bash
python manage.py runserver
```

## Usage

Once the server is running, you can access the application by navigating to `http://localhost:8000` in your web browser. There you can create an account, log in and manage it, leave comments and ratings. For managing create an superuser:
```bash
./manage.py createsuperuser
```

## Contributing

If you'd like to contribute to Zerolab, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.
