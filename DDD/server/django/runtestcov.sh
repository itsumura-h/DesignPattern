python manage.py migrate models zero --settings=project.settings.test
python manage.py migrate --settings=project.settings.test
yes yes | coverage run manage.py test --settings=project.settings.test --keepdb
rm htmlcov/*
coverage html
