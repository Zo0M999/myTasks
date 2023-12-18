import pytest
from mytasks import MyTasks


@pytest.fixture(scope='session')
def mytasks_instance():
    mytasks = MyTasks()

    yield mytasks

    mytasks.__del__()


@pytest.fixture(scope='module')
def setup(mytasks_instance):
    mytasks_instance._setup_database()

    yield mytasks_instance

    mytasks_instance._cursor.execute('drop table mytasks')
    mytasks_instance._db.commit()


@pytest.fixture(scope='module')
def setup_inserted(setup):
    setup.add_task('Task_1', 'Description_1')
    return setup
