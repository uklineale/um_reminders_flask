#UM Reminders
This app sends out Urban Ministries Open Door Clinic reminders. It does so by taking in a CSV file with a phone number and a message. Most functionality is in `app/` in `app/classes` and `app/views.py`.

To start the app, grant `build.py` permission to execute and run the script. 

Environment variables that must be set are:
-UM_PASSWORD - the password for your app. Make it strong!
-UM_USERNAME - your Bandwidth user id. Contact Pablo Escobar or the current head of your Urban Ministries chapter 
-UM_TOKEN - your Bandwidth token
-UM_SECRET - your Bandwidth secret
-UM_NUMBER - your Bandwidth number

I hope the code is commented clearly enough, but if not feel free to reach out to me at neelk1123@gmail.com
