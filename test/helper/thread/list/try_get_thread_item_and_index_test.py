from timer import Timer
import timer.constant as constant
import timer.helper.thread as thread
from _mock_data.thread_list import thread_item_default, thread_item_a, thread_item_b, thread_item_c

def test_try_get_thread_item_and_index() -> None:
    timer = Timer()
    assert len(timer.threads) == 0
    _thread_item_default = thread_item_default()
    _thread_item_a = thread_item_a()
    _thread_item_b = thread_item_b()
    _thread_item_c = thread_item_c()
    timer.threads = [
        _thread_item_default,
        _thread_item_a,
        _thread_item_b,
        _thread_item_c]
    assert len(timer.threads) == 4
    assert _thread_item_default, 0 == thread.list.try_get_thread_item_and_index(timer, constant.various.NONE_VALUE)
    assert _thread_item_a, 1 == thread.list.try_get_thread_item_and_index(timer, "A")
    assert _thread_item_b, 2 == thread.list.try_get_thread_item_and_index(timer, "B")
    assert _thread_item_c, 3 == thread.list.try_get_thread_item_and_index(timer, "C")
    del timer
