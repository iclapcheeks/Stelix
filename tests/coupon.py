import stelix

sellix = stelix.Sellix(
    secret_key='SECRET_KEY'
)

coupon = sellix.request(
    method='create', # What you want to do, in this case we want to create a new coupon code
    endpoint='coupon', # The API Endpoint you are trying to access

    code='stelix is awesome',
    discount_value=0.15,
    max_uses=5,
    products_bound=[
        'stelix2021abc'
    ]

    # Passing the arguments required to create the coupon code, some are
    # required while some are not, read more at https://developers.sellix.io
)

print(coupon['data']['uniqid']) # Getting the ID of the newly created coupon code
