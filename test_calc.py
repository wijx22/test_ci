from main import evaluate_expression

def test_addition():
    assert evaluate_expression("2+3") == 5

def test_divide_by_zero():
    assert evaluate_expression("1/0") == "Error"

def test_invalid_expression():
    assert evaluate_expression("2++") == "Error"
