import unittest

from utils.auction_hause_utils import AuctionHouse


class AuctionHouseTests(unittest.TestCase):
    def test_get_item_count_from_item_bytes_success_1(self):
        item_bytes = "H4sIAAAAAAAAAEWQ3U4bMRCFZxNKk6USVdVLVA39UW+aomyzbNK7EEAgNSBBql5W43jIWlrvRra3bfomfYK8Rx6sYjYScOOxjs98xzoxQBciEwNA1IKW0dG/CJ5NqroMUQztQIs2dC+M5vOCFl5c/2N4ro1fFrTqws63ynFH1D3Y26zViWP+y3gJ7zbr7EfOJa6qGnP6xeXHgIpF0GRpwRpNCW/FFHLGgnzAzZpSL2dWObQC/dSsOngjiqWScF754JEco+a5Y/LCUCt4Ie+y2v8g87P840DmpLLKlIy/TcjRBLZe0lCS4HDrVuMQnFF1YDyvvanKJtZyWWOo4LXcabksVkgPLt+AJehusy4m19Pp9VUHdq7IMrwS8Ql2m5PTEMP+2Z/g6FH3McRPrDbsqm1LTeHQaRqH/fFsdnN58n129vP2YnxzKvi6Fv096zlzknCPaah7g/5Q9dQ8Hfa+ZKNRSoO7dHicdaAbjGUfyC7h5egoSY+SBPv9r4MMx1OAFuyebjuXQLgH3Q5Pt+4BAAA="
        item_count = AuctionHouse.get_item_count_from_item_bytes(item_bytes)

        self.assertEqual(1, item_count)

    def test_get_item_count_from_item_bytes_success_2(self):
        item_bytes = "H4sIAAAAAAAAAB2OzwqCQByExz+V7qEOQecuQa8h7oaBrpc6x692sQVdQ1eoJ+o9erBIm9sMw8fHgBieYQA8H75R2HmYpe1g3Z4hcFTFCLW93TElQJwZpQ81Vf1YvwwLZfpHTa/xlbedjiYOlp83fd71WaZlUZQyQiip0diMsxhRZJ1WW05W6dq0Fgwr8XQdJc515jo43Ud/k7WQaZbIk+AXnkgu8mMpAR9zTg1VehL6ASQrCYO/AAAA"
        item_count = AuctionHouse.get_item_count_from_item_bytes(item_bytes)

        self.assertEqual(40, item_count)

    def test_get_extra_info_from_item_bytes_success_1(self):
        item_bytes = "H4sIAAAAAAAAAHVUzW4bNxAe2XIsyQEcJLkU7YFpa9SqIUe7+ndOsiTLamQpkOwGQREsqOVoRXh3KVBcpz7m0lfopT0b6GP4UfwgRYcrBfWh3QOXnPnmm48zJAsAecjIAgBktmBLisxeBnY6KolNpgDbhgd5yGLsL8B+Gdi7imca+TWfhZjZhvy5FHgW8mBF3r8LsCvkahnyWwoaKo05sn4N7P6u0Ueu2dQn2wkthVN2mvRvHjqtarkIPxCiyyMepF7/yK059MfDI7dcTGFHdad+XC3CGwJOjcY4MIs11Kk3H0Nbh0eNmp0Immxiq5XqsVMvwncU3NHSsM6Cx/4mlVMuH6xhTq18UITSF9BjPU65drAmt5g13K03Cf4jwU9VnKxY2xjuX7PpElH8N/W+pfiFpD38+ZlmH6k4X9Hq/i5cj+MY2ZnSrB2GbEDOF0Ty8Ptv7DRUSrBJQm5rpm3U2zMZSnN7wi4XWn2yBaD4yaB/fsk6w0HnLXxDuta+W5VoJngQoGbcpEvYIy/GGElcvYKXJPGCx5x11MpY5RWSC8/J2lEqFOpTbI28Zlv8LQV+sIS2RNLnITuXZsUE0oy2ZHds9bUIFlGvKa8tIpNzm5dxssxwIWMB+4RIlRmuAzTHxE2m1pk9V4KlFYVXm1akeRY2z4LfIOPMT/vHjIIDgqTJkyUtrUwn7VQDfzWab9Jb8taXQl/z+zvNHpf94sPl+aDDulejfm88YtP340mX/QvPQXbEI4QamTbyhvJGCjogaU2pGw9//PV/IxRgv2e10PHQcpYYXG3Dvua0rVsvWQaaC7SFpbv0bKGMt1SGG+X59gKSuVCAbIDRKge5n9rTd72JV4bs2WDUI94dTSeC2HZPh+Nx13PT+0nASAk5l6jhyTyVuw3PRRIHqGJPGoy8EG8wJPBODvJKy0DGlzyA3avR29H4/ShnHwF4Ohz8POh63Xa/35sU4Kl9AXhsIowNZdwzGOK1pOxyo/1lEhoZcYOeitGbK+3xMNwIyiYJMX4v5gJ9t9IoVXjTLVWrNSy1am691Krg3J1Vqm7Lp/ciTzS4MjxawrPGa6fy2nWY45w4DfbuAmALnqyvpX2M/gEgqaP3uwQAAA=="
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual("Telekinesis 1, Ultimate_one_for_all 1", extra_info)

    def test_get_extra_info_from_item_bytes_success_2(self):
        item_bytes = "H4sIAAAAAAAAAHVVzW7bRhAeWbYi0Q4cFDn01G7bGI3qWBEpibJ8KODKii3EP4ElKzCKgFiRK2khkissl3Z87Av0CdKzgD6GHiUPUnSWpH56qCGTmtlvfnbmm5EBUIIcNwAgtwVb3Mvt5mCnLeJQ5QzIKzouwTYL3Qnovxzs3oVDyeiUDn2Wy0PpgnvsnU/HEZ7+Y8Azj0cznz6h0aWQrIjab+H7xbx5zqgkPRd1J2Qx95q1Jr6OX5sts1mGnxFwRgM6Tg7dQ/O4gW/2+tCqlhPYYaNerdhlsBDYU5KFYzVJoVajuQltIXRp07RrFasMr9CmLbkimxGa1YMUZFlWxT5IPf8mwjgip0pRd0p6M8a8DHyQem4eZJ7NaqWBNhW06YaK+T4fY4kS1xSTr6Zw02oss2/YlUYZvtPS7/j/9cuf+Py0Ev/6Q4tYq1+xNIu5nz7vfMUDqhj5yCNGBujzjXbc9hl92JTxbtylPhl0oanleMijYH3eCT2Gpcem4Gut/TxjkuusSbfb1YFb77hk5DSaMVehbglEbaQIFp1PEbqyP+c0VOQ9933tFeqo6gYz6vNwrB0uYZdMTVCpntaRL4VQCWoANS3GWOzByuCKhhSjMbzPhpsPUkTMjbEWA7BR7rlYgnCMoTdAvYBrwEruT2J9dV9IT9dGqwY0mHH5n/IMWCgCgX0fYP1/Wczt0yHXCZ+QPpOS8pD0RRRpjmFLbrvnF33Svuy238NP2P3+RIrHiFDiYqwpESOiMiP8qAmDHxHkYV1dxUVInkRMKBZ5RF2swA/kDK8ZJeMRz4gSmmyW/aZmtio20YYJYSvwEtmR1KUtIqVJVkNqwTeobQvhe+IxTJhn6hlsLRk0pYu5JJt8urrvX3Tb5Ozu+rxzc016H29uz8gaXoTtaxow3RTvgknBXXLPFCe9R11ALMzXL3//3xMM2O98VpLi8Eg+xEZFediXFKn55MSzsaQe09nhxngxEcqZCUWVcFy9ZlBt5GDPi7GfInSwh0GuCMVAeHzEmYTCJEkmD88zR47PHpiPZjtFvbDAuO/0u05yHQP29K5CagYsVJhDkWekRHg+D9s+sg2/FvDEzeYmFQtuMlbaax52Ik2l9OCZn/IVpW3cd9GSealDDIcUc6JkulLj3RH226HJHKFmKw8GWw1balV6WPIwNdkb62lypsk0pSojwIY7kR6ELNJIDyJq9CCmyRQfMu5mgdWa8Gnuz+NshTiPuEJSVMFN9kMqlPzlfGbyh9ubXqd91+9oGZAScYwVflUf1lq4Dt0jdtyyj+reyDtqVavVI2YObdaw3GPmjYpQwmAsUng32G+8Nc23lkXsk3qLnF5hHaCQLmD9O/IvLBWaT3YGAAA="
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual(
            "Impaling 3, Luck 6, Critical 6, Cleave 5, Smite 6, Looting 4, Scavenger 3, Ender_slayer 5, Fire_aspect 2, Experience 3, Vampirism 5, Giant_killer 5, Mana_steal 3, First_strike 4, Venomous 5, Thunderlord 6, Ultimate_wise 5, Cubism 5, Lethality 5, Prosecute 5",
            extra_info)

    def test_get_extra_info_from_item_bytes_success_3(self):
        item_bytes = "H4sIAAAAAAAAAI1U3W7iRhSeJLtdoKravai6lXoxayW92ZD4H4PUCwJs4hSbbCAkS1VFY3sAw9hGnjGJU/UR+hy8QJ+A1+i7VD1DVtte1vLFnDnf+b7z4+MaQlW0F9cQQnv7aD+O9v7YQy87WZGKvRo6EGR2gKoXcUTfMzLjgPq7hmrDZcHY4CGleQXtuxE6NBt2GJmaUTc1R68bhhbVHdOa1k1Ls1XHsCzH0CDuKs9WNBcx5VVUEfRRFDnlO+kKejkmrKDoT1peqpO7uRrdXbKwdG2wR0OVDdzFquGm4zLouLabgP+ibffL5n+wliC3FvtoXM4n6YciSMZq37hm9OJaC5ObtZ+M5x8XoTa5fT/3bz1rsrhc+F1/7p1/KD3dTybnPvOexol/fp34C6+cjJamN7p58Lo90x+1n/yn8GnQBb/ulpNF+2lwC/jhZXN6p/4EFdTQqyjmK0bKKnrRz3Jagcs36KvtxulkSUAEvqICrr7fbhqdPBa4SxIyoy283YTvDO3EOgLnl9uN3UsjmsckRQog4R2RJQUQ0fQT+wgODUY5x9EuGn0L9jTPEkzTCCdZygXN+QkwvQamEWV0leUCD8l6XaIfnvnOiumUYzGneJSTlCcx53GWoiNwkSBmsZwOnoFLxOlMCuuaVH2gZAWwN3B81sbTLMcWx1mKC06lJlDYF5RF2BU0kYVN24zh4TJmjOPe4wqfZRkX6MfnPM7jNQi9k5Wpu7pWVGAKKMlLGEM1uOO7YEn+Fiz4fGa5rF5kuE/XlGHTkDrUbJ6YR+h0u9Hrnx+Q/9eQoOaxbeonGiQJQKo1l8B6uMuFXsezuaiHLA6XkptEETQo5limJDLZTFpmRb6zE5oWb+XAtxtru2G9K7dTQS98klD0HbD90l9DWvqvoGjtRpnAKGvo696jyElbiDwOCkF5Bb0CMjedZuiv3xRRrqjSUnp+t3fttX3lWCGhgP4orSlhnB4r0BelpTUdWYHqWIZmapbTtI8VmFYuIyELiJrDnkrOz3FzGIecBkCueqN7d9Tz7tv9/v3wZ7ffH96fDQbD0X1n4HkDKRqSNCpvOI2UlnqsFEUMB6WhqXakBWGdNgxYaE1z6o6lB/UgaIaw1446DYJP0rs2dmQXPyXwe0X+UdABaEOPJCE6/D98FVQVcUK5IMkKfdM81a1TXcea3lINfOUhtI++eF4fdIDQPzdx1YbCBAAA"
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual("PET_ITEM_ALL_SKILLS_BOOST_COMMON", extra_info)

    def test_get_extra_info_from_item_bytes_success_4(self):
        item_bytes = "H4sIAAAAAAAAAI1V3W7iRhidJLtdglptW1W962qW7l5tyBoDBiLtBeHXBJsNv8FVFY3twZ4wtpE9BkzVR+hz5D3yGr3tc1T9TNhsu1e1LIG/Od855/sxZBE6RUcsixA6OkbHzD764wg9bwSxL46y6EQQ5wSddplN25w4EaD+zqLsaBlzPtj4NMygY9VGbypSqVhTFmaeVhZSvkiKxbxplit5u2baxZKtWBWrBnkfw2BFQ8FodIoygm5FHNJoL51Bz6eEx/ToL7oJHLXRk8iswK3i0DVv6kxtBo42nidaUyvqY2uj3zmSlmyu1EadWd3e2vB4ZEz4UmV1RW2oG312LeljnRmzlqTLc0kbu2wwU2WjOdkNmpA7u95qzbmsNdSoweqO6l8mpmyszM50MAfdR55eey67a8vvuSo7aMncN722ZN/0+MSbbu0ZT4zZ9d6f3e0VjNEjzu5MS3Z3mhg32v7ssSbQ4Xp/NCn9N5bib3rRQTOwu8PNgFXX/+KIzRmPjZmezGeG1PfK3G7UJOPG3fvoy5qk33E2H0PdTWur3fW41mklRmeym+8sSdvZrtHUl0ZzutR2bU+bte807zrR5TYDTNm4c0p6s82hJ2XNa5XmuynTdxPWr3/2Z86m0nw2dO1O60vv6ayEKQ+52VCdAUt7tF2ZI/Xq0/niOvj82ZWuFtcfPsDEs+iFzaIVJ8kpetYPQpqB4Cv0zcN9tRF4JhH4IxUQ+vHhvjISIfUd4V7gh3vrXUE6l8voB4i3aRhYTCRpnLwrnRcA//3DvQJrJqgl2Jri0ZL56CfAwt2BQJRSuBTomefFPiSfQ9LXkNRmIcUzl63Qm0d4a03DJGUup0mVjcs4xczH1t4eegWxwMer2OTMwizixLejM3xJON4wztFrOI9EyJYU+5SEZoKpTz1YfTgWLnZZhHIAWaSywL3CNiWc+U5qEEp5m2oGiz1NEsQhtolHHIpJamYhwpgeIqn/l+BfIzbFwQL3yZrsmdOKCfiFCpRPfD6u9/s4EkRE6Od9UdSHmiJ4v7FwaaqtEccjuM0ot6OUGwwoXXjAqqBe2umaxvzUZ2u7wpdBEIkntX1/34FeSdrLrajAFFCLIERZeH5MPJBWYEoOvP4RFgHu0zXluCSn/LRQPlfeovcP93IeLqg2/8WVgopnNVk5r4E5AFK5vATWx8HRIXNckbdgLMuUm9g21MYinNoRAfoOIPuOps8e9ePXhw4+3PN+q9PSm/XhPIOe6cSj6TpVfumvwVvhV5BVYLywui9bWxGSuoDxmrGgUQa9ADLVXwToz99yIlnR3EXust7PneXIfg9zFwvCI3qWg3bkLuRyqVpWzqtKUSmUFEmpFc9y8KMYQtKTAUh1YSop51OyC2NIpwC4j63xrTpuabeaqqt653Z0pfb7t5eDwWh8O6wPW5BuwUImk4jauQvpLBfHDL7kZNlULLks5UmlIOdLRbmar5rlWl4xq7ZFqmVale2D9L6NjbSLBwO/Z9L/B3QC2tCelBC9+T98GXQqmEdh67wV+rb2XpbhxgXpoljDdQ2hY/RVc7/K6AShfwDrWi4skAYAAA=="
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual("PET_ITEM_MINING_SKILL_BOOST_RARE", extra_info)

    def test_get_extra_info_from_item_bytes_success_5(self):
        item_bytes = "H4sIAAAAAAAAAG1UXW+jRhQdJ7tdx+qHKnW3L63EWkn7EicD+COO1AcHxw5egxPHjmOqPgwwwDgDeGGwQ6r+hP6Dvud/5IdVvZB020pFRgP3nHvuuZfx1BDaQxVWQwhVdtAOcyu/V9BrLc4iUamhXUH8XbR3wVw64MRPgfVnDdWu7zLOJ9uIJlW0o7toX211XKeD3YbnKt2G2pZbjZMTz27YzXaLuFRVPbkLeZdJvKaJYDTdQ1VB70WW0LQsXUWvbwjPaOUPuo19XRthspC5o04D+7bH9H7sG7N5a9K/wubKwcbqHBvX2w+61mPOxWhjhTy15vxOZ722runYWFw9LBejlRFeqWb/Dhv9s9Vk1msZwyvZ7BvY6vceJn3jfsn0VGM9X4/Oclux1vbwZrKEus86I9NauAFR7je20mTjXunrgSzcbHk7lZ3w5tq6HcjkdsQtTfcn7Aw70Q1/4WHrNsAuYE5eYp2yDvidYzGasf/ECj7obcs+9RDyLnrtcd79l0ZLkEWLL9VRYEVXmR3e4LE65fSi8DHfmEMjN5X5w1LRZSM8V6BnZTKcK8bQaJqrAbdWg2C58rE1OwuMocnMxXJrKiNuzHowJ0OdDKcBzFU1V+eq8TAIy3lp+ofS2wWG9ayrRfgn+FI19MZl6ZqTfA+9GscJrULwHfri6fFEi0ObCOmSCgh98/TYuRYJjXwRnEpPjw4+UlroW4jqkaCcM59GDi0Qgo/kEtASJiQtIC9xyJAP/gH6JCT+30DrAL0FwCA+c6QBi9xPQuDw6bE9cfM0pTn6AUjlTzFyEcQ8Bj7hkpNQUu49yOrkcYbew+qBjETgtrMkibepBIDkMl9KIYWiA6CwqCjvMs9jTsZFXqQXGVAxoVuSuCn6Dp4hapOUulIcFSKJRD9mbL2mbjmVYVLkRz+mUkKgsfwIPH8Pcfhz+GAplUQsjemGckkpuqL4oGjDa/zPVcJQ8BhWGWMQ2i+7pVPmB6LhcObcFXLEdSURsFRaUwHv6GuglMaK95BG2XtI/RyKPD1ybWIYE7OKXpkkpOWUfx5vuCT/AsW8F++wC746vxcJ6QmRMDsTNK2iNyCmR16MPv5aF/ma1k/rw6k+GOhm/bBOHME2EPIIT+lhnd6v66f4CB/W4TBIgPlcFYgBHDWFyieqAwPO5zBNSHiGy+a0orcX0m/V4uBCu5fnM/CdZfC87ylNTNtNu+HZMmk0PYIbttJRG12l23bb3ZaHXaWK9gQLaSpIuEZfdo+7x4oitU5xV7o0ENpBnz3vObSL0F/tQiBOJwUAAA=="
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual("", extra_info)

    def test_get_extra_info_from_item_bytes_success_6(self):
        item_bytes = "H4sIAAAAAAAAAEVRTW/TQBAdpwWSgNQClXpdBOJShcZ2ksa5WalLIvqBEiMOCEVj78RZ1V5H3o3U/Al+Qc/kf+Sn9IcgxuLAZXf2vX1Pb2baAC1wVBsAnAY0lHROHHg2LjfaOm04sJg58PKbTirCe0xycg6gNVGSrnLMDIv+tOGFVGad47YFh9dlRU1GX8Gb/e7iEgvMaCT2u/TM7XbhhLG5rUhndvUfPeJq+IOpp8dfXP1kubffDcJE5cpuR2KqjUVtRVyhNoUyRpWaJbTf5bPp50ksxtfT8Rd4zw4x5bQuK8s0DkWSl+m9YVjgilCKcgkf+bUtNwK1FBmq2gfP+l2+lk+Pv8V8TST5C5zysSyrmvaFobTUsjb6BG854Q1qFOPS2LoHv9/lwFxcMBOvlBHKUiFS1CIhURG7ZCTfwfF+F9SJw1kk5t/vZpdNOLzFguqhBKFZU2o5oLArEpGW0Iaj6MFWGFpbqWRjyTTr5cDrcP41GseLu6tFPIkW0W3ts9kw8yFJh7Inu8uOn3p+pzdYup0kGA46rotSpt6wF7hJE1pWFcQDLdZwHJx7/XPPE6478gMR3gA04Pm/pXFP8BdCSNuRGwIAAA=="
        extra_info = AuctionHouse.get_extra_info_from_item_bytes(item_bytes)

        self.assertEqual("", extra_info)

    def test_check_if_item_has_enchantments_true(self):
        item_bytes = "H4sIAAAAAAAAAE1SXW/TQBDcNGmbREUFJCQkEFoJIhq1+bbjpG8hdVuk0kYxbR+ji312TrXP0flS6DM/Jv8jPwyxtlPAL3eemdu9mb0qQAUKogoAhR3YEV7hXQF2x/FK6kIVipoFFShx6S4g/YpQuRQePw9ZkNDv7yrseyJZhuyJVFex4mVCX8GHzdq64Eyh4xJ2ipu11zX7tAyOulanDu+JP2MRCzLOPR6YGXc87DQHdfhMrKMVl4Fe5LyR8sOj465Zz4XGoNmvQ4OEYyU0/l/Late24nZtq7bMZr9WhxbJv8RyleBIa+Y+oLPk3Nt22B4yns/Qhqz0CByHnD1yvKPtSSpKOwqXhf8QW3qcvFIKtNxBjaBzoRKN5EI8cPz6V+ksmFpKniQkA3i9WfdHcxEK/XSKeRv4SJe8X3CJC6G1kAEyiVxqkpxgFMtEc5VkIiGRUUlGV7RwHsbkRzEZcPwhwhDneSUqgn6sSLmMlRaxxNhHvWAavSwy2CeRjuMm3eYtFZtw5XNXY6/XNw1sYc9st9spM9ysw+loauPZ7fWFfXONzv3N9KwMpWsWcXiThrAULjqrJUWQW1FQhUP7p1aM4lZivtI8KUM5ij3hC2JLnE6UoRIrEQj5nQXwwrm8mcwmt9Px5cixi3AoNI9m3kqxPCSAX4/l9I2S8nZiT2fjK3t0Z0+rcJC+UCZ1RFElRSi72xmRrd0iHPjpNGZJNg2CSkXYc/O4M76SPI9lq+fpQGdJNtAUAjK6WlHfT8bQc12Ldxqu5RkNw5t3GszrdxvmcGga5mAwn/s+edIi4olm0RJeWq2u0ep2sNM5bRs4+gawA3v5g4UCwB9Bd2SDgAMAAA=="
        extra_info = AuctionHouse.Enchants.check_if_item_has_enchantments(item_bytes)

        self.assertTrue(extra_info)

    def test_check_if_item_has_enchantments_false(self):
        item_bytes = "H4sIAAAAAAAAAEVR227TQBAdpwUSg9QClXhdBOKlCo2dq/NmpS6J6AUlRjwgFI3tsbOqvY68G4n8BF/QZ/wf+ZR+CGIsHnjZPXvOztGZGRugA5a0AcBqQUsm1pkFT2blThnLhiODmQXPv6qoIrzHKCfrCDpzmdBVjpnmoj82PEuk3ua478DxdVlRm9kX8OpQjy+xwIym4lDH506vB2fMrUxFKjOb/+wJo8l3lh4ffjH6weXuoR75kcyl2U/FQmmDyoiwQqULqbUsFZfQoc6Xi0/zUMyuF7PP8I4dQsppW1aGZZyIKC/je820wA1hIsoUPvBrX+4EqkRkKBsfPB/2+EofH36L1ZYo4S/who+0rBq5LzTFpUoao4/wmhPeoEIxK7VpeugPexyYwZiVcCO1kIYKEaMSEYmK2CWj5C2cHmqvSewvA7H6dre8bMPxLRbUDMXz9ZZiwwGF2ZAIVAI2nAQ/TYW+MZWMdoZ0u1kOvPRXX4JZuL67WofzYB3cNj67HSvvBxPCfjqKu9HIoe5g4DBCL+56qRs542E/dXtuGzpGFsQDLbZw6l24wwvXFY4z7XvCvwFowdN/S+Oe4C/HvSXsGwIAAA=="
        extra_info = AuctionHouse.Enchants.check_if_item_has_enchantments(item_bytes)

        self.assertFalse(extra_info)

    def test_get_item_enchantments_from_item_bytes_success_1(self):
        item_bytes = "H4sIAAAAAAAAAHVW224aRxgeAnGAOHXVtKpUtelEratYjh3YgLHdqhUBbGh8EhCnB1WrYfeHHbG7g3ZnbXzZd+hV1dxVtdSH6IUfxQ9S9f93AHNTy4KZ/3z8hiJjBZaRRcZY5h67J93Mxxl2v6GSUGeKLKvFqMByEDoeo78Me/gmHEQgxmLgQybLCm3pwoEvRjFy/y2yB66MJ764QqUjFUEeqU/Z5zfXtUMQEe85SNvnN9durVrBr91n1svd0gZbR4GmCMQoZTqbVpm48Gxzp7SRim3W9lDsOxTr6QjCkfZmgrXqdnVZdA9Fq3Rwn22WKzPl8vNSxdre3WBbaKARSc2XnZWt0rrRrJbWZxqVWmV9gz0h8s9o6/bdr3j6ZXH9/Te6Ym7f4u3m2jefb3wtA6GBv5Ux8HMUeU4aDR/ExfIdA5CO8Pl5h31N92Qg4+CO34zESIW8jR2AiHc6nTmjFbpI6GF18QuVa0SbgpPoJeut6QQiiQ0D3lkQD2QEvB5PwNFokO0j6VCKUPPX0vdTY3PJTjARvgxHy36PQHtI1Ffk1CKCUjqVWTg4SpzxkpVjEQre04BJoh22g6Seg0UIR5TRQqsXSAr9zlPfSyhHX0Uu+dojUiQnPmxh2+V4OaVzEUxklBZuoX4OoQpUEvNzbM2n2Os2RYA9rpZu3/2JhxrWhntSb7MNmjjDFZtWNZ2AmptOBdeK/6SCgYQYadvsC/zE/y44ILGPqGBVU3Ef4pgbHfYZ3oeRCpY0+aUHIffAd7cxHBy9Ac7I7V//oOpOfSCpoPu870XqkgYYed3OYbvPG0edxmv2BA0Y3pVKIi6mYDxR2YXvp3wIIUBXXIZc6phPhPa4C2n72Cdp0E65RKvFA/BhZgC22VPaAhXGNDmUkSY/MY+1wCaikjVlX+HXXUEGieaOijXV2JpS6gE1OJmwAp6xXOWdKXuMi5P2vYGStFkvrRLmvUbjR2Dh8lcqTGLjfb4CHgXu0XoI7niCplarFA4oEfRAzcCKl03FYaojsciD0YCY9RuLm+uILy/j8Y/9dqfBm29ODlunJ7z39rTb5HfieZY7EQGwb5A0C6+ONVZDrAbwnheB6yINW3X7x9//98mKbK1FIdU1jidWCeIsW4sEZndlJ5NRJFwgXEScfN9T2p4oLbSyHQJXKk2R5UYQxHmW/77eO2t17RLLHXROWkhonB6/qvfnhAJ7Lwl95YzBtWNf6Zhw9d6S2kI+z1bnRxttsxUjwtBkoFw5lBCxlWGacJZ94Ca4kSq0cQ0D24cL8NHu/Tz7cKIuIbKFmVI7diKFM/dRr3521u50W/bZ6Vt022t0T4+O8qygIomD2Rcjttpt1SmitNx5ek7Y4/oPLfv0wO63W3av3W01m61mka3Sk4IIFECosWh5OcMd9J/NspyPeILHFeQ4s1kx1xUnRVMKM8se+AaI8JbLsvsxwQmeH+CzFM/hxvDQHeIK1o6w01h6qHEpxjKEWM56VLiYY4qRKMICS42Vh0PEUVukOEoNwAjA4K+JZ3VEoGqPU1Cd2aBNsWOCQpNa/mIGUkblkZuive2laG9EHukU81CLMG/mWt9Bo7H8KJk9N/YlPjfG2oqTviXmUvDnuE0KOAG5JMF+fDkc1vZ2Xu5ZW6XKALYqUBpuDQZWeQvKA7CGbm0X9naxqWgcEBKCCVsrl17svrDKvLpvVXn9mEZvxbyg9JvgP+j4WytCCAAA"
        extra_info = AuctionHouse.Enchants.get_item_enchantments_from_item_bytes(item_bytes)

        self.assertEqual(
            "Impaling 3, Luck 6, Critical 6, Cleave 5, Looting 4, Smite 7, Scavenger 4, Ender_slayer 6, Telekinesis 1, Vampirism 6, Experience 4, Fire_aspect 2, Execute 5, Giant_killer 6, Mana_steal 3, Venomous 5, Dragon_hunter 3, Triple_strike 4, Thunderlord 6, Ultimate_wise 5, Cubism 5, Lethality 6",
            extra_info)

    def test_get_item_enchantments_from_item_bytes_success_2(self):
        item_bytes = "H4sIAAAAAAAAAF1T227aQBAdIGnBTZtenvpSTdpEbUVIbBIDzhsqVEFNGgly6Rta7AGv4gvyLkl47If0mf/gU/ohVWdN00jxi3dmdo7PnDm2ACpQkBYAFIpQlEGhWID1L+ks0QULSlpMKrBGiR+CeQrw7CIZZSSuxSiiQgkqxzKgr5GYKK7+seBpINU0EnNuOkkzKnP2LbxeLpodEYsJHeFy4Vcdx4U3nBvojJKJDldZz+PLr5YL70SOCQeaRIS9Xg8+8M1jDhSO04xvCmfP3eF3Mx3jPJ1lGIs7eM9xyJd0iCT8ELWMyVQxlBoFxuloD14w9iAU2TQhpfAy7+klPk+jSGFMEREGOU0MDBSO5vCc7/AnD+wdPqwgLkU8lZlUMUPsPObmmgz+ZyaVkskE3j2wuw0poRvKcnLXMopQJFDhOqfj+R5L0OagK7KE4RrVuo1+KhNl5h1nacyTJEpzu2lV+OmEsSIukmNXc02SaP6ZQT7kOuNKdVOYkuHnu7Ztorwbtvn0zZzyBTjNXdc+MEMsF9Fp+0e3g2cX51sM9jEH+/3rJ95v7AGR/iHepmlgFG0NZrFCEzHxKCJfS2a8a5aEVce2cy2uHpXN96l+uOsdGg9grnnrPJQKpaYYfZHgiDAjFnlCwRa85DUwyX6738XB1Vm/U4a17yImsy6vL9iSGbbvCCzY7N7pTLS1zuRopkmVYCPL68OVBNAZlo3rweq3e51uf8hzW7BhDC8SHVOiuaWi7l3D7NY5vrm3wCq2InbsUBnHcqIEzGY2Y8xtMfZsp+U2avXGyKkdthp2rWWLg1pzPBZuoyk84QVlqBizKs2YsOnt1939eh2do3oD26cARXiyWqL5/f4CSxCF/q0DAAA="
        extra_info = AuctionHouse.Enchants.get_item_enchantments_from_item_bytes(item_bytes)

        self.assertEqual("Sharpness 5, Vampirism 5, Life_steal 3", extra_info)

    def test_get_pet_rarity_from_item_bytes_success_1(self):
        item_bytes = "H4sIAAAAAAAAAG1UXW+jRhQdJ7tdx2q1qtTuvrQSayXtS5wM4I84Uh8cHDt4DU4cO46p+jDAAOMM4IXBDqn6E/oP+p7/kR9W9ULSbSsVGQ3ce865517GU0NoD1VYDSFU2UE7zK38XkGvtTiLRKWGdgXxd9HeBXPpgBM/BdSfNVS7vss4n2wjmlTRju6ifbXVcZ0Odhueq3QbaltuNU5OPLthN9st4lJV9eQu8C6TeE0TwWi6h6qC3ossoWlZuope3xCe0cofdBv7ujbCZCFzR50G9m2P6f3YN2bz1qR/hc2Vg43VOTautx91rceci9HGCnlqzfmdznptXdOxsbh6WC5GKyO8Us3+HTb6Z6vJrNcyhley2Tew1e89TPrG/ZLpqcZ6vh6d5bZire3hzWQJdZ91Rqa1cAOi3G9spcnGvdLXA1m42fJ2KjvhzbV1O5DJ7Yhbmu5P2Bl2ohv+gsPWbYBdyDl5meuUdcDvHIvRjP0nVuBBb1v2qYfAu+i1x3n3XxotQRYtvlRHgRVdZXZ4g8fqlNOLwsd8Yw6N3FTmD0tFl43wXIGelclwrhhDo2muBtxaDYLlysfW7CwwhiYzF8utqYy4MevBnAx1MpwGMFfVXJ2rxsMgLOel6R9LbxcY1rOuFuGf4EvV0BuXpWtO8j30ahwntArBd+irp8cTLQ5tIqRLKiD0zdNj51okNPJFcCo9PTr4SGmh9xDVI0E5Zz6NHFpkCD6Sy4SWMCFpAXmJA0M++CfRJyHx/060DtC3kDCIzxxpwCL3sxA4fHpsT9w8TWmOfgBQ+VOMXAQxjwFPuOQklJR7D1idPM7QB1g9kJEI3HaWJPE2lSAhucyXUqBQdAAQFhXlXeZ5zMm4yAt6wYCKCd2SxE3Rd/AMUZuk1JXiqBBJJPopY+s1dcupDJOCH/2YSgmBxvIj8Pw9xOHP4YOlVBKxNKYbyiWl6Irig6INr/E/V5mGgsewyhiD0H7ZLZ0yPxANhzPnrpAjriuJgKXSmgp4R18DpDRWvIc0yj4A9Uso8vTItYlhTMwqemWSkJZT/nm84ZL8CxTzXrzDLnh7fi8S0hMiYXYmaFpFb0BMj7wYffq1LvI1rZ/Wh1N9MNDN+mGdOIJtIOQRntLDOr1f10/xET6sw2GQAPK5KgADOGoKlc9QBwacz2GaQHhOl81pRW8voN+qxcGFdi/PZ+A7y+B5v9uWcbsLJ5LrYqfR7DSdht1V5AacUwpWFPXE63pVtCdYSFNBwjV62z2WlWNFkdqnSlO6NBDaQV88bzq0i9BfXrr5KSgFAAA="
        extra_info = AuctionHouse.Pets.get_pet_rarity_from_item_bytes(item_bytes)

        self.assertEqual("Common", extra_info)

    def test_get_pet_rarity_from_item_bytes_success_2(self):
        item_bytes = "H4sIAAAAAAAAAI1UzW7iVhQ+JDMdQGqn3bTqzuMmq8HEP9jG7CJggiMCJECIqarRxb7GDv5B9jUTqLrpvvu+Adv2FXiAeYg+SNVzM2k16ixay5J9z/2+73zn3GNXASpQCqsAUDqCo9Ar/VKC5+20SFipCseMLI+h0gs9+iYiyxxRf1ahOl4VUTR8l9CsDEe2ByeNpq9rvk8lovmypKlNWSLElSVFcV3ZMxRV8RvIG2XpmmYspHkFyow+sCKj+WPqMjy/JVFB4Te6vZTnd4Hs3V1G7tY2cD0Zy9HQvl+bdnK7XbRtw45xv3du9LfWR1idkZkeOdplME+ui0V8K/e1m4j2bhQ3nm4c9TaeT7zVsHO+cybXijPrbp2Z8zCcrHbzC2c7mFzLzsRu4Htj0ImCwQ5j985usOvqTjyP5vGVMry4jK92S92Z2dr8fhr6d4qF7qvwwgvzdUS2FXjWTzNaxuC38MVh33wT5kGYLIURZRj75rDHGhiNonBJE5e2hMOevLYagE9zTInQzijhTRHaAXnad19bdfMUyShnjFJPmBCXhW4Op8jB+yIjCcsRuEBg449ffxb+zjleU+qBiDsI89NMoMQNBG6TZsK7kCGI59dkOMEHYhZR6q7ymlCsBZbyLZ37+kDI62jhJVroukGKOMLCNIHv/uVB4x7e/y58XAt8jvEP9SCUyyDL6NHIE2xGY16jMSN5QD0JE4/TYkOTMINXn0jr/ynM7eKMLXGqcl5Cn25oJFg6z0HNunoKymGvStJh70ufXBxjmDVDM+sWWjrDpaUZK5Q9ebRCb8JlwCQ3Ct0VFyeeJ2APc2FNGa7hK4Rs0yJ7XMc0KV7x0Tjs9cM+6o7sdhmeDUhM4WtU+76/QV+NHzCn3kmjNR4FTtHL7gPLyDljWbgoGM3L8AK17MRP4f2PItuuqdgSO8P+qGcPxJrI52CDIZ9EOa2J9GEttpS6Yuq6pZmWqpua3FSUrlkT8YvLkMpdIC/Ar5mL/sMM8Cz4USBkdj7udTtvp6O34+H0tjuwb5DgksTbTnPqiS25JhZFiC+i1lR1V9Ob0sLSNanh66pkUWJISlPWfdMkC9nwn5I9Nq7N+/aU8qcy/9PA8ag7wa5wQTj5P3plqLAwpjkj8Rq+tM5U/UxVBUVtKYowugI4gs86JCZLCscAfwH+nwNm2gQAAA=="
        extra_info = AuctionHouse.Pets.get_pet_rarity_from_item_bytes(item_bytes)

        self.assertEqual("Epic", extra_info)

    def test_get_pet_held_item_from_item_bytes_succes_1(self):
        item_bytes = "H4sIAAAAAAAAAI1U3W7jRBSetrtsGn4WxAUgJDSbbRFok9Z27DipxEVJQuOSvyZptylCq4l9ErsZeyJ73DaLuOABuOMCISFxlxfgCfIOvEAfBHHGLdVK3GCN5JlzznfOd35m8oRsk40gTwjZ2CSbgbfx8wZ5XBdpJDfyZEuy2RbZbgUefMPZLEGrv/MkP5ynnPeuI4hzZNPxyA4zNdO2DVaa1oxyqWx609LEhnLJrE1tsKwK6HYNcf1YLCCWASTbJCfhRqYxJFnoHHl8xngK5E9YHmsX577mnR9zd+lU8DwaarznXC5sJzpbTupOxQlR3zqstJe1N2wtyV5afFw+9i+ik3QSnmnt8oBDa6C74enVRdj1u40Tvfv6xOpcnt6Mw8G815ibF6Fjdoyx0b10zW5jwDuvfb/zchBeXLrWeNTUO5c87L7miHW0bsPzO41Tqzfq3HSOzvxu/bg2Pde+wgzy5IkXJAvOltvkUVvEkEPhc/LuelWti3DCJO2DRNEn65VdjwNJ6z6LXDig65X7Qtf2rF3y0b+qBgvZ7F5l6LvkM1R8LaI0oYdSMndOhwsA705fRiAh761XFbQAehjH4jrJELicyI2BJUCZElMv80snS/I80zPd3MUNvfYD16dBQmUcLDh4SsCBPEVdEFEvjWYgomQP4+QwjkpHkMJdhCOGFoy6SkaTjNxUxBSuIF4SJGhPMK6POc1iFskgmtEXGLesqN/+/hPZwf9QxhDNpI/Ge7TDbmhGTGEzf0mRfPqwp1hjtlgAiymbSohplbytlOCKyMsYfogMh3PgIBmnDZhClMB9uvZYpDFNMqWIaOILIRPKorvqEFUKDxhXJBVHTTGxlwqzXtVuf/2DquaoxGt3DVLqax9U/qGY0BmgN5cLjPcxaqSgiKVfWCgUgnviOvpSEfwcCbaAe9SREKoeWvVYuD5IOgpmmFGfp4kfPHA+UnVL0Ayw1be//ULfHATyDsqzYVDFQ+fP8I+XbIbXCrspaBsbwamtqzhQy6bMWK+M0n+/9WpaUkZ61S7qVnUPzSr7eDa0yhwd72RsYBDMfFlyeYB9RvfM86j0cXAWSF8K8gGaZAVT5xCi9BlCcYwq6xVvN4+a3cbhYJwjj7oshGzcv2tfIT3te/rQNRHhVXravJExwxzjYJJKSHLkCXp0oqkgf/1QkMsFFA4Kw2+b7eao1y0UC8yVwRXKpownUCzAzaJwYNTKZrla3dMrNq6ybleKBXx5YkQ+UEGoj0+bcvwA9rE3qjVoVx/06q3m6NXIOWoOXvXbp8OW00SMyyJveZqAVzjQioU0DXBTYBVjAqbmlqa6DiWzYpglprNJqepaNdtyq3p5ot3Hy6pYV0W8j/pjTr28ZKvfHGF1lEN8Uv+HvxzZlkEIeDfCBXm/tm9Y+4ZBdeNAL9N+h5BN8tbdqJItQv4BiBtGDeoFAAA="
        extra_info = AuctionHouse.Pets.get_pet_held_item_from_item_bytes(item_bytes)

        self.assertEqual("CROCHET_TIGER_PLUSHIE", extra_info)

    def test_get_pet_held_item_from_item_bytes_success_2(self):
        item_bytes = "H4sIAAAAAAAAAI1VTW/jVBR9bWeYNBKMEEKwQODJdNi0mfFH4ky6c2M3dYidNt82QqMX+zl+rT8i+zlNgtiwYsOeBWzpmr/QH8CGfzDidyCuk0w0M2KBFCvWveeee945jlNE6BDt0SJCaG8f7VN37+c99LARZxHbK6IDhqcH6PCCuuQ8wNMUUP8UUbF3kwVB5zYiSQHt6y46cvmqWxdrpOzJL+WyJEqkXHdEoYzrdZcnvOOIDoa5yySekYRRkh6iAiMLliUkXa8uoIdDHGRk729yG0/1RovHIyFwpK4/GStUV+Op0beWhqotzL5eNVVNMOntN3pDoc5Fa26HQWoPghudKrLe0HlzZElWvxWY15rUUTXeum5dd1TltqMaVSPshqaorwDD21RPG1SZ6tHZciLas0lz2LFg74an5fWi4crVuvPe+Iq2lbWuFR65mTXuCk447NnjcwGPW4Hd0KcdesY70TDY4nh77PMu9Jzluldb7wG9A561+vSdWo4Hvtv1OfUQ5i4Uub2sv8VRZXhUDSyp5dvRVTYJh3xb6gbkItcxmFt9RTKbmmSFV1VzZYd23/atELy61nnwbWGublZWOBBM1b0x+13wwhAs0eKNa31pqqbfUQcLwN92RlcLu28JhjoQjOXWm40+Zo+7vt08563e+9rhCoW53RymW99Wk2bA9Gm87Z/VN9jNt3c1q0PiRfTIpekswMtD9KAdJ6QAxS/RR/d3L89p6tNoyl0SBrWv7u9qPYK5RkJw/rxwDR9HDjnl7u+cY6H2DCCf3N/JFwQnjIs9jvmEAzx6AnPwaSY4YimApWPhzz+4t5lyiLRhg36NxdwyzhJuRhjnxQlHsOOjZ2uW6jvsRv7jwDTKhwIyJ8Fz0PApaNAW+dPNNfCccPkhSPJGRR/GvO2x0hkhLpcQN3MYjSP0BfS9JA65CcnbWeSSZJrADpej6bqLGSNRhhmMTZawFQs8nwvL934Ge5vU24lTwjCOKCPo6WazBqfgDBrl1Bgo35i7Fo6+BsT0jUOTY/559fUvP+4wvVwpIE62x/COxde//r4p54fP+UANVH/7KU8Oq8QjUUq20p6uYwlcTmckzPOSRxhMccvZjOvF2ZxENPmPmKrvx/ThLqYt8WPQen8XGMqYa2tDrQ2lozUN6dKpz8pOQJ0bDvLErgum0HSdKYvRxwDZZRyCp082bDKwtbWmZqpK1yqgByYOCfocKL9tzwMO3P4uV7+ztogeawuWYIWxhE4yRtICegSUeuTF6K/vS2w5I6XTkmIYHVPva6WTEoao51DzcJCSkxJZzEqn8nNelGWhIohCvVaR6pJWOynBuzGB0Z0YmPXh5Zsz76Z98DS3FHAjpXehqa8Gl696ncFQM/UuDDiQy3KQErd0yp+UsozCTWkiy7JblbyyV6mK5crLiVCeOBJfrtRkyatgoVKrCttlaxMbuYfblT8U8j8GdHCp9cGcnBAd/R++AjpkNCQpw+EMPa6/ECsvRJETTit17tJAaB99oOIQTwk6QOhfeObBuogGAAA="
        extra_info = AuctionHouse.Pets.get_pet_held_item_from_item_bytes(item_bytes)

        self.assertEqual("WASHED_UP_SOUVENIR", extra_info)

    def test_check_if_item_is_a_pet_from_item_bytes_true(self):
        item_bytes = "H4sIAAAAAAAAAG2T3W7iVhDHh2S3S6jaVbXStqpU6ayV9KYhtfkwEKkXKLCJESYpkA9S9eLgM/6Ag43sYxKn6iP0ObjtM/BgVcdmtepFLUvneOY/v5k5nlMBOIJSUAGA0gEcBKL0VwleX0RpqEoVOFTcO4Sjq0DgR8m9hFT/VKAyWaZSXj+FGJfhwBJwXG/NuSNMs9py0azWO1ivtg3HrbZrHcMQ3DUb7TnF3cTRGmMVYHIEZYXPKo0xKVKX4fUdlynC35gN9McHXxcPA+lklknf04kur63FumWFd9n8wjKtFfmvuuYw6/xH21T8viln9YH/GP6azld3+rA+lng1NpzV7Wa0GEt7MfBHvdnTqCeW9sLJHqdeczb9uHhc9Z/t2m1z9GLrs4WQ9tRq2Pm6sI3Zi/VkTwcL+77fHE2XNXvh1UeXY9++GHTcB/0Xqr4Cb0SQrCXPjuDVMIqxTMbv4Ovdtt2Vjo+rjN2gItv73ZZ6UChl4GHo4DnbbflPBnxP9u48kIHKWI+vuFd4HP2sdkJRX+22ps1DziZ8gzF8IPH+HaNIHUyY8pGtcoETJYpFLnxLTl7w6KjZPMvTfIJ9SbBrwvjIJZzsOZfBhmR8rzJOaG0lfoBSMO4qyvgDGcJIMcWXQegxUVTI3Chmhp6cEfQbgvbS0MMoZPfBC48FaHu0FTox8oTwWZTGTEWKy32t8wxYoSkqy7dPfiCRBSETe1SBznPT2Hg0KNRoxIa4Qclq+fmgfgI/7rZu9X+ewk1V/UyraeoEOi6S4TjwfFV1ZOAscxwXgo4vSNgaqb8o7wSLSvPvFYbpBwp9S6DdVg77l/1RrzueleHViK8Q3hHyt+FGMuN3ymdOfMQ1DcPb/rOKeVepOJinCpMyvCGaFboRxH9oKlujdq5Nrvr9G+1U446i09fOXS4TPNXwea2d62f6qUa/Libd56Sk9eka5pjPaoeHIrtNUFDM3l20d5F390n0Zzm/1HB4059S2WlK++NaA+utBqfbWjOdaqNTF1XeabtV7tSbyFuIjbYBcABf7GcRDgH+BRMKfS0nBAAA"
        extra_info = AuctionHouse.Pets.check_if_item_is_a_pet_from_item_bytes(item_bytes)

        self.assertTrue(extra_info)

    def test_check_if_item_is_a_pet_from_item_bytes_false(self):
        item_bytes = "H4sIAAAAAAAAAFVU3W7iRhQ+CSQBdptUW1XqTdvZdtNulEDAJkAi9YIlQOiykALJqlqtrMEe8Ci2B3nG+bnsTV+hN+11pD5GHiUPUvWMbZasL2yfc77z/1MAyMMaLwDA2jqscwd+WoONlogCtVaAjKLzPGRZYLugnwzkz7jDOh6dSyT/K8CWw+XCo3eI6ouQ5ZD7HXz/cF/vMhqSsY28E/Jw7zQqBn4arw2jVt2DnxFwSn06j4X2fqVRK1Xxj73eN8p7MXC/Vjb3wETgWIUsmCs3gZpm4ynQQWCqUDkoHxulyh7so1Ir5Iq0XBrYqQujvIvfY623myoY1d09KC/Bn8VTPUrR9aMluto4KmkKdrTkA7p+/OcP/PuIKdeQerj3kndL+FNBLlF0oJEtj9Fr9oRGZ9ymHrnsgaHpaMqlv5K3A4dh5bCm+Flxb5kdKTQDv8TUgoUc28JIr9dbYjo8ZKQpF8xWZMXtchoo8pZ7nrYHR8jq+Qvq8WD+VLnPlItMdbfy2RdCpSgoaTqyr1bSsY1pBXM0+sTK2Oc6yB6caOJu4YrgqXjiRjo7T4TOytAk5AuPFbHN/ArzuQTNvKT+goefFeaSBcIXkcQkAL7GNj3+9Sd54wnhkFEUxJVAweHDfa055TqTE3LGqCqOGbvSaYyEZHp0sEWjXvdsQlr9XuttPKxjF1OVhJJQY7AQioTcFrbLlIQfEDBl6oaxgLCA+ZzJA+LoadFWowVRIjbycE9NtF8XM3InopDMBJMv07GClyjwI09hqqhPqCQ+rsbSHqEhgy2EuFyV4Cuct3c0oKQlpNIDaRomvEBmSwjPETeB5tGKhB9jr/WJy4iv8TbiCbpXLpcEG+ETLuFVElqlXIo34FN4Pr3lfuTHmiUs3DcIOmfhTE9PvYwPOUy+8C2WFIvWb3fbg9Pm6HdyejHotocDMn4/HJ3mIDugPoNdRI1dGi5IxxM3OBboaBJGykWntce//03eUICd9q0KaVNhv6c40jIDX7pCWQuhqBKWrU8PhlMoQHbOfJmD3K/N8Xl7ZJUh2+kN2mhhI8R+o97Wm/5weGoZ8WVCoC8cPuMshA2pA8nACyfCCRWBpYtheeyaeYhdz0FehBzbN6Fz2P7tAsfAao2anUlv0M3FR3Cn0x++R5/DjjUZXUzOCvBcH0HcJJ8FCl3neLpD2ncGsh7uBv5uoMROFxzJzQxs66b7VDHMDO9Cgtm046OQEFtesmeJpU0Zb01CbEi9T4mhZ4p5epCZ5Pr2ruEtlssVTNAYIi6XJePTkdh+NsObYNH4JujMM1Bgn25HopW/Xq5aGg5LTk1CPZ/r82FdxecjTfA6XcSE/ELF+2vJeH+Rl9WxrhZ9mXF85hIi7y2Pjaaxc9kowqK/qrPZcX1aN4p1x5gVq9PatHhsOnbRbJgNp8borOLMsHdYTyYVRg3bR4eNQ6NCaidmhZy/wwRhM104fP4HKcdme9wGAAA="
        extra_info = AuctionHouse.Pets.check_if_item_is_a_pet_from_item_bytes(item_bytes)

        self.assertFalse(extra_info)

    def test_check_if_pet_has_a_held_item_from_item_bytes_true(self):
        item_bytes = "H4sIAAAAAAAAAI1U3W7iRhQ+JLtdoFK7VXvRSr2YtbJqpcWJbTB/0l4kQBanGAg4sKGqosEeg8E/1B6ncape9AH6CL3mBfoEvEVv+yBVzxBUrXpVC9maM9/5vnO+OUMRoAA5rwgAuSM48pzcbzl43orSkOeKcMzp4hgKXc9hlz5dJIj6uwjF8Tr1/cFPIYvzcGQ4cFKb6w7VG2W5rjhludxwK3Jd0xRZs5mr1Wx93nAamDeMow2LuceSAuQ5e+BpzJK9dB6eT6ifMviDZVfK7P1Scd5f+XZmVHFtjRV/YKw2NSOcZPOWUTUC3O+eV3tZ4wOszulU92/LV8tZeJ3Og4nSK4981h2pdnBzb7Y7ivnY92aWoZgrU+sHl4FpGdrsnYiPvEHbfuxPR4E5nXj9qfF4qxnZrTZZzyxTN61rdWDZyszyV/324rG/Oi/fBpcrI1Qb7vXbt9hBEV44XrLxaVaAZ70oZnkMfgmf7Lb1Sy9ZeuGCDBnH2Oe7ba3LqM+XTbLb0jda7VSHrzBohJz5vrdgoc0+2AL4eLetmshIjHANJ4jE3zvqhYQKlK6/xk/NXlLMIzwiC5T5GiNOlM59Rhz0PCFuHAUk+TH1nOQUKV8iJbKR8YbZHtaSwbdPvBep6yaEL/diZEpDh8wzIaNp+Lb/+v1X+Aa/bRrQBRO6AoHbqnrYJmMes3DBl0LmFcp0me8Qg7NA9OS2omBOOek8bMhFFCUcpEM/3j1LyBshpOz72TBOGKLcKIYirp8SD6Q1HKQFjk4i+u2xe+YTvSr4mVo7rb8GZbfVZHxQUP7PswcpJQW9LWN1Z7jUq2ukfTKWjbzFksu279lrQU4dB93wEiLq4RF8hpAsSuP9OmBh+kqc/W6r77Z+Z2i08vCsTwMGXyDb9717rEv/ASX1sbAeh+TTzgOP6TnnsTdPOUvy8AKZjNCN4M+fJZ5tmNSUxtc3RlsqSdTmaIvUdKmfsJKEdkjNarkuateqaqPeEK+ShPcpxiwhj0lLvKuC79+0JR6A8B8hw451Z1gd8641MC/Orbvxd0avd3cxGIwtETIHfSSw8Uizm4Q5UlMpSSnWjZl6hdUdXa3JjXJlLlfqFVWea1WGV52VVZ0quqNWD+J7B1vCwEMJv+TF/wocozraIwjh5P/w5aHAvYAlnAYbeNk40/QznEJVa6oaGZoAR/DR0xzCMcA/SM9rcMgEAAA="
        extra_info = AuctionHouse.Pets.check_if_pet_has_a_held_item_from_item_bytes(item_bytes)

        self.assertTrue(extra_info)

    def test_check_if_pet_has_a_held_item_from_item_bytes_false(self):
        item_bytes = "H4sIAAAAAAAAAG1UXU/jRhSdwG43RP1Qpe72pZW8EbQvBMYODgSpD8EhwdnYgZAQ4qoPE8/YnjC2s/Y4wVT9Cf0Hfed/8MOqXhu6baVasca+59xzz72eTA2hHVThNYRQZQttcVr5vYJeG3EWyUoNbUvib6OdC05ZTxA/BdafNVS7vsuEGG0illTRlknRblM/pu4xpg2Pau1Gs6XqjZMTb9FYHLV0Qlmz6altyLtM4hVLJGfpDqpKdi+zhKVl6Sp6fUNExip/sE3sm8YAk5kq3OY4WNx2uNmNfWsy1UfdK2wvXWwtz7F1vflgGh3uXgzWTihSZyruTN5pmYaJrdnVw3w2WFrhVdPu3mGre7YcTTq61b9S7a6FnW7nYdS17ufcTA3e8c3oLF9ozmrRvxnNoe6zzsB2ZjQg2v16oR3xYaf09UBmNJvfjlU3vLl2bnsquR0IxzD9ET/DbnQjXnjYuQ0wBczNS+y4rAN+p1gOJvw/sYIPepuyTzOEvItOa5i3/6WhSzLTxbw5CJzoKluEN3jYHAt2UfiYru2+ldva9GGumaoVnmvQszbqTzWrbx3Zy55wlr1gvvSxMzkLrL7N7dl8Y2sDYU06MCerOeqPA5hr016eN62HXljOyzA/lN4uMKxnbSPCP8GXqqE3lKcrQfId9GoYJ6wKwXfoi6fHEyMOF0Qql0xC6Junx+NrmbDIl8Gp8vTo4gNNR99C1IwkE4L7LHJZgRB8oJaAkXCpGAF5iUOGuvcP0CUh8f8G9D30FgCL+NxVejyin4TA4dNja0TzNGU5+gFI5U+zchnEIgY+EYqbMFLuPcg6zuMMvYfVAxmFwL3IkiTepAoACuW+kkIKQ3tA4VFRnnLP424mZF6kFxlQMWEbktAUfQfPEF2QlFEljgqRRGEfM75aMVpOpZ8U+dGPqZIQaCw/AM/fQxz+HD5YShUZK0O2ZkLRiq4Y3iva8Br/c5UwFDyEVcUYhHbLbtmY+4FsuIK7d4UcoVSRAU+VFZPwjr4GSmmseA9ZlL2H1M+hyNOjMEaWNbKr6JVNQlZO+efhWijqL1DMe/EOu+Cr83uZkI6UCV9kkqVV9AbEzMiL0cdf6zJfsfppvT82ez3Tru/XiSv5GkIeESnbr7P7Vf0UH+D9OhwGCTCfqwIxgKOmUPlEdWHA+RSmCQnPcNmcUfT2QvqtWhxcaPvyfAK+swyed1lL1zFt0wbBLm0cYa3VIJ7easCBhD2VYPUIu1W0I3nIUknCFfqyfdg+1DRFP1WxcmkhtIU+e95zaBuhvwCbVGu8JwUAAA=="
        extra_info = AuctionHouse.Pets.check_if_pet_has_a_held_item_from_item_bytes(item_bytes)

        self.assertFalse(extra_info)


if __name__ == '__main__':
    unittest.main()
