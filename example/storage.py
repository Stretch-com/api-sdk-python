import os

from stretch import Stretch

client_id = os.getenv("MY_ACCOUNT_CLIENT_ID", None)
base_url = os.getenv("STRETCH_API_URL", "https://api.stretch.com")

base_url = "http://localhost:8000"
client_id = "2f9445b3-5266-45cd-8a85-d5c3fff69781"


def main():
    print("Start storage example")
    stretch = Stretch(base_url=base_url, client_id=client_id, profiling=True)
    login = stretch.auth.login("bell", "123456")
    print("User auth credentials:", login)
    if login:
        # Get coaches by coords [lat, lng]
        info = stretch.auth.get_user()
        print(info)

        certificates = stretch.storage.get_certificates()
        print(certificates)

        if len(certificates) == 0:
            cert = stretch.storage.post_certificate(
                file="https://www.ti.com/lit/ds/symlink/tps61197.pdf",
                filename="TPS61197.pdf",
                title="Test save",
                issue_date="2003-12-22",
            )
            print(cert)
        else:
            cert = certificates[0]

            cert_uodate = stretch.storage.put_certificate(cert.id, title="Opa no title")
            print(cert_uodate)

            stretch.storage.delete_certificate(cert.id)

        # coaches = stretch.search.post(lat=None, lng=None)


if __name__ == "__main__":
    main()
