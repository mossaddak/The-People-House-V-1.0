# Sing up
post => http://127.0.0.1:8000/api/account/sing-up/

required fields: 

    {
        "email":"ne33@gmail.com",
        "password":"1234",
        "first_name":"Mossaddak",
        "last_name":""
    }


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


# Invitation
post => http://127.0.0.1:8000/api/blog/blogs/

required fields:

    {
        "name": "Mossaddak",
        "email": "10000mossaddak@gmail.com",
        "state": "Dhaka",
        "phone": "45464564"
    }


# How to create app password?
=)
    go to this link: https://myaccount.google.com/?hl=en_GB&utm_source=OGB&utm_medium=act

    then,

        security > 2 step verification > sing into your account > App passwords(it will get in bottom) > select app(other) > give a name > click generate

