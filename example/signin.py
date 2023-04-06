import time

from stretch import Stretch


def main():
    print("Start singin example")
    stretch = Stretch(
        base_url="http://localhost:8000", client_id="2f9445b3-5266-45cd-8a85-d5c3fff69781", profiling=True
    )
    time.sleep(1)
    # login = stretch.auth.login("bell", "123456")
    login = stretch.auth.guest()
    print("Login:", login)
    if login:
        resp = stretch.auth.get_user()
        # resp = stretch.auth.put_user(gender="female")
        # resp = stretch.auth.post_guest()
        # resp = stretch.auth.post_phone_check()
        # resp = stretch.auth.post_verify_phone()
        # resp = stretch.auth.put_verify_phone()
        print("User: info:", resp)
        # resp = stretch.auth.user()
        # print("User: info:", resp)

        coaches = stretch.search.post()

        print("Coaches:", coaches)


if __name__ == "__main__":
    main()
