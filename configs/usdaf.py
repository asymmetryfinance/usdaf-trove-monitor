topic0 = "0x962110f281c1213763cd97a546b337b3cbfd25a31ea9723e9d8b7376ba45da1a"

branches = {
    "ysyBold": {
        "trove_manager": "0xf8a25a2e4c863bb7cea7e4b4eeb3866bb7f11718",
        "price_feed": "0x7f575323ddedfbad449fef5459fad031fe49520b",
    },
    "scrvUSD": {
        "trove_manager": "0x7aff0173e3d7c5416d8caa3433871ef07568220d",
        "price_feed": "0xf125c72ae447efdf3fa3601eda9ac0ebec06cbb8",
    },
    "sUSDS": {
        "trove_manager": "0x53ce82ac43660aab1f80fecd1d74afe7a033d505",
        "price_feed": "0x2113468843cf2d0fd976690f4ec6e4213df46911",
    },
    "sfrxUSD": {
        "trove_manager": "0x478e7c27193aca052964c3306d193446027630b0",
        "price_feed": "0x653df748bf7a692555dcdbf4c504a8c84807f7c7",
    },
    "tBTC": {
        "trove_manager": "0xfb17d0402ae557e3efa549812b95e931b2b63bce",
        "price_feed": "0xeaf3b36748d89d64ef1b6b3e1d7637c3e4745094",
    },
    "wBTC": {
        "trove_manager": "0x7bd47eca45ee18609d3d64ba683ce488ca9320a3",
        "price_feed": "0x4b74d043336678d2f62dae6595bc42dccabc3bb1",
    },
}

filters = [
    {"address": [branch["trove_manager"]], "topics": [topic0]}
    for branch in branches.values()
]
