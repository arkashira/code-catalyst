from validation_toolkit import ValidationToolkit, ValidationReport, FeatureUsage, ConversionFunnel
import json

def test_track_usage():
    toolkit = ValidationToolkit()
    toolkit.track_usage('feature1')
    toolkit.track_usage('feature1')
    toolkit.track_usage('feature2')
    assert toolkit.feature_usage['feature1'] == 2
    assert toolkit.feature_usage['feature2'] == 1

def test_track_conversion():
    toolkit = ValidationToolkit()
    toolkit.track_conversion('step1', 0.5)
    toolkit.track_conversion('step1', 0.7)
    toolkit.track_conversion('step2', 0.3)
    assert len(toolkit.conversion_funnels['step1']) == 2
    assert len(toolkit.conversion_funnels['step2']) == 1

def test_generate_report():
    toolkit = ValidationToolkit()
    toolkit.track_usage('feature1')
    toolkit.track_usage('feature1')
    toolkit.track_usage('feature2')
    toolkit.track_conversion('step1', 0.5)
    toolkit.track_conversion('step1', 0.7)
    toolkit.track_conversion('step2', 0.3)
    report = toolkit.generate_report()
    assert report.dau == 0
    assert report.mau == 0
    assert len(report.feature_usage) == 2
    assert len(report.conversion_funnels) == 2

def test_ab_test():
    toolkit = ValidationToolkit()
    toolkit.ab_test('feature1', ['variant1', 'variant2'])
    assert 'feature1' in toolkit.usage_data
    assert 'variant1' in toolkit.usage_data['feature1']
    assert 'variant2' in toolkit.usage_data['feature1']

def test_export_report():
    toolkit = ValidationToolkit()
    report = ValidationReport(10, 100, [FeatureUsage('feature1', 5), FeatureUsage('feature2', 3)], [ConversionFunnel('step1', 0.5), ConversionFunnel('step2', 0.7)])
    exported_report = toolkit.export_report(report)
    assert 'dau' in json.loads(exported_report)
    assert 'mau' in json.loads(exported_report)
    assert 'feature_usage' in json.loads(exported_report)
    assert 'conversion_funnels' in json.loads(exported_report)
