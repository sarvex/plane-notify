def getMap(mapLocation, file_name):
    import requests
    import configparser
    config = configparser.ConfigParser()
    config.read('./configs/mainconf.ini')
    api_key = config.get('GOOGLE', 'API_KEY')
    url = "https://maps.googleapis.com/maps/api/staticmap?"

    center = str(mapLocation)
    zoom = 9

    r = requests.get(
        f"{url}center={center}&zoom={zoom}&size=800x800 &key={api_key}&sensor=false"
    )

    with open(file_name, 'wb') as f:
        # r.content gives content,
        # in this case gives image
        f.write(r.content)