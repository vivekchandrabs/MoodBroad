# MoodBroad

# api.speckbit

## Getting Started with the Project

To get started with the project:
    
     $ git clone https://gitlab.com/speckbit/api.speckbit.com.git

To install all dependencies, create a new virutalenv with your preferred plugin and do:

      $ pip install -r requirements.txt
      
To run the project, Go to the root folder and run
 
      $ python manage.py runserver
 
## Api end point documentation:

Authentication urls

| Api end-point   | Method | Function            | Argument| Description                                   | Response| 
| --- ------------| --- | ------------------- | ------- | -----------------------------------------------------------|
| /auth/register/ | GET | UserRegisteration() | "email" | Sends a verification email | json with a message and email |


 
