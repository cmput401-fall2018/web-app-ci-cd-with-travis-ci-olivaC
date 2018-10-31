from unittest import TestCase

import mock

from service import Service

return_value = [20]
div_value = [5]


class ServiceTest(TestCase):

    def setUp(self):
        self.service = Service()

    @mock.patch('frontend.service.Service.bad_random', return_value=return_value[0])
    def test_service_bad_random(self, x):
        """
        Tests the bad_random function for Service.
        """

        assert self.service.bad_random() == 15

    @mock.patch('frontend.service.Service.bad_random', return_value=return_value[0])
    def test_service_divide(self, x):
        """
        Tests for the divide(x) function for Service.
        """

        # Tests for Zero Division Error
        try:
            y = self.service.divide(0)
        except ZeroDivisionError:
            y = 'zero division error'
        assert y == 'zero division error'

        # Tests y > 0
        y = self.service.divide(1)
        assert y == 15

    def test_service_abs_plus(self):
        """
        Tests for the abs_plus(x) function for Service.
        """

        # Test x < 0
        assert self.service.abs_plus(-1) == 2

        # Test x > 0
        assert self.service.abs_plus(5) == 6

        # Test x == 0
        assert self.service.abs_plus(0) == 1

    @mock.patch('frontend.service.Service.bad_random', return_value=return_value[0])
    @mock.patch('frontend.service.Service.divide', return_value=return_value[0])
    def test_service_complicated_function(self, x, y):
        """
        Tests the complicated function for Service.
        """
        a = self.service.bad_random()
        b = self.service.divide(4)
        i = self.service.complicated_function(4)
        assert b == i[0]
        assert a % 2 == i[1]
