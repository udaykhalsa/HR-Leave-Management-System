On linux/mac
```
source hr_management_env/bin/activate
```
in the root folder


Create a superuser/admin with
```
python manage.py createsuperuser
```

Employees/users can ONLY be added via admin panel.
Employee logged in will be redirected to page where they can apply for leave and see the status of the leave they've applied for.
Admins logged in will be redirected to page where they can all the leave applications and can approve or deny them.

Employees can only log in between 9am to 6pm.
