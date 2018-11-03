from selenium import webdriver


def test_home():
    driver = webdriver.Chrome()
    driver.get('http://162.246.157.145:8000/')
    test_list = ["name",
                 "about",
                 "education",
                 "work",
                 "contact",
                 ]

    for i in test_list:
        elem = driver.find_element_by_id(i)
        assert elem is not None
