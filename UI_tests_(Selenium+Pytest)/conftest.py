import pytest
from selenium import webdriver
from mytasks import MyTasks


@pytest.fixture(scope='session')
def config():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    return browser


@pytest.fixture(scope='module')
def setup(config):
    browser = config

    yield browser

    mytasks = MyTasks()
    sql = ("DELETE FROM mytasks WHERE id = (SELECT MAX(id) FROM mytasks)")
    mytasks._cursor.execute(sql)
    mytasks._db.commit()


if __name__ == "__main__":
    mytasks = MyTasks()
    mytasks._cursor.execute("SELECT MAX(id) FROM mytasks")
    print(mytasks._cursor.fetchall())

