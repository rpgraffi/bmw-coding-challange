# Challenge:
Given a simple backend that returns a list of nearby sushi restaurants and parking garages for a user located in Marienplatz, Munich: https://github.com/mmiLabGarching/places-data
Let the user ask for either a sushi restaurant or a parking and then conversate with the LLM (gpt-3.5-turbo by OpenAI) about the dataset, i.e. the user may ask for details about the available points of interest like distance and payment methods.
It’s not required to be able to support both sushi and parking searches, but it would be nice.
The data is meant to mock a database, so please do not simply include the full json in the LLM prompt.

## Useful functions:
### General
set_user_interest(interest:Enum(UserInterest))

### Sushi Resturant
get_shushi_restaurants()

get_position(title:str)
get_business_hours(title:str)
get_reviews(title:str)
get_contact_info(title:str)
get_price(title:str)



### Parking
get_parking_spots()


It’s possible to use any feature of the Chat Completions API from OpenAI.
The front end can be of any form and shape: console script, web UI, jupyter notebook, android app, etc... (I will start with Python and then try to build a Kotlin Android App)
 
Please send your entire code until 10 PM via email (zip) on the evening before the exchange to us.