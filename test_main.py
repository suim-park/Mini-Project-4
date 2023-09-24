# Test main.py
from main import load_data, describe_stat, pivot_table, draw_heat_map


def test_load_data():
    result_load_data = load_data()
    assert result_load_data is not None


def test_describe_stat():
    result_desc_stat = describe_stat()
    assert result_desc_stat is not None


def test_pivot_table():
    result_pivot_plot = pivot_table()
    assert result_pivot_plot is not None


def test_draw_heat_map():
    result_heat_map = draw_heat_map()
    assert result_heat_map is None


if __name__ == "__main__":
    test_load_data()
    test_describe_stat()
    test_pivot_table()
    test_draw_heat_map()
