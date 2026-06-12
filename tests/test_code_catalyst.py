from code_catalyst import CodeCatalyst, TourStep

def test_start_tour():
    code_catalyst = CodeCatalyst()
    assert isinstance(code_catalyst.start_tour(), TourStep)

def test_get_current_step():
    code_catalyst = CodeCatalyst()
    assert isinstance(code_catalyst.get_current_step(), TourStep)

def test_next_step():
    code_catalyst = CodeCatalyst()
    assert isinstance(code_catalyst.next_step(), TourStep)

def test_skip_tour():
    code_catalyst = CodeCatalyst()
    assert code_catalyst.skip_tour() == "Tour skipped"

def test_replay_tour():
    code_catalyst = CodeCatalyst()
    code_catalyst.skip_tour()
    assert isinstance(code_catalyst.replay_tour(), TourStep)
