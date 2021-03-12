from python_package_demo.module_demo import send_mail
import mock
import pytest

def test_send_email_default():
    assert send_mail() == True

def test_send_email_without_mock():
    assert send_mail("test_send_email_without_mock@white-house.org") == True

@mock.patch('python_package_demo.module_demo.true_send_mail', return_value=True)
def test_send_email_with_mock_decorator(mocker):
    assert send_mail("test_send_email_with_mock@white-house.org") == True
    assert send_mail("second@white-house.org") == True
    mocker.assert_called_with("second@white-house.org")
    print("called: "      + str( mocker.called ))
    print("call_count: "  + str( mocker.call_count ))
    print("call_args: "   + str( mocker.call_args ))
    print("args_list: "   + str( mocker.call_args_list ))
    print("mock calls:\n" + str( mocker.mock_calls ))
    print("method calls:\n " + str( mocker.method_calls ))

def test_send_email_with_mock():
    with mock.patch('python_package_demo.module_demo.true_send_mail', return_value=True) as mocker:
        assert send_mail("third@white-house.org") == True
        assert send_mail("next@white-house.org") == True
        mocker.assert_called_with("next@white-house.org")
        print("called: "      + str( mocker.called ))
        print("call_count: "  + str( mocker.call_count ))
        print("call_args: "   + str( mocker.call_args ))
        print("args_list: "   + str( mocker.call_args_list ))
        print("mock calls:\n" + str( mocker.mock_calls ))
        print("method calls:\n " + str( mocker.method_calls ))