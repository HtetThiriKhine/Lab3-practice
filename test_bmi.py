import lab2.bmi as bmi

def test_bmi_underweigh():
    assert bmi.calculate_bmi(1.7,50) == -1

def test_bmi_normalweigh():
    assert bmi.calculate_bmi(1.7,65) == 0

def test_bmi_overweigh():
    assert bmi.calculate_bmi(1.7,80) == 1

