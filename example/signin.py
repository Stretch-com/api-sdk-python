from stretch import Stretch


def main():
    stretch = Stretch(client_id="2f9445b3-5266-45cd-8a85-d5c3fff69781")

    resp = await stretch.auth.token("bell", "123456")


if __name__ == "__main__":
    main()
