from unittest.mock import Mock, call

from homework3.task1 import cache


def test_cache():
    mock = Mock()
    cached_function = cache(times=1)(mock)
    cached_function(1, 3)
    cached_function(1, 3)
    cached_function(1, 3)
    assert mock.mock_calls == [call(1, 3)]
