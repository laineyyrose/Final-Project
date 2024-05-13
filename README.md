<img width="637" alt="Screenshot 2024-05-12 at 8 25 48 PM" src="https://github.com/laineyyrose/Final-Project/assets/122582580/36f93df2-aaa2-425c-914f-64ffe6280f6f"># Four Winds Thrift
This is a project by Lainey Rose and Andy Trinh for the Spring 2024. Four Winds Thrift is a commerce-focused platform designed to give New College students a specific site for selling and buying from each other. The goal of the project is to have an accessible, sustainable, and social experience in the New College second-hand market.

## Installation Instructions
Four Winds Thrift should be hosted at http://fourwindsthrift.pythonanywhere.com/, but if that isn't the case, you can run it on localhost.

### Local Host

1. Fork/clone/download this repository.

```
git clone https://github.com/laineyyrose/Final-Project
```

2. Navigate to the directory.

```
cd Final-Project
```

3. Create a virtual environment for this project. This example uses `venv` as the name.

```
python3 -m venv venv
```

4. Load the virtual environment.
    - On Windows Powershell: `.\venv\Scripts\activate.ps1`
    - On Linux and Git Bash: `source venv/bin/activate`

5. Run `pip install -r requirements.txt`.

6.  You may have to make migrations in order to work the program. In that case run:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Then run `python manage.py runserver`. The console should indicate where it's being hosted. Usually this is `http://127.0.0.1:8000/`. Open this in a browser as it's running and you should be able to access the site. Ctrl+C in the console will quit the program.

### Deploying
There are a lot of different ways to deploy a Django site. For this project we used a free [PythonAnywhere](https://www.pythonanywhere.com) plan, so the deployment examples will centered around what we did. You can also view [PythonAnywhere's own deployment instructions](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject).

1. Create an account with PythonAnywhere. You may want your username be named after your project. A free PythonAnywhere plan uses the users' username in this format: `username.pythonanywhere.com`.

2. Assuming you're using our github or a clone/fork, open a bash script from the PythonAnywhere dashboard. In the bash, clone the github repository using `git clone https://github.com/laineyyrose/Final-Project` (or the url of your repository). There are also [other methods](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles) for uploading your files.

3. Navigate to the directory.

```
cd Final-Project
```

3. Create a virtual environment for this project. This example uses `venv` as the name.

    - This project is a big install for a free plan. To get around this you may want to add the `--system-site-packages` flag for the creation of a virtual env, as things like pandas and numpy are already installed on the PythonAnywhere.

```
$ mkvirtualenv --python=/usr/bin/python3.10 venv

or 

$ mkvirtualenv --python=/usr/bin/python3.10 venv --system-site-packages
```

To activate this virtual environment if it's not activated, use `$ workon venv`.

4. Create a web app under the web tab using the "Manual Configuration" option. Enter the name of your virtual environment under the "virtualenv" header where the input box is.

5. Edit the WSGI file provided in the code section to uncomment the Django section at the bottom. 

6. In your project's settings.py file, add the url of the site to the  `ALLOWED_HOSTS` list. You can access your files in the files tab. 

7. You'll have to set up your database. Run `python manage.py migrate`. It's also recommended that you run `python manage.py collectstatic` and set up static urls to make sure your static elements may work. Click the circular arrow (reload) button at the top. You should then be able to click on the link in your webtab and view a working app. 

**Pushing and pulling from your project in PythonAnywhere**

PythonAnywhere recommends using SSH keys to be able to push and pull to your project, but this is only limited to paid accounts on PythonAnywhere. Pulling can be done easily, but pushing is a little more difficult without SSH set up.

To do this without paying, you'll want to configure the git in PythonAnywhere with your information. 

Run: 
```
git config --global user.email "Your Email"
git config --global user.name "Your Name"
```

Your Github name should be what's in your profile's name field, NOT your username.

Create a [personal access token (classic)](https://docs.github.com/en/enterprise-server@3.11/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for your Github account. Store this somewhere safe.

Go back to your bash script and run `git push origin branchname`. You'll be prompted for your username and password. Enter your Github username as your username, but **enter your personal access token when prompted for your password**. This should allow you to push to the remote repository. 


## Resources

LAINEY:
(I used this playlist and his github for most of the user functions)
https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi 
https://github.com/danielkim2711/simple-blog.git

https://docs.djangoproject.com/en/5.0/topics/auth/default/
https://www.youtube.com/watch?v=H_cWdD-aXCQ&t=164s
https://www.youtube.com/watch?v=WuyKxdLcw3w&t=3256s
https://www.youtube.com/watch?v=FdVuKt_iuSI
https://forum.djangoproject.com/t/showing-method-not-allowed-get-users-logout/26044
https://stackoverflow.com/questions/60159817/django-database-migration-not-working-new-table-not-created
https://medium.com/@mustahibmajgaonkar/how-to-reset-django-migrations-6787b2a1e723
https://stackoverflow.com/questions/65744877/noreversematch-at-reverse-for-profile-with-arguments-not-found-1-pa
https://pylessons.com/django-login-logout


## Trailer
https://github.com/laineyyrose/Final-Project/assets/122582580/9f93b8d3-afa7-4aac-bf3d-eccf6aafa039


## Demo Video
[![Watch the video](https://www.youtube.com/watch?v=cWF2I7bIBWk)]


## System Architecture

<img width="417" alt="System Architecture" src="https://github.com/laineyyrose/Final-Project/assets/122582580/2574f33a-0812-4612-8f10-18afa452b04d">


## UML Diagram

<img width="437" alt="UML" src="https://github.com/laineyyrose/Final-Project/assets/122582580/f92cf6b9-213b-4dde-be5c-248055f3ba9b">

