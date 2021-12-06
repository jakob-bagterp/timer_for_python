from timer.constants.decimals import default, maximum, minimum
from timer.helper.decimals import mediate
from timer import Timer

class TestDecimalsMediation():
    """As decimals both can be set on the Timer object and the timer.start() function, let's ensure that decimals set in the timer.start() function takes precedence.
    NB: Always delete Timer object after each test since it's a singleton and we therefore want to avoid conflicts."""

    def test_mediate_of_start_timer_without_any_decimals_set_by_user(self) -> None:
        """Case: When the user initiates the Timer with default decimals and doesn't set any decimals when using "timer.start()", i.e. decimals should be default value."""

        timer = Timer()
        assert mediate(timer, None) == default()
        del timer

    def test_mediate_of_start_timer_with_decimals_override_set_by_user(self) -> None:
        """Case: When the user initiates the Timer with default or custom decimals and wants to override this by using, e.g., "timer.start(decimals = 7)"."""

        decimals_range = range(minimum(), maximum() + 1)
        for decimals_timer in decimals_range:
            timer = Timer(decimals_timer)
            for decimals_start in decimals_range:
                assert mediate(timer, decimals_start) == decimals_start
            del timer
