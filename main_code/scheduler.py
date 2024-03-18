import config

class Scheduler:

    def schedule(self, task, arrival_server_id, arrival_time, cluster):      # 任务(.objs), 所属服务器, 到达时间, 集群信息
        this_server = cluster.server_pool[arrival_server_id]
        funcs_to_be_exec = task.functions.values()       # 待调度函数列表
        for func in funcs_to_be_exec:
            isCpuOk = (func.cpu <= this_server.cpu_capacity)
            isMemOk = (func.mem <= this_server.mem_capacity)
            isTypeOk = (func.func_type in this_server.func_types.keys())

    #         # 第一版
    #         if isCpuOk and isMemOk and isTypeOk:        # 本地资源、缓存都有：本地立即执行
    #             esi = self.LocalExecution(func, arrival_server_id, cluster)
    #         else:
    #             esi = self.RemoteExecution(func, cluster)

    #         # 占用相关资源
    #         cluster.server_pool[esi].executing_queue.append(func)    # 加入到服务器执行列表
    #         cluster.server_pool[esi].cpu_capacity -= func.cpu
    #         cluster.server_pool[esi].mem_capacity -= func.mem
            
    #         # elif isTypeOk and (isCpuOk is False or isMemOk is False):
    #         #     self.RemoteExecution(func, cluster)
    #         # else:
    #         #     self.CloudExecution(func, cluster)


    # # 本地卸载，直接开始执行
    # # 可能加冷启动时间，这里不需要改变函数开始执行时间（否则需要加传输过来的时间 / 等待时间）
    # def LocalExecution(self, function, exec_server_id, cluster):
    #     esi = exec_server_id
    #     this_server = cluster.server_pool[esi]
    #     if self.isColdst(function, this_server) == True : # 冷启动，否则不用加
    #         function.start_time += function.cold_st
    #     function.finish_time += function.start_time
    #     if function.func_type not in cluster.server_pool[esi].containers.keys():
    #         cluster.server_pool[esi].containers[function.func_type] = {}
    #     cluster.server_pool[esi].containers[function.func_type][function] = []
    #     cluster.server_pool[esi].func_types[function.func_type] = function.finish_time  # 更新镜像最后使用时间

    #     return esi


    # # 卸载到其他服务器
    # # 判断卸载到哪个服务器，加传输时间，可能加冷启动时间
    # def RemoteExecution(self, function, cluster):
    #     candidates = []     # 所有资源足够的候选服务器
    #     for i in range(1, config.EDGE_NUM + 1):
    #         ts = cluster.server_pool[i]     # this_server
    #         if function.cpu <= ts.cpu_capacity and function.mem <= ts.mem_capacity and function.func_type in ts.func_types.keys():
    #             candidates.append(i)
    #     if len(candidates) == 0:                # 如果没有其他服务器有相应类型，就直接在本地的服务器置换掉
    #         exec_server = function.belong_server
    #         cluster.server_pool[exec_server].func_types[function.func_type] = -1
    #     else:
    #         exec_server = min(candidates, key=lambda server: cluster.dists[function.belong_server][server]) # 距离最近的服务器
        
    #     function.start_time += function.funcTransTime(exec_server, cluster.dists)
    #     esi = exec_server
    #     this_server = cluster.server_pool[esi]
    #     if self.isColdst(function, this_server) == True: # 冷启动，否则不用加
    #         function.start_time += function.cold_st 
    #     function.finish_time += function.start_time
    #     cluster.server_pool[esi].func_types[function.func_type] = function.finish_time      # 更新镜像最后使用时间

    #     if esi != function.belong_server:
    #         cluster.server_pool[function.belong_server].workflow_queue[function.belong_wf].executing_tasks[function.belong_task].finish_time += function.funcTransTime(i, cluster.dists)

    #     return esi


    # # 检查函数镜像是否需要冷启动
    # def isColdst(self, function, exec_server):
    #     # 镜像缓存从未被使用过，或曾经用过但处在休眠期
    #     if exec_server.func_types[function.func_type] == -1 \
    #     or function.start_time - exec_server.func_types[function.func_type] >= config.FUNC_EXP_TIME:
    #         return True
    #     return False



            # 第二版
            if isTypeOk:
                if isCpuOk and isMemOk:
                    esi = self.ImmediateExecution(func, cluster)
                else:
                    esi = self.RemoteExecution(func, cluster)      # 卸载到其他
            else:
                if (len(cluster.server_pool[arrival_server_id].func_types) < config.MAX_CACHE_NUM) and isCpuOk and ((func.mem + func.cache_mem) <= this_server.mem_capacity):        # 镜像格子没满，还能装；资源也足够装
                    esi = self.LocalPullFunction(func, cluster)      # 本地拉镜像

                else:
                    esi = self.RemoteExecution(func, cluster)      # 卸载到其他

            cluster.server_pool[func.belong_server].workflow_queue[func.belong_wf].executing_tasks[func.belong_task].functions[func.func_id].exec_server = esi
            # 占用相关资源
            cluster.server_pool[esi].executing_queue.append(func)    # 加入到服务器执行列表
            cluster.server_pool[esi].cpu_capacity -= func.cpu
            cluster.server_pool[esi].mem_capacity -= func.mem



    # 本地卸载，直接开始执行
    # 可能加冷启动时间，这里不需要改变函数开始执行时间（否则需要加传输过来的时间 / 等待时间）
    def ImmediateExecution(self, function, cluster):
        esi = function.belong_server
        this_server = cluster.server_pool[esi]
        if self.isColdst(function, this_server) == True : # 冷启动，否则不用加
            function.start_time += function.cold_st
        function.finish_time += function.start_time
        # if function.func_type not in cluster.server_pool[esi].containers.keys():
        #     cluster.server_pool[esi].containers[function.func_type] = {}
        # cluster.server_pool[esi].containers[function.func_type][function] = []
        cluster.server_pool[esi].func_types[function.func_type] = function.finish_time  # 更新镜像最后使用时间

        return esi
    

    # 云端拉取镜像
    def LocalPullFunction(self, function, cluster):
        asi = function.belong_server
        # 拉取之后服务器资源变化
        cluster.server_pool[asi].func_types[function.func_type] = -1
        cluster.server_pool[asi].mem_capacity -= function.cache_mem
        # 要加镜像从云端拉下来的传输时间
        function.start_time += function.funcTransTime(0, cluster.dists, 0)
        # 本地直接执行
        return self.ImmediateExecution(function, cluster)
        

    # 卸载到其他服务器
    # 判断卸载到哪个服务器，加传输时间，可能加冷启动时间
    def RemoteExecution(self, function, cluster):
        candidates = []     # 所有资源足够的候选服务器
        for i in range(1, config.EDGE_NUM + 1):
            ts = cluster.server_pool[i]     # this_server
            if function.func_type in ts.func_types.keys() and function.cpu <= ts.cpu_capacity and function.mem <= ts.mem_capacity:
                candidates.append(i)
        if len(candidates) == 0:                # 如果没有其他服务器有相应类型，就上传到云服务器执行
            exec_server = 0
        else:
            exec_server = min(candidates, key=lambda server: cluster.dists[function.belong_server][server]) # 距离最近的服务器
        
        function.start_time += function.funcTransTime(exec_server, cluster.dists, 1)
        esi = exec_server
        this_server = cluster.server_pool[esi]
        if self.isColdst(function, this_server) == True: # 冷启动，否则不用加
            function.start_time += function.cold_st 
        function.finish_time += function.start_time
        cluster.server_pool[esi].func_types[function.func_type] = function.finish_time      # 更新镜像最后使用时间

        return esi


    # 检查函数镜像是否需要冷启动
    def isColdst(self, function, exec_server):
        # 镜像缓存从未被使用过，或曾经用过但处在休眠期
        if exec_server.func_types[function.func_type] == -1 \
        or function.start_time - exec_server.func_types[function.func_type] >= config.FUNC_EXP_TIME:
            return True
        return False








    

    # # 返回合适的边缘服务器，没有合适的返回0
    # def searchServer(self, function, cluster):
    #     candidates = []     # 所有资源足够的候选服务器
    #     for i in range(1, config.EDGE_NUM + 1):
    #         ts = cluster.server_pool[i]     # this_server
    #         if function.func_type in ts.func_types.keys() and function.cpu <= ts.cpu_capacity and function.mem <= ts.mem_capacity:
    #             candidates.append(i) 
    #     if len(candidates) == 0:
    #         return 0
    #     return min(candidates, key=lambda server: cluster.dists[function.belong_server][server]) # 距离最近的服务器
    

    # # 本地等待其他函数执行完毕，求最早开始时间
    # # 返回最早开始时间，在哪个函数等待队列
    # def LocalWait(self, function, server_id, cluster):
    #     ts = cluster.server_pool[server_id]
    #     min_time = float('inf')
    #     f_obj = None
    #     for key, value in ts.containers[function.func_type].items():
    #         if len(value) == 0:
    #             if key.finish_time + function.exec_time < min_time:
    #                 min_time = key.finish_time + function.exec_time
    #                 f_obj = key
    #         else:
    #             if value[-1].finish_time + function.exec_time < min_time:
    #                 min_time = key.finish_time + function.exec_time
    #                 f_obj = ke
                


    




    # # 卸载到云服务器
    # def CloudExecution(func, cluster):