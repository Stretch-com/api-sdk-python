import os
import time

from stretch import Stretch

client_id = os.getenv("MY_ACCOUNT_CLIENT_ID", None)
base_url = os.getenv("STRETCH_API_URL", "https://api.stretch.com")


def main():
    print("Start singin example")
    stretch = Stretch(base_url=base_url, client_id=client_id, profiling=True)
    time.sleep(1)

    username = "coach-test2"
    phone = "+999111111112"
    password = "123456"

    login = stretch.auth.login("coach0", "123456")

    if login:
        resp = stretch.auth.get_user()
        print("user:", resp)
        url = "/Users/iuriibell/dev/api-stretch/test.jpeg"
        url = "https://www.denofgeek.com/wp-content/uploads/2022/05/Leged-of-Zelda-Link.jpg"
        resp = stretch.storage.post_avatar(url)
        print(resp)
        # resp = stretch.storage.post_image(url, "title image")
        # print(resp)

    return
    session = stretch.auth.signup(phone, "coach")
    print("signup session:", session)
    if session:
        verify = stretch.auth.post_verify_phone(session)
        print("verify create:", verify)
        check = stretch.auth.put_verify_phone(verify.sid, "0000")
        print("verify check:", check)
        complete = stretch.auth.put_complete(
            gender="male", password=password, username=username, firstNmae="Test1", lastName="last"
        )
        print("complete:", complete)


if __name__ == "__main__":
    main()
