# send-email-smtp
This is python script written to send customized emails

before using this files :

Step 1 : you should have a google account

step 2 : Then if you are finding this tutorial in 2020 then turn on 2-step verification at this link => https://myaccount.google.com/security

Step 3 : For the developers who want to send mass emails or email to specific users or a selected user , you have to visit this link
https://myaccount.google.com/apppasswords

  3.1 : After visitng , select the right option which suits your demand(Select the app and device you want to generate the app password for)
  3.2 : I have selected  "app" :"mail" and "device": "windows computer" because my requirement was to send email from python code running on my windows os. Likewise select that
  
  3.3 You will be prompted with password , just make a note of this somewhere.

Step 4: Then open python files listed in this github repo.

Step 5: just change EMAIL_ADDRESS to your current google email with which you registered your app.
      just change EMAIL_PASSWORD to the password you got in the step 3.3
      
Step 6: You are good to go.
There will be 4 files depending on the features it gives:
1. simple.py : - it will just send subject and message to intended receiver .
2. images.py : - modified a little bit as it will send images also . You can add multiple images:D
3. pdf.py    : - This will attach pdf to email and deliever to reciever. While running this file, it may take some time depending on the size of pdf.
4. customized.py: - in this you can customize your code according to your wish using html format to customize the message.

