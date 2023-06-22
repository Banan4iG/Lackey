import pytest
import lackey
import time
import platform


@pytest.fixture()
def open_programms():
    lackey.App.focus("Notepad++")
    time.sleep(1)
    image_path = ["files"]
    lackey.SettingsMaster.ImagePaths = image_path
    lackey.SettingsMaster.MinSimilarity = 0.97
    result = lackey.exists("change_log.png")
    assert result != None


def test_new_project(open_programms):
    lackey.click("2023-06-22_19-25.png")
    lackey.type("Hello-world")
    time.sleep(2)
    lackey.type("a", lackey.Key.CTRL)
    lackey.rightClick("hello_world.png")
    result1 = lackey.exists("features.png")
    result2 = lackey.exists("new_project.png")
    result3 = lackey.exists("all_style.png")
    lackey.click("style.png")
    lackey.click("blue_style.png")
    time.sleep(2)
    lackey.type(lackey.Key.DELETE)
    lackey.click("close_project.png")
    assert result1 != None
    assert result2!= None
    assert result3 != None
