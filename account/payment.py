import stripe

from payment_method.models import(
    Charge
) #new

#my stripe
stripe.api_key = 'sk_test_51Mei6tA4Xf1XOr7ROyXtE7oBA3CUKjMg3jhpbjcc9EgCzFENvPxQfRxe0caqLIvHokpUNwLEazVeJMmkeHgW6G1y00fHxP7I11'

#client stripe
#stripe.api_key = 'pk_live_51KH8ijFQRvmRrSikRd1spAjHsW9D18eN8Sx8XpvolnHWbtiajBHT4klGOSLUdgEfHazQIHBTgw5IxnznGcWMIw8R00kwdrZrEk'


def subscription(amount, user, token):
    

    # Create a charge on Stripe
    #amount = request.data['amount']
    
    charge = stripe.Charge.create(
        amount=int(amount * 100),
        currency='usd',
        source=token
    )

    # Create a charge in the database
    Charge.objects.create(
        amount=amount,
        stripe_charge_id=charge.id,
        user=user
    )