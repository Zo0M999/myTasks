from selenium.webdriver.common.by import By
import pytest


base_url = 'http://127.0.0.1:5000'


@pytest.mark.parametrize(
    'creds',
    [
     pytest.param(('/', 'tasks'), id='tasks "only slash"'),
     pytest.param(('/tasks', 'tasks'), id='tasks "not only slash"'),
     pytest.param(('/add_task', 'add_task'), id='add_task'),
     pytest.param(('/comp_task', 'comp_task'), id='comp_task'),
     pytest.param(('/del_comp_task', 'del_comp_task'), id='del_comp_task'),
    ]
)
def test_page_titles(config, creds):
    url, expected_ans = creds
    browser = config
    browser.get(base_url + url)
    title = browser.find_element(By.TAG_NAME, "p").text
    assert title == expected_ans


def test_add_task(setup):
    browser = setup
    browser.get(base_url + '/add_task')
    browser.find_element(By.XPATH, "//input[@name='task_name']").send_keys('test_task_name')
    browser.find_element(By.XPATH, "//textarea[@name='task_desc']").send_keys('test_task_description')
    browser.find_element(By.XPATH, "//input[@value='Submit']").click()

    browser.get(base_url)
    last_added_row = browser.find_element(By.XPATH, '//table//tr[last()]').text.split()
    assert last_added_row[1:] == ['test_task_name', 'test_task_description', 'Undone']

# def test_comp_page():
#     browser = setup







