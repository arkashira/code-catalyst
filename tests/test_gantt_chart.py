import pytest
from gantt_chart import GanttChart, Feature, parse_blueprint
import json

def test_gantt_chart():
    features = [Feature('Feature 1', '2022-01-01', '2022-01-31'), Feature('Feature 2', '2022-02-01', '2022-02-28')]
    chart = GanttChart(features)
    assert len(chart.features) == 2

def test_update_chart():
    features = [Feature('Feature 1', '2022-01-01', '2022-01-31'), Feature('Feature 2', '2022-02-01', '2022-02-28')]
    chart = GanttChart(features)
    new_features = [Feature('Feature 3', '2022-03-01', '2022-03-31'), Feature('Feature 4', '2022-04-01', '2022-04-30')]
    chart.update_chart(new_features)
    assert len(chart.features) == 2

def test_export_chart(tmp_path):
    features = [Feature('Feature 1', '2022-01-01', '2022-01-31'), Feature('Feature 2', '2022-02-01', '2022-02-28')]
    chart = GanttChart(features)
    output_file = tmp_path / 'output.txt'
    chart.export_chart(str(output_file))
    assert output_file.exists()

def test_parse_blueprint():
    blueprint = {'features': [{'name': 'Feature 1', 'start_date': '2022-01-01', 'end_date': '2022-01-31'}, {'name': 'Feature 2', 'start_date': '2022-02-01', 'end_date': '2022-02-28'}]}
    features = parse_blueprint(blueprint)
    assert len(features) == 2

def test_main(tmp_path, monkeypatch):
    blueprint_file = tmp_path / 'blueprint.json'
    with open(blueprint_file, 'w') as f:
        json.dump({'features': [{'name': 'Feature 1', 'start_date': '2022-01-01', 'end_date': '2022-01-31'}, {'name': 'Feature 2', 'start_date': '2022-02-01', 'end_date': '2022-02-28'}]}, f)

    output_file = tmp_path / 'output.txt'
    monkeypatch.setattr('sys.argv', ['gantt_chart.py', '--blueprint', str(blueprint_file), '--output', str(output_file)])
    from gantt_chart import main
    main()
    assert output_file.exists()
