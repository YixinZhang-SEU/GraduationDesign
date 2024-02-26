import config

class Scheduler:

    def schedule(self, task, arrival_server_id, arrival_time, cluster):      # 任务(.objs), 所属服务器, 到达时间, 集群信息
        this_server = cluster.server_pool[arrival_server_id]
        funcs_to_be_exec = task.functions.values()       # 待调度函数列表
        for func in funcs_to_be_exec:
            isCpuOk = (func.cpu <= this_server.cpu_capacity)
            isMemOk = (func.mem <= this_server.mem_capacity)
            isTypeOk = (func.func_type in this_server.func_types.keys())
            if isCpuOk and isMemOk and isTypeOk:        # 资源、缓存都有：本地立即执行
                self.LocalExecution(func, arrival_server_id, cluster)
            else:
                self.RemoteExecution(func, cluster)
            # elif isTypeOk and (isCpuOk is False or isMemOk is False):
            #     self.RemoteExecution(func, cluster)
            # else:
            #     self.CloudExecution(func, cluster)


    # 本地卸载
    # 可能加冷启动时间，这里不需要改变函数开始执行时间（否则需要加传输过来的时间 / 等待时间）
    def LocalExecution(self, function, exec_server_id, cluster):
        esi = exec_server_id
        this_server = cluster.server_pool[esi]
        if this_server.func_types[function.func_type] == -1 \
        or function.start_time - this_server.func_types[function.func_type] >= config.FUNC_EXP_TIME : # 冷启动，否则不用加
            function.start_time += function.cold_st
        function.finish_time += function.start_time
        cluster.server_pool[esi].func_types[function.func_type] = function.finish_time  # 更新镜像最后使用时间

        cluster.server_pool[esi].executing_queue.append(function)    # 加入到服务器执行列表
        cluster.server_pool[esi].cpu_capacity -= function.cpu
        cluster.server_pool[esi].mem_capacity -= function.mem
    

    # 卸载到其他服务器
    # 判断卸载到哪个服务器，加传输时间，可能加冷启动时间
    def RemoteExecution(self, function, cluster):
        candidates = []     # 所有资源足够的候选服务器
        for i in range(1, config.EDGE_NUM + 1):
            ts = cluster.server_pool[i]     # this_server
            if function.cpu <= ts.cpu_capacity and function.mem <= ts.mem_capacity and function.func_type in ts.func_types.keys():
                candidates.append(i)
        if len(candidates) == 0:                # 如果没有其他服务器有相应类型，就直接在本地的服务器置换掉
            exec_server = function.belong_server
            cluster.server_pool[exec_server].func_types[function.func_type] = -1
        else:
            exec_server = min(candidates, key=lambda server: cluster.dists[function.belong_server][server]) # 距离最近的服务器
        
        function.start_time += function.funcTransTime(exec_server, cluster.dists)
        esi = exec_server
        this_server = cluster.server_pool[esi]
        if this_server.func_types[function.func_type] == -1 \
        or function.start_time - this_server.func_types[function.func_type] >= config.FUNC_EXP_TIME : # 冷启动，否则不用加
            function.start_time += function.cold_st
        function.finish_time += function.start_time
        cluster.server_pool[esi].func_types[function.func_type] = function.finish_time      # 更新镜像最后使用时间

        if esi != function.belong_server:
            cluster.server_pool[function.belong_server].workflow_queue[function.belong_wf].executing_tasks[function.belong_task].finish_time += function.funcTransTime(i, cluster.dists)

        cluster.server_pool[esi].executing_queue.append(function)    # 加入到服务器执行列表
        cluster.server_pool[esi].cpu_capacity -= function.cpu
        cluster.server_pool[esi].mem_capacity -= function.mem



    # # 卸载到云服务器
    # def CloudExecution(func, cluster):