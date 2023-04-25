from collections import defaultdict, deque

def task_manager (task_list: list) -> dict:
    result = defaultdict(deque)
    for task_num, serv_name, importance in task_list:
        if importance == True:
            result[serv_name].appendleft(task_num)
        if importance == False:
            result[serv_name].append(task_num)
    return result
                  
tasks = [(36871, 'office', False),
(40690, 'office', False),
(35364, 'voltage', False),
(41667, 'voltage', True),
(33850, 'office', False)]

print(task_manager(tasks))