Requirements:
- Python >= 2.6
- MySQL
- Django >= 1.0.4

Installation:
Types_database is a django application. In order to run it, you need to:
- Edit settings.py
- You can unpack database release (unpack data_files to media directory and
recreate the database)
- run:
python manage.py syncdb
- run:
python manage.py runserver 8000
