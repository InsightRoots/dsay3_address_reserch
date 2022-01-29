from serch import search_address


def main():
    zipcode = '0287111'
    address = search_address(zipcode)
    # print(address)
    assert "岩手県八幡平市大更" == address

#     チェックをするために、アサートをやっている。


if __name__ == '__main__':
    main()
