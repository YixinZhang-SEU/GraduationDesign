# 模拟工作流到达
# import numpy as np
# import time

# class WorkflowArrivalSimulator:
#     def __init__(self, arrival_rate):
#         self.arrival_rate = arrival_rate

#     def generate_interarrival_time(self):
#         # 生成泊松分布的随机时间间隔
#         return np.random.exponential(scale=1/self.arrival_rate)

#     def simulate_workflow_arrival(self, num_arrivals):
#         for i in range(num_arrivals):
#             interarrival_time = self.generate_interarrival_time()
#             time.sleep(interarrival_time)
#             print(f"Workflow {i + 1} arrives at time {time.time()}")

# # 示例用法
# arrival_rate = 0.4  # 工作流到达率，平均每秒到达 0.4 个工作流
# num_arrivals = 10  # 模拟的工作流到达次数

# workflow_simulator = WorkflowArrivalSimulator(arrival_rate)
# workflow_simulator.simulate_workflow_arrival(num_arrivals)




# 工作流数据集
# import networkx as nx
# import numpy as np
# import os
# import matplotlib.pyplot as plt

# def build_graph_from_graphml(self,filename):
#     # 更换数据集
#     graph = nx.read_graphml(filename)
#     # 数据清洗
#     isolated_nodes = [n for n, d in graph.degree() if d == 0]
#     graph.remove_nodes_from(isolated_nodes)
#     if graph.number_of_nodes() < 10:
#         return None

#     self.num_nodes = len(graph.nodes)+2
#     self.entrance = self.nodes[0]
#     self.exit = self.nodes[-1]
#     self.num_edges = len(graph.edges)
#     self.nodes = [Node(i) for i in range(self.num_nodes)]
#     sorted_nodes = list(nx.topological_sort(graph))
#     dag = np.zeros((self.num_nodes, self.num_nodes), dtype=int)
#     dict = {}
#     tempid = 1
#     for node in sorted_nodes:
#         dict[node] = tempid
#         tempid += 1
#     for u,v,attr in graph.edges(data=True):
#         dag[dict[u],dict[v]] = 1
#     for i in range(1,self.num_nodes-1):
#         if dag[:,i].sum() == 0:
#             dag[0,i] = 1
#             self.num_edges += 1
#         if dag[i,:].sum() == 0:
#             dag[i,self.num_nodes-1] = 1
#             self.num_edges += 1

#     for i in range(self.num_nodes):
#         out_degree = 0
#         next_nodes = []
#         for j in range(self.num_nodes):
#             if dag[i, j] == 1:
#                 next_nodes.append(self.nodes[j])
#                 out_degree += 1
#         weights = [random.random() for _ in range(out_degree)]
#         total_weight = sum(weights)
#         for j, next_node in enumerate(next_nodes):
#             self.nodes[i].add_edge(next_node, weights[j] / total_weight)

#     return 1

# for file_name in os.listdir(folder_path):
#     if file_name.endswith('.graphml'):

#         ok = graph.build_graph_from_graphml(os.path.join(folder_path, file_name))

# folder_path = 'data/MicroserviceDataset'
# file_name = 'Spinnaker.graphml'
# graph = nx.read_graphml(os.path.join(folder_path, file_name))

# # print("Node:", graph.nodes())
# # print("Edges:", graph.edges())
# pos = nx.spring_layout(graph)
# nx.draw(graph, pos)
# nx.draw_networkx_edges(graph, pos)
# plt.show()



# ttttttest
# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

# class Task:
#     def __init__(self, task_id, workflow_id, cpu_required, memory_required, predecessors=None):
#         self.task_id = task_id
#         self.workflow_id = workflow_id
#         self.cpu_required = cpu_required
#         self.memory_required = memory_required
#         self.predecessors = predecessors if predecessors else []

# class Workflow:
#     def __init__(self, workflow_id, tasks):
#         self.workflow_id = workflow_id
#         self.tasks = tasks

# class EdgeServer:
#     def __init__(self, server_id, cpu_capacity, memory_capacity):
#         self.server_id = server_id
#         self.cpu_capacity = cpu_capacity
#         self.memory_capacity = memory_capacity
#         self.tasks = []

#     def assign_task(self, task):
#         # 尝试将任务分配到当前边缘服务器
#         if self.has_enough_resources(task):
#             self.tasks.append(task)
#             print(f"Task {task.task_id} assigned to Edge Server {self.server_id}")
#             return True
#         return False

