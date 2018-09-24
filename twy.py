import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="aHtGWhDgKtBTfohXBe9gMdUgh"
consumer_secret="pSpOjgCvKcoW9ZmLtfrzKk4JpA7604VLlA0N5Thz2CvPEMk344"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="710845973400915968-rexTM2eE79GX0PvX10Ervme2pbMTXFE"
access_token_secret="9jC9udCr8GAXqLzvA8WAKJG8VvchAVl8HQWziF3oaIRq8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
