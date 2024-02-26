from clusters import Cluster
from scheduler import Scheduler
import config
import random

# 构造服务器环境
edge_num = config.EDGE_NUM
arrival_rate = config.ARRIVAL_RATE
cluster = Cluster(edge_num)
dists = cluster.dists

scheduler_instance = Scheduler()


# 主函数
if __name__ == "__main__":
    total_t = config.TIME_SLOT    # N个时间槽，一秒一个
    receive_t = config.RECEIVE_SLOT
    workflow_id = 0                 # 工作流序号，每来一个就自增一下
    wf_completed = 0
    t = 0
    while t <= total_t:
        
        for i in range (1, edge_num + 1):
            
            if t <= receive_t:
                # 模拟工作流到达
                if random.random() <= config.ARRIVAL_RATE:   # 工作流到达
                    cluster.server_pool[i].receive_workflow(workflow_id, i, t)   # 接收
                    # print(f"server {i} receives wf at time {t}, the wf_id is {workflow_id}.")
                    workflow_id += 1

            # 模拟全局运行任务
            # 执行结束的函数弹出服务器的执行队列
            temp_exec_funcs = []
            for func in cluster.server_pool[i].executing_queue:
                if func.finish_time <= t:       # 函数执行完毕
                    cluster.server_pool[i].cpu_capacity += func.cpu     # 返还资源
                    cluster.server_pool[i].mem_capacity += func.mem
                    cluster.server_pool[func.belong_server].workflow_queue[func.belong_wf].executing_tasks[func.belong_task].functions_left -= 1
                else:
                    temp_exec_funcs.append(func)
            cluster.server_pool[i].executing_queue = temp_exec_funcs

            # 遍历工作流
            for wf in list(cluster.server_pool[i].workflow_queue.values()):
                # 查看工作流的正在被执行列表
                temp_list = {}
                for task in list(wf.executing_tasks.values()):
                    if task.isDone() == True:       # task执行完成
                        for child in task.children:
                            cluster.server_pool[i].workflow_queue[child.belong_wf].tasks[child.task_id].predecessors_left -= 1    # 通知后继节点
                        cluster.server_pool[i].workflow_queue[wf.wf_id].tasks_left -= 1
                        cluster.server_pool[i].workflow_queue[wf.wf_id].executing_tasks.pop(task.task_id)
                        
                # 查看工作流的任务列表
                while cluster.server_pool[i].workflow_queue[wf.wf_id].tasks and list(cluster.server_pool[i].workflow_queue[wf.wf_id].tasks.values())[0].isOK():    # 任务可以开始执行
                    task = list(wf.tasks.values())[0]
                    # print(f"===={cluster.server_pool[task.belong_server].workflow_queue[task.belong_wf]}")
                    cluster.server_pool[i].workflow_queue[task.belong_wf].tasks[task.task_id].changeStartTime(t)
                    cluster.server_pool[i].workflow_queue[wf.wf_id].executing_tasks[task.task_id] = cluster.server_pool[task.belong_server].workflow_queue[task.belong_wf].tasks[task.task_id]
                    scheduler_instance.schedule(task, i, t, cluster)        # 调度器
                    cluster.server_pool[i].workflow_queue[wf.wf_id].tasks.popitem(last=False)[1]
                # print(f"Time {t} tasks of wf {wf.wf_type} are {[task.task_id for task in wf.tasks]}.")

                # 查看工作流是否已经可以交付
                if cluster.server_pool[i].workflow_queue[wf.wf_id].isCompleted() == True:
                    wf_completed += 1
                    cluster.server_pool[i].workflow_queue[wf.wf_id].calSatisfaction(t)       # 计算满意度，还没写
                    del cluster.server_pool[i].workflow_queue[wf.wf_id]    # 把工作流从服务器的工作流列表中弹出去
        
        if workflow_id != 0 and wf_completed == workflow_id:
            break
        t += 1

