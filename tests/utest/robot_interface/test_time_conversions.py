from unittest import TestCase

from oxygen import RobotInterface
import datetime

class TestMsToTimestamp(TestCase):
    def setUp(self):
        self.interface = RobotInterface()
        self.time_format = self.interface.result.get_time_format()
        self.timezone_delta = self.interface.result.get_timezone_delta()

    def str_time_in_local_timezone(self, strtime):
        return (datetime.datetime.strptime(strtime, self.time_format) + self.timezone_delta).strftime(self.time_format)

    def test_should_be_correct(self):
        timestamp = self.interface.result.ms_to_timestamp(1533625284100.0)
        assert timestamp == self.str_time_in_local_timezone('20180807 07:01:24.100000')

        timestamp = self.interface.result.ms_to_timestamp(1533625284451.0)
        assert timestamp == self.str_time_in_local_timezone('20180807 07:01:24.451000')

    def test_should_be_associative(self):
        timestamp = self.str_time_in_local_timezone('20180807 07:01:24.300000')

        milliseconds = self.interface.result.timestamp_to_ms(timestamp)
        assert milliseconds == 1533625284300.0

        timestamp = self.interface.result.ms_to_timestamp(milliseconds)
        assert timestamp == self.str_time_in_local_timezone('20180807 07:01:24.300000')

        milliseconds = self.interface.result.timestamp_to_ms(timestamp)
        assert milliseconds == 1533625284300.0


class TestTimestampToMs(TestCase):
    def setUp(self):
        self.iface = RobotInterface()
        self.time_format = self.iface.result.get_time_format()
        self.timezone_delta = self.iface.result.get_timezone_delta()

    def str_time_in_local_timezone(self, strtime):
        return (datetime.datetime.strptime(strtime, self.time_format) + self.timezone_delta).strftime(self.time_format)

    def test_should_be_correct(self):
        milliseconds = self.iface.result.timestamp_to_ms(self.str_time_in_local_timezone('20180807 07:01:24.000'))
        assert milliseconds == 1533625284000.0

        milliseconds = self.iface.result.timestamp_to_ms(self.str_time_in_local_timezone('20180807 07:01:24.555'))
        assert milliseconds == 1533625284555.0

    def test_should_be_associative(self):
        milliseconds = 1533625284300.0

        timestamp = self.iface.result.ms_to_timestamp(milliseconds)
        assert timestamp == self.str_time_in_local_timezone('20180807 07:01:24.300000')

        milliseconds = self.iface.result.timestamp_to_ms(timestamp)
        assert milliseconds == 1533625284300.0

        timestamp = self.iface.result.ms_to_timestamp(milliseconds)
        assert timestamp == self.str_time_in_local_timezone('20180807 07:01:24.300000')
