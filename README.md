# django-blog
django blog demo project

## About:

This is demo project for practicing Django. The idea was to build some basic blogging project. 
There is login and signup functionality included
User has his own blog page, where he can add new blog posts, edit blog post. 
Admin can add new blog, edit blog, and delete the existing blog, and view the all blog. Home page is paginated list of all blog posts.
Non-authenticated users can see all blog posts, but cannot add new posts
	
## quick start:

To get this projects up and running locally on your computer.

1)Assumming you hav python setup run the following commond:

python manage.py makemigrations 

python manage.py migrate  

python manage.py createsuperuser 

2)Open a browser to http://127.0.0.1:8000/admin/auth/group/ to open admin site. Create group Admin and Author

3)Then run demo project :

python manage.py runserver 
