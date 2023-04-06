from stretch import Stretch
import time


def main():
    stretch = Stretch(base_url="http://localhost:8000", client_id="2f9445b3-5266-45cd-8a85-d5c3fff69781")

    login = stretch.auth.login("bell", "123456")
    print("Login:", login)

    if login:
        resp = stretch.auth.user()


if __name__ == "__main__":
    main()
