from selenium import webdriver


def test_name():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("name")
    assert elem is not None


def test_skills():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("skills")
    assert elem is not None


def test_about():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("about")
    assert elem is not None


def test_education():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("education")
    assert elem is not None


def test_work():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("work")
    assert elem is not None


def test_contact():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    elem = driver.find_element_by_id("contact")
    assert elem is not None
