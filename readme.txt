#Install
* Add django_cohorts to the installed apps in your settings file.
* Add to your urls.py

#Setup
In metrics.py create a function for the analysis you want to make. 
There is an example in there for analyzing logins for the group.
You are passed a queryset of user objects and must return a float.
