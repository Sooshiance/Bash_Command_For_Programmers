# Portfolio

This is a full rest api Portfolio using Django rest framework and React.

I used **`Service Repository`** design pattern for its backend.

I handled **testing** scenarios in simple but insightful way in backend.

I used **best practice** of Django to modify its `settings`.

# Backend(using django-admin)

We have 4 major app.

- **`user`**: We handled authentication flow in <a href="#user">user</a>
- **`project`**: We handled project, post etc. flow in <a href="#project">project</a>
- **`dash_board`**: We handled admin statistics flow in <a href="#dash_board">dash_board</a>
- **`club`**: We handled Rating, Review etc. flow in <a href="#club">club</a>

Let's deep dive into these apps one by one:

## user app

We have three models:

- **`User`**

This model have `email` field for authentication and some other required fields for registering flow.

- **`Profile`**

This model will let users to modify or delete their accounts and give other developers information about them.

- **`OTP`**

This model will handle **Reset Password** scenario.

## project app

We have 8 models:

- **`Project`**: 

 This model will let users add their own project into your **Portfolio**.

- **`Post`**: 

 This model Will let users share their thoughts with other developers.

- **`Skill`**: 

 This model will let users add their skills and its level of how good at that skill.

- **`Testimonial`**: 

 This model will let users display testimonials from clients or colleagues.

- **`ContactMessage`**: 

 This model will let users allow visitors to send messages to you.

- **`Education`**: 

 This model will let users display their educations.

- **`Experience`**: 

 This model will let users list their work experience, including job titles, companies, etc.

- **`Certification`**: 

 This model will let users showcase any certifications or courses you have completed

This app and its related models are the heart of **Portfolio**.

## dash_board app

In this app, there is no models but, I handled some queries for you with **OOP** programming concept.

For now, I have created these classes:

- **`ProjectQuery`**: In this class I'v created two `static method` one for counting created projects in a duration for example from 1st September till 30 September, and the other query is an **`Advanced Search`** for users to search any project either with its title or description

- **`PostQuery`**: This class only has one method and that is a method to count how many `posts` created in one day.

## club app

We have 6 models:

- **`Statistic`**: 

This model will let users know statistics like the number of projects completed, years of experience.

- **`GalleryItem`**: 

This model will let users showcase images or media related to your work or interests.

- **`Service`**: 

This model will let users list their services like offers etc.

- **`Event`**: 

This model will let users list participate in or host events.

- **`FAQ`**: 

This model will show users some predefined questions.

- **`Subscriber`**: 

This model will let users allow visitors to subscribe to your newsletter.

## Test Scenario

As you can see, I'v deleted the **test.py** file in all apps but, I created a folder that has two files:

- **`test_models`**: I'v added this file because First we need to check the models integrity. 

- **`test_views`**: I'v added this file to make sure our endpoints work just fine.

### Run Portfolio backend

First in for most, I'v deleted the **settings.py**. In backend folder we have another folder named **settings**.

In that folder, first look at the **`__init__.py`** file and as you can see, I have three main files :

- **`__init__.py`**: Since Django first look at this file, we just import the important settings based on **DEBUG** value.
- **`base.py`**: will keep the root of the project
- **`develop.py`**: will keep the development settings. These settings are just the basics of any testing project
- **`production`**: will keep most important settings like **Database** and its connection, handle **JWT** token in production and its security concerns, **Logging** flow to log everything for you and other settings.

Now you have a full overview of how settings work.

To run this project in develop mode: 
- fill up `SECRET_KEY` and other settings that replaced by `config` .
- If you prefer `Postgresql`, make sure the connection and its necessary dependencies.

Run these commands:
- Linux/Mac:

        python3 manage.py makemigrations

        python3 manage.py migrate

        python3 manage.py test

        python3 manage.py createsuperuser

        python3 manage.py runserver

- Windows:

        python manage.py makemigrations

        python manage.py migrate

        python manage.py test
 
        python manage.py createsuperuser

        python manage.py runserver

# Frontend(using yarn)
