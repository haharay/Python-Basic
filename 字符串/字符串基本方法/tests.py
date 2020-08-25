from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_value():
    window = get_answer_placeholders()[0]

    if "monty_python.upper()" in window:
        passed()
    else:
        failed("使用upper()方法")

if __name__ == '__main__':
    run_common_tests()
    test_value()

