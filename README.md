# Four Winds Thrift
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

ANDY:

OpenMeteo API: https://open-meteo.com/en/docs/#latitude=27.3364&longitude=-82.5306&current=temperature_2m,apparent_temperature&hourly=&daily=temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_probability_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FNew_York&forecast_days=1
Raincard: https://mdbootstrap.com/docs/standard/extended/weather/
Round Button Styling: https://codepen.io/jnbruno/pen/vNpPpW
Floating Action Button: https://codepen.io/Gogh/pen/XzrNZd
Inline Text Alignment: https://stackoverflow.com/questions/19871123/align-text-in-one-line
Forced Float Formatting with Input: https://html.spec.whatwg.org/multipage/input.html#the-step-attribute
Force Numbers in Number Input: https://stackoverflow.com/questions/18510845/maxlength-ignored-for-input-type-number-in-chrome
Django Docs:
Price Formatting on Display: https://docs.djangoproject.com/en/5.0/topics/i18n/formatting/#localize
Form Widget Styling: https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
Timezone Display: https://docs.djangoproject.com/en/5.0/topics/i18n/timezones/
Django URL Path: https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280
Post Details: https://tutorial.djangogirls.org/en/extend_your_application/
Image Preview: https://www.tutorialspoint.com/preview-an-image-before-it-is-uploaded-in-javascript
Deploy Disk Space Troubleshooting: https://www.pythonanywhere.com/forums/topic/27961/
Static Fix: https://blog.pythonanywhere.com/60/
GitHub Connect from PythonAnywhere Bash:
https://jss367.github.io/python-anywhere-and-git.html
https://docs.github.com/en/enterprise-server@3.11/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
Installation Documentation Format:
https://github.com/Datalux/Osintgram
https://github.com/Genymobile/scrcpy
Chat GPT Links:
Listings Feature & Forms Troubleshooting: https://chat.openai.com/share/76a10a00-5b84-4518-b838-5701d4102784
Items Pages: https://chat.openai.com/share/f8583589-49f8-47ff-8437-f31d64319790

## Trailer
https://github.com/laineyyrose/Final-Project/assets/122582580/9f93b8d3-afa7-4aac-bf3d-eccf6aafa039


## Demo Video
[![Watch the video]([https://i.stack.imgur.com/Vp2cE.png](https://www.google.com/imgres?q=youtube%20stock%20photos&imgurl=https%3A%2F%2Ft3.ftcdn.net%2Fjpg%2F03%2F00%2F38%2F90%2F360_F_300389048_dPZlxdHWAbKU1qD5Mt9jLB4eeh24K2Bo.jpg&imgrefurl=https%3A%2F%2Fstock.adobe.com%2Fimages%2Fyoutube-logo-on-a-white-background%2F300389048&docid=RnoYP541VF6VLM&tbnid=Sl4okNBMEvqheM&vet=12ahUKEwi1rPm-r4mGAxUETDABHV7FD7UQM3oECE8QAA..i&w=540&h=360&hcb=2&ved=2ahUKEwi1rPm-r4mGAxUETDABHV7FD7UQM3oECE8QAA))](https://www.youtube.com/watch?v=cWF2I7bIBWk)

## System Architecture

<img width="417" alt="System Architecture" src="https://github.com/laineyyrose/Final-Project/assets/122582580/2574f33a-0812-4612-8f10-18afa452b04d">


## UML Diagram

<img width="437" alt="UML" src="https://github.com/laineyyrose/Final-Project/assets/122582580/f92cf6b9-213b-4dde-be5c-248055f3ba9b">

