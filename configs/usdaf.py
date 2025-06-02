topic0 = "0x962110f281c1213763cd97a546b337b3cbfd25a31ea9723e9d8b7376ba45da1a"

branches = {
    "scrvUSD": {
        "trove_manager": "0xa0290af48d2E43162A1a05Ab9d01a4ca3a8B60CB",
        "price_feed": "0x629b6c0DcDf865584FD58a08727ABb9Db7390e28",
    },
    "sDAI": {
        "trove_manager": "0x7F1171686e6028c321517EdB6DD70321164b6343",
        "price_feed": "0xC470A1574B469A562fb237e289FDb217f8C14dc9",
    },
    "sUSDS": {
        "trove_manager": "0x2ba8e31b6C1C9f46046315406E840dBabeA803a8",
        "price_feed": "0x806B2921E394b3f84A549AB89CF73e57F0C882c5",
    },
    "sfrxUSD": {
        "trove_manager": "0x53A5DE1b94d7409F75FFF49fd81A823fb874BF71",
        "price_feed": "0xcDA8ccA990afF26fD8298e0d30304E4d01F7B387",
    },
    "sUSDe": {
        "trove_manager": "0x9dc845b500853F17E238C36Ba120400dBEa1D02A",
        "price_feed": "0x0DAaFdDcf74451caec724Bcd2f0d7E4025C95B94",
    },
    "tBTC": {
        "trove_manager": "0x64454C84Dc289C7CDe7E2eE2F87Ae1196bC9cD36",
        "price_feed": "0xCe1Ca28e54fD3BD431F893DDFFFa1bd619C0517e",
    },
    "WBTC": {
        "trove_manager": "0x085AbEe74F74E343647bdD2D68927e59163A0904",
        "price_feed": "0x4d349971C23d6142e8dE9dEbbfdBB045B7AAbA49",
    },
    "cbBTC": {
        "trove_manager": "0x0291C873838F7B62D743952D268BEbe9ace1efa4",
        "price_feed": "0xAF99E6Cf5832222C0E22eF6bf0868C4Ed7f2953F",
    },
}

filters = [
    {"address": [branch["trove_manager"]], "topics": [topic0]}
    for branch in branches.values()
]
