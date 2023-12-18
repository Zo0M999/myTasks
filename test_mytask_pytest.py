def test_show_tasks(setup):
    mytasks = setup
    all_tasks = mytasks.show_tasks()
    assert len(all_tasks) == 0


def test_show_tasks_inserted(setup_inserted):
    mytasks = setup_inserted
    all_tasks = mytasks.show_tasks()
    assert len(all_tasks) == 1


def test_add_task(setup):
    mytasks = setup
    mytasks.add_task('Task_1', 'Description_1')
    tasks = mytasks.show_tasks()
    assert tasks[-1][1:3] == ('Task_1', 'Description_1')


def test_completed_task(setup_inserted):
    mytasks = setup_inserted
    mytasks.completed_task('Task_1')
    tasks = mytasks.show_tasks()
    assert tasks[-1][-1:] == (1,)


def test_del_task(setup_inserted):
    mytasks = setup_inserted
    mytasks.del_task()
    tasks = mytasks.show_tasks()
    assert len(tasks) == 0
