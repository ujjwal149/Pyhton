import requests
from datetime import datetime
import smtplib


MY_MAIL = ""
MY_PASSWORD = ""
MY_LAT = 30.7446
MY_LNG = 76.6525




#GET INTERNATIONAL SPACE STATION LOCATION.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json",timeout=5)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    #GET SUN RISE AND SUN SET TIME OF ANY PARTICULAR LATITUDE AND LONGITUDE.
    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T").split(":")[0])
    sunset = int(data["results"]["sunset"].split("T").split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return False


if is_iss_overhead() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_MAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_MAIL,
        to_addrs=MY_MAIL,
        msg="Subject:Look UP👆\n\nIss is above you in the sky."
    )
