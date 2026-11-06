from ml_pipeline_cli.core import profile_csv

def test_profile(tmp_path):
    p=tmp_path/"x.csv"; p.write_text("a,b\n1,\n", encoding="utf-8")
    assert profile_csv(str(p))["missing_values"]["b"] == 1
