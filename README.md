# Image Gallery

Store, organize, and relive your memories with albums – just like Google Photos.

## Features
User Authentication (Register, Login, Logout, Profile Update)

- Upload and View Images
- Create and Manage Albums
- Move Images to Trash and Restore/Delete from Trash
- Bulk Actions on Images
- Password Reset and Change Support
- Responsive UI using Bootstrap 5
- Custom Admin for images

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** Bootstrap 5 + HTML Templates
- **Database:** SQLite (default)
- **Other:** Django Messages Framework, Static Files


##  Installation Guide for To do App Project

### 1. Clone the repository
git clone https://github.com/Darpan-Anjanay/ImageGallery.git  # Download the project from GitHub
cd ImageGallery  # Move into the project directory

### 2. Create a virtual environment
python -m venv venv  # Create a virtual environment named 'venv'

### 3. Activate the virtual environment

venv\Scripts\activate  # For Windows

### 4.Install the project dependencies
pip install -r requirements.txt  # Install all required packages listed in requirements.txt

### 5. Set up the database
python manage.py makemigrations  # Generate migration files based on the models
python manage.py migrate  # Apply the migrations to create the database schema

### 6. Create a superuser for accessing the Django admin panel
python manage.py createsuperuser  # Follow the prompts (username, email, password)

### 7. Run the development server
python manage.py runserver  # Start the local server

###  Now, open your browser and go to: http://127.0.0.1:8000/
###  To access the admin panel, visit: http://127.0.0.1:8000/admin/
 


## Author

- **Name:** Darpan Anjanay
- **GitHub:** https://github.com/Darpan-Anjanay/


## Screenshots

### Register Page
![Register Page](/screenshots/register.png)

### Login Page
![Login Page](/screenshots/login.png)

### Home Page
![Home Page](/screenshots/home.png)

### Album View
![Add Image Page](/screenshots/albumview.png)

### Upload Image
![Upload Image Page](/screenshots/upload.png)


###  Image View
![ Image View](/screenshots/imgview.png)


###  Trash View
![ Trash View](/screenshots/trash.png)


###  Admin View
![ Admin View](/screenshots/admin.png)

