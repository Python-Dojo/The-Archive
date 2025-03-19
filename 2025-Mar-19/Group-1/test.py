from main import max_number_of_groups, organise_admins

data_2_4 = { 1231425: 1, 4545345: 2, 423235235: 11, 5453243423: 11 }
data_1_12 = { 323423: 11, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1 }
data_2_12 = { 323423: 11, 1: 11, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1 }

data_3_7 = { 1: 11, 2: 11, 3: 11, 4: 1, 5: 1, 6: 1, 7: 1 }

def test_max_groups():
    try:
        max_number_of_groups({234567890: 1})
        assert False # No admins
    except Exception as e:
        assert "one" in str(e).lower()
        assert "admins" in str(e).lower()
    try:
        max_number_of_groups({1234567890: 11})
        assert False
    except Exception as e:
        assert "one" in str(e).lower()
        assert "admins" in str(e).lower()
    assert max_number_of_groups({1234567890: 11, 1234567822: 11}) == 1

    # Two admins, 4 people -> 2 groups
    assert max_number_of_groups( data_2_4 ) == 1
    # one admin 12 people -> 1 group
    try:
        max_number_of_groups( data_1_12 )
        assert False
    except Exception as e:
        assert "one" in str(e).lower()
        assert "admins" in str(e).lower()
    assert max_number_of_groups( data_2_12 ) == 2

    # 3 admins 4 people -> 1 group
    assert max_number_of_groups( data_3_7 ) == 2

def test_organise_admins():
    assert len(organise_admins(data_2_4, 1)) == 1
    assert len(organise_admins(data_2_12, 2)) == 2
    print(organise_admins(data_2_12, 2))


if __name__ == "__main__":
    test_max_groups()
    test_organise_admins()