#     def has_enough_resources(self, task):
#         # 检查边缘服务器的资源是否足够执行任务
#         return self.cpu_capacity >= task.cpu_required and self.memory_capacity >= task.memory_required

# class Simulation:
#     def __init__(self, edge_servers, workflows, time_slots):
#         self.edge_servers = edge_servers
#         self.workflows = workflows
#         self.time_slots = time_slots

#     def run_simulation(self):
#         for time_slot in range(self.time_slots):
#             print(f"\nTime Slot {time_slot + 1}")
#             for workflow in self.workflows:
#                 for task in workflow.tasks:
#                     # 尝试将任务分配到边缘服务器
#                     assigned = False
#                     for edge_server in self.edge_servers:
#                         assigned = edge_server.assign_task(task)
#                         if assigned:
#                             break
#                     if not assigned:
#                         print(f"Task {task.task_id} from Workflow {workflow.workflow_id} cannot be assigned.")

# # 示例用法
# edge_server1 = EdgeServer(server_id="Edge-1", cpu_capacity=10, memory_capacity=20)
# edge_server2 = EdgeServer(server_id="Edge-2", cpu_capacity=8, memory_capacity=15)
# edge_servers = [edge_server1, edge_server2]

# workflow1_tasks = [
#     Task(task_id="Task-1", workflow_id="Workflow-1", cpu_required=3, memory_required=5),
#     Task(task_id="Task-2", workflow_id="Workflow-1", cpu_required=2, memory_required=4),
#     Task(task_id="Task-3", workflow_id="Workflow-1", cpu_required=4, memory_required=6)
# ]

# workflow2_tasks = [
#     Task(task_id="Task-4", workflow_id="Workflow-2", cpu_required=5, memory_required=8),
#     Task(task_id="Task-5", workflow_id="Workflow-2", cpu_required=3, memory_required=5)
# ]

# workflow1 = Workflow(workflow_id="Workflow-1", tasks=workflow1_tasks)
# workflow2 = Workflow(workflow_id="Workflow-2", tasks=workflow2_tasks)

# workflows = [workflow1, workflow2]

# # 运行模拟
# simulation = Simulation(edge_servers=edge_servers, workflows=workflows, time_slots=60)
# simulation.run_simulation()


# import heapq

# class EdgeServer:
#     def __init__(self, server_id, resources):
#         self.server_id = server_id
#         self.resources = resources  # 服务器资源信息，例如 CPU、内存等

# class Edge:
#     def __init__(self, server1, server2, distance):
#         self.server1 = server1
#         self.server2 = server2
#         self.distance = distance

# class ShortestPathAlgorithm:
#     def __init__(self, edge_servers, edges):
#         self.edge_servers = edge_servers
#         self.edges = edges

#     def dijkstra(self, start_server, required_resources):
#         distances = {server: float('inf') for server in self.edge_servers}
#         distances[start_server] = 0
#         heap = [(0, start_server)]

#         while heap:
#             current_distance, current_server = heapq.heappop(heap)

#             if current_distance > distances[current_server]:
#                 continue

#             for edge in self.edges:
#                 neighbor = edge.server2 if edge.server1 == current_server else edge.server1
#                 new_distance = current_distance + edge.distance

#                 if new_distance < distances[neighbor]:
#                     distances[neighbor] = new_distance
#                     heapq.heappush(heap, (new_distance, neighbor))

#         # 找到距离最短且有足够资源的服务器
#         candidates = [server for server in self.edge_servers if server.resources >= required_resources]
#         nearest_server = min(candidates, key=lambda server: distances[server])

#         return nearest_server

# # 示例用法
# server1 = EdgeServer(server_id="Server-1", resources=10)
# server2 = EdgeServer(server_id="Server-2", resources=8)
# server3 = EdgeServer(server_id="Server-3", resources=12)

# edges = [
#     Edge(server1, server2, distance=5),
#     Edge(server2, server3, distance=7),
#     Edge(server1, server3, distance=10),
# ]

# edge_servers = [server1, server2, server3]

# algorithm = ShortestPathAlgorithm(edge_servers, edges)
# start_server = server1
# required_resources = 9

# nearest_server = algorithm.dijkstra(start_server, required_resources)
# print("Nearest Server:", nearest_server.server_id)



