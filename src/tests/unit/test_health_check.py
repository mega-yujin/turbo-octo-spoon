
def test_up(cli):
    resp = cli.get('/health/check')
    assert resp.status_code == 200
