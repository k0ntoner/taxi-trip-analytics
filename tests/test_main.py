from taxi_analytics.main import main


def test_main_runs_without_errors():
    assert main() == 0
