# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life

## Youtube Video Stream Preparer

Hallelujah, this will set up YouTube's broadcast title and description for a stream that will be at that moment God
willing.

## How to use

1. Make a virtual environment `python3 -m venv venv_chirho` in this directory and activate it `. venv_chirho/bin/activate`
2. Install all the dependencies `pip install -r requirements_chirho.txt`
3. Set up [Google oauth2 Web credentials](https://developers.google.com/identity/protocols/oauth2) with access to youtube data api, that can redirect to `http://localhost:4422`.
4. Copy your `client_secret_*.json` from those credentials to the same directory as this script, name it
   `client_secret_chirho.json`
5. Copy sample file `stream_preparer_chirho.sample.yml` to `stream_preparer_chirho.yml` in the same directory as this script and fill it in with your
   desired video information and the stream id you want (TODO: Create new stream) that you will use the stream key from in for example OBS.
6. Run `stream_preparer_chirho.py`

#### And some Twitch instructions, aleluya

```shell
#For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
brew install twitchdev/twitch/twitch-cl  # Hallelujah on Macos
rehash
twitch configure
twitch token -u -s "channel:manage:broadcast"
twitch api get users -q login=loveJesusbrian  # Get broadcaster id...
twitch api patch channels -q broadcaster_id=257133600 -b '{"title":"aleluya"}'
```

#### Additional useful info

```shell
# Hallelujah download google cloud cli https://cloud.google.com/sdk/docs/install
# Hallelujah youtube api samples https://github.com/youtube/api-samples.git
pip3 install --upgrade pip
pip3 install --upgrade google-auth-oauthlib google-auth-httplib2
pip3 install google-api-python-client
```