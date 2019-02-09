import pytest
from random import randint
from exercises.data import get_data
from exercises.level_2.users import User, MissingItemError, LowStockError, LowCreditsError


def test_users():
    # create test data
    for person in get_data(10):
        name = person['name']
        user = User.create(name, randint(0, 1000000))

        # check user is added to the list + login works
        assert User.users[name].login(user.password)
        # negative check on login
        assert not user.login(-1)

        # positive+negative logout check
        assert user.logout(user.password)
        assert not user.logout(-1)

        # assert 'cup' not in user.items['cup']
        [user.buy('cup', 0.50) for _ in range(100)]
        assert user.credit == 50
        assert user.items['cup'] == 100
        with pytest.raises(LowCreditsError): user.buy('gold bar', 1000)

        [user.sell('cup', 1) for _ in range(100)]
        assert user.credit == 150
        assert user.items['cup'] == 0
        with pytest.raises(LowStockError): user.sell('cup', 1)
        with pytest.raises(MissingItemError): user.sell('chair', 1)

