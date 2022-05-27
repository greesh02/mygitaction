import pytest
from . import code.add as add


@pytest.fixture
def addition(request):
    a = request.param[0]
    b = request.param[1]
    return add_func(a,b)

@pytest.fixture
def result(request):
    return request.param

# parameterizing fixtures so that we can run multiple testcases
@pytest.mark.parametrize("addition,result", [([1,2],3), ([3,4],7)], indirect=True)
def test_indirect(addition,result):
    assert addition == result
