from tartarus.constants import PrintType
from tartarus.print import Print


def test_print_error():
    Print(type_print=PrintType.ERROR)._out(message="test error message")

    assert 1 == 1


def test_print_success():
    Print(type_print=PrintType.SUCCESS)._out(message="test error message")

    assert 1 == 1


def test_print_info():
    Print(type_print=PrintType.INFO)._out(message="test error message")

    assert 1 == 1


def test_print_warning():
    Print(type_print=PrintType.WARNING)._out(title='Using Default', message="test error message")

    assert 1 == 1
