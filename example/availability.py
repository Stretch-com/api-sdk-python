import os
import time

from stretch import Stretch

client_id = os.getenv("MY_ACCOUNT_CLIENT_ID", None)
base_url = os.getenv("STRETCH_API_URL", "https://api.stretch.com")

client_id = "2f9445b3-5266-45cd-8a85-d5c3fff69781"
base_url = "http://localhost:8000"


def main():
    print("Start availability example")
    stretch = Stretch(base_url=base_url, client_id=client_id, profiling=True)

    #login = stretch.auth.login("coach0", "123456")
    login = stretch.auth.login("bell", "123456")

    if login:
        resp = stretch.auth.get_user()
        print(resp)
        resp = stretch.coach.get_availability()
        print(resp)
        # resp = stretch.storage.post_image(url, "title image")
        # print(resp)

    return


if __name__ == "__main__":
    main()
