import os

from stretch import Stretch

client_id = os.getenv("MY_ACCOUNT_CLIENT_ID", None)
base_url = os.getenv("STRETCH_API_URL", "https://api.stretch.com")


def main():
    print("Start guest example")
    stretch = Stretch(base_url=base_url, client_id=client_id, profiling=True)
    guest = stretch.auth.guest()
    print("Guest auth credentials:", guest)
    if guest:
        # Get coaches by coords [lat, lng]
        coaches = stretch.search.post(lat=None, lng=None)

        print("Coaches:", coaches)


if __name__ == "__main__":
    main()
