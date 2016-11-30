Isaac Díaz 2016

Notes:
------
- database used sqlite
- admin available (admin/covadonga18)
- one django app
- backend api two DocumentedViews classes Cards and Positions ( insert/delete/list elements )
  No updates
- frontend with angular + bootstrap
- api documentation automatically generated thought instropction, 
   searching for DocumentedView
- test code coverage 78% 
- total time spent 10h 30m
- possible improvements
      - use angular directives
      - frontend testing
      - update elements functionality
      - improve frontend usability
      - increase coverage


Deploy:
-------

- unpack
- install requirements
- python manage.py runserver port
- open browser


How to do coverage:
-------------------
- coverage run --source='.' manage.py test
- coverage html
- open browser in the html generated


Tasks:
======
- implement views logic (ok) 4h
- create documentation (ok) 1h
- create test+coverage (ok) 2h
- create fixtures  (ok) 10'
- create frontend (ok) 3h
- check deploy (ok) 10'

Description
=====
### Python – Full Stack Developer Test assignment
### Requirements
- Ubuntu 16.04
- Python 2.7
- Django 1.9
- Default Bootstrap 3 framework

### Time to delivery - max 2-4 h for Backend part

### Problem description

Barcelona 2020 has been predicted to be the most attractive touristic city. To better handle
more significant amounts of tourists, the IT department designed “BCN ID Tourists cards” which
would help in smoothing dynamic resources management. Each tourist will be given an unique
ID NFC / WIFI / GPS card which will be updating the tourist department with their current
location. Having such data the tourist department will be distributing more efficient
communication resources (such as buses, trams, taxis). You have been selected to write a
backend for such system!

## Requirements

As a result we expect two separate projects:

### Backend

A Django backend app that is being served by a REST API, providing the basic operations for
the tourist office (add/update tourist data, and querying for tourists within the system)

### Frontend (optional)

A frontend app to provide a Web-based interface to handle such operations seamlessly, using
the REST API mentioned before. You can implement it the way you want, based on the platform
and language of your choice (for instance, Python/Django- or JavaScript- based)."
Example applications should contain (whenever its applicable):

- necessary models to handle tourist and all related objects
- fixture with an example tourists data
Task delivery
- Your solution will be executed on plain Ubuntu 16.04 host.
- If there is a necessity to install some software – let us know, preferably way by sudo apt- get
install
- All necessary python modules should be installable through requirements.txt
- Archived solution with documentation send to xxxxx

### Task evaluation
During the task evaluation we will pay attention to the following:
- Unittests
- Code quality (standards like PEP8)
- Documentation quality (write which documentation format you follow and why)

Good luck!