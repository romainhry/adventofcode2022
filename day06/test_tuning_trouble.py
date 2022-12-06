from day06 import tuning_trouble


def test_getMarkerPosition_dataReturns7():
    assert tuning_trouble.getMarkerPosition("test_data.csv", 4) == 7


def test_getMarkerPosition_dataReturns19():
    assert tuning_trouble.getMarkerPosition("test_data.csv", 14) == 19
