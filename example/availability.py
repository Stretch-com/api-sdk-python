import os
import time
from pprint import pp
import logging
from stretch import Stretch

client_id = os.getenv("MY_ACCOUNT_CLIENT_ID", None)
base_url = os.getenv("STRETCH_API_URL", "https://api.stretch.com")

client_id = "2f9445b3-5266-45cd-8a85-d5c3fff69781"
base_url = "http://localhost:8000"


logging.basicConfig(level=logging.INFO)


def coverage_test(stretch):
    resp = stretch.coach.post_availability(
        title="Availability slot", startSlot="13:30", endSlot="17:30", slotType="monday"
    )
    pp(resp)


def main():
    print("Start availability example")
    stretch = Stretch(base_url=base_url, client_id=client_id, profiling=True)

    # login = stretch.auth.login("coach0", "123456")
    login = stretch.auth.login("bell", "123456")

    if login:
        resp = stretch.auth.get_user()
        pp(resp)
        resp = stretch.coach.get_availability()
        pp(resp)
        resp = stretch.coach.post_availability(
            title="Availability slot", slot_start="13:00", slot_end="17:30", slot_type="monday"
        )
        pp(resp)

    return


if __name__ == "__main__":
    main()
