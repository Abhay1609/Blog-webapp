<!-- Add a title with an icon -->
<div align="center">
  <img src="https://logo.com/image-cdn/images/kts928pd/production/f8930dc16b61049931afec210ae32d614e763895-345x348.png?w=1080&q=72" alt="Your Icon" width="100px" height="100px">
  <h1>Blog Webapp</h1>
</div>

<!-- Table of Contents -->
## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

<!-- Project Description Section -->
## Project Description

The Blog WebApp is a powerful and versatile content management system (CMS) built using Django, designed to simplify the process of creating and managing blogs. Whether you're a writer, blogger, or content creator, our platform provides a seamless and intuitive experience to publish and share your thoughts with the world.

<!-- Features Section -->
## Features

1. **User-Friendly Dashboard**: A user-friendly dashboard that makes it easy to manage your blog.

2. **Multi-Author Support**: Support for multiple authors with individual profiles.

3. **Admin Tools**: Feature-rich admin tools for efficient management.

<!-- Prerequisites Section -->
## Prerequisites

- Python 3.x
- Django 3.x

<!-- Installation Section -->
## Installation

```shell
# Clone the repository
git clone https://github.com/Abhay1609/Blog-webapp/

# Change into the project directory
cd Blog-webapp

# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Linux/macOS)
source venv/bin/activate
```
## Configure environment variables
```shell
export SECRET_KEY='your-secret-key'
export DEBUG=True
export DATABASE_URL='your-database-url'

# Modify Django settings if necessary


# Install project dependencies
pip install -r requirements.txt
python manage.py migrate
```
##Usage
```shell


python manage.py runserver

```



