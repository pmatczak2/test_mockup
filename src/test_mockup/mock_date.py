import datetime
from unittest.mock import Mock

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)
thursday = datetime.datetime(year=2019, month=1, day=3)

datetime = Mock()


def is_weekday():
    today = datetime.datetime.today()
    return 0 <= today.weekday() < 5


datetime.datetime.today.return_value = tuesday
assert is_weekday()
datetime.datetime.today.return_value = saturday
assert not is_weekday()
datetime.datetime.today.return_value = thursday
assert is_weekday()

# Mock is a powerful tool that can be useful in many different situations. Here are a few common scenarios where you
# might want to use Mock:
#
# When you want to test code that depends on external resources (like a database or web service), but you don't want
# your tests to actually interact with those resources. In this case, you can use Mock to create a fake version of
# the external resource that behaves the way you want it to, just for the purposes of your test.
#
# When you want to test code that has side effects (like printing to the console or writing to a file), but you don't
# want your tests to actually produce those side effects. In this case, you can use Mock to "catch" the output of the
# code and check that it's what you expect.
#
# When you want to test code that depends on other functions, but those other functions are complicated or slow. In
# this case, you can use Mock to create a fake version of the dependent function that behaves in a simple,
# predictable way.
#
# So, you can use Mock whenever you want to simplify the testing process, by replacing complex or external
# dependencies with simpler, more predictable versions that you control.
#
# However, it's important to use Mock judiciously. Overusing Mock can lead to tests that don't accurately reflect how
# your code works in the real world. You should always aim to write tests that are as close to the real world as
# possible, while still being efficient and reliable.