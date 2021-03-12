from python_package_demo.module_demo import send_mail
import mock
import pytest

def test_send_email_default():
    assert send_mail() == True

def test_send_email_without_mock():
    assert send_mail("test_send_email_without_mock@white-house.org") == True

@mock.patch('python_package_demo.module_demo.true_send_mail', return_value=True)
def test_send_email_with_mock(mocker):
    assert send_mail("test_send_email_with_mock@white-house.org") == True
    mocker.call_args_list