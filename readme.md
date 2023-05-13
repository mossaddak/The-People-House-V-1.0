# Sing up
post => http://127.0.0.1:8000/api/account/sing-up/

required fields: 

    {
        "email":"ne33@gmail.com",
        "password":"1234",
        "first_name":"Mossaddak",
        "last_name":"",
        "subscription_type":"<Here will be subscription type>"
    }

<b>Note:</b> 
<p>
    if subscription type == "Liberty plan" then no token will be added,
    else will be added new field named "token" after "subscription_type" field. Here token means card number. Without payment no user will be able to get the entry permissions except "Liberty plan" subscriber.
</p>

    There is four subscription types:
        #Liberty plan
        #Patriot plan
        #Eagle plan
        #Stars and Stripes plan
        #Founding Fathers plan
    
<b>Note:</b> You can't change these, you have to keep these as it is and under a dropdown menu so that user can select subscription type as they want.


# Login
post => http://127.0.0.1:8000/api/account/login/

required fields:

    {
        "email":"ne33@gmail.com",
        "password":"1234"
    }


# Profile 
post, patch => http://127.0.0.1:8000/api/account/profile/

required fields:

    {
        "id": 2,
        "username": "ne33",
        "first_name": "Mossaddak",
        "last_name": "",
        "email": "ne33@gmail.com",
        "birth_date": null,
        "phone": null,
        "state": null,
        "city": null,
        "country": null,
        "political_affiliation": null,
        "num_of_national_election_voted": null,
        "num_of_state_election_voted": 5
    }


# Account Verification
-)First:

need to hit this url, user must need loged in. there is no need any field. after hit this user will get an otp through the email:

    post => http://127.0.0.1:8000/api/account/account-verify-code/

-)Second:

then you have to hit the below link with the otp you got through the email 

    post => http://127.0.0.1:8000/api/account/verify/

required fields:

    {
        "otp":"12279"
    }


# Reset Password Generate Token
post => http://127.0.0.1:8000/api/recovery-account/reset-password/

required fields:

    {
        "email":"demomail1@gmail.com"
    }


# Reset password
post => http://127.0.0.1:8000/api/recovery-account/reset-password-send-token/

required fields:

    {
        "password_reset_token":<here will be the token send by email>,
        "new_password":12345
    }


# Contact 
post => http://127.0.0.1:8000/api/contact/contact/

required fields:

    {
        "name": "Mossaddak",
        "email": "mossaddak@gmail.com",
        "subject": "Something",
        "message": "oke"
    }


# News Letter 
post => http://127.0.0.1:8000/api/main/newsletter/

required fields:

    {
        "email":"mossaddak@gmail.com"
    }


# Election Start
get => http://127.0.0.1:8000/api/main/election-start/


# Blogs
get => http://127.0.0.1:8000/api/blog/blogs/


# Blog Comment

<b><i>For All Comment</i></b>

get, post => http://127.0.0.1:8000/api/blog/comment/

required fields:

    {
        "comment": "new1",
        "blog": 1
    }

put,patch,get => http://127.0.0.1:8000/api/blog/comment/1/

Note: User needs to authenticate



# Invitation
post => http://127.0.0.1:8000/api/blog/blogs/

required fields:

    {
        "name": "Mossaddak",
        "email": "10000mossaddak@gmail.com",
        "state": "Dhaka",
        "phone": "45464564"
    }


# Payment Method
api_key = 

post => http://127.0.0.1:8000/api/payment_method/stripe-payment/

required field:

    {
        "amount": 34,
        "token": "4242424242424242"
    }


# How to create app password?
=)
    go to this link: https://myaccount.google.com/?hl=en_GB&utm_source=OGB&utm_medium=act

    then,

        security > 2 step verification > sing into your account > App passwords(it will get in bottom) > select app(other) > give a name > click generate

