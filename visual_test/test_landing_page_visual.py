import time
import pytest

from utilities.test_common_utilities import common_utilities
@pytest.mark.skip
def test_visual_landing(page,assert_snapshot)->None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(100)
    page.wait_for_load_state(timeout=3000)
    assert_snapshot(page.screenshot())

