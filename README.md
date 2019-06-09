# screening_project
A simple example of role based authentication system.
What can you find here:
* Custom User registration and login system with role based functionality
* Signup and Signin option with gmail
* Request tracking option
* Download PDF report
* API documentation with public endpoint
* Test code

### Prerequisites

Make sure you have installed Python 3 and pip

# Installation

1. Download or Clone the project
```
git clone https://github.com/kazinayem2011/screening_project_for_misfit.git
```

2. Install virtualenv.
```bash
pip install virtualenv
```

3. Create a virtual environment in the project directory.
```bash
cd <project_directory>
virtualenv venv
```

4. Start a virtual environment:
```bash
source venv/bin/activate
```

5. Install project requirements with **pip**:
```bash
pip install -r requirements.txt
```

6. Create a mysql database by naming 'misfit', make sure about password field on database connection in settings.py file and run the command
```bash
python3 manage.py migrate
```

7. Run the below mysql command in your database for creating 3 types of role. (Role has been used statically as their is no requirement for dynamic solution)
```bash
INSERT INTO `users_role` (`id`, `role_title`) VALUES
(4, 'Employee'),
(3, 'HR'),
(1, 'Manager');
```

# Run

Now run the development server by typing the next command, to stop the server just press **Ctrl + C**:
```
python3 manage.py runserver
```
