import time
import random
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def generate_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    for val in values[1:]:
        insert_node(root, val)
    return root

def recursion_count(node):
    if node is None:
        return 0
    return 1 + recursion_count(node.left) + recursion_count(node.right)

def iteration_count(root):
    if root is None:
        return 0
        
    count = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
            
    return count

def measure_execution_time(func, tree_root):
    start_time = time.perf_counter()
    result = func(tree_root)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

def count_vertex_helper1(node):
    if node is None:
        return 0
    return count_vertex_helper2(node.right) + count_vertex_helper2(node.left) + 1

def count_vertex_helper2(node):
    if node is None:
        return 0
    return 1 + count_vertex_helper1(node.left) + count_vertex_helper1(node.right)

def indirect_count(root):
    return count_vertex_helper1(root)

test_sizes = [50, 500, 5000, 50000]

results_recursion_times = []
results_iteration_times = []
results_indirect_times = []
sizes_used = []

for size in test_sizes:
    values = [random.randint(1, 1000) for _ in range(size)]
    tree_root = generate_tree(values)
    
    try:
        _, rec_time = measure_execution_time(recursion_count, tree_root)
        results_recursion_times.append(rec_time)
        
        _, iter_time = measure_execution_time(iteration_count, tree_root)
        results_iteration_times.append(iter_time)
        
        _, ind_time = measure_execution_time(indirect_count, tree_root)
        results_indirect_times.append(ind_time)
        
        sizes_used.append(size)
        
    except RecursionError:
        print(f"Ошибка рекурсии при размере {size}. Стек переполнен.")
        try:
            _, iter_time = measure_execution_time(iteration_count, tree_root)
            results_iteration_times.append(iter_time)
            results_recursion_times.append(None)
            results_indirect_times.append(None)
            sizes_used.append(size)
        except Exception as e:
            print(f"Ошибка при измерении итерации для размера {size}: {e}")

plt.figure(figsize=(12, 8))

valid_rec_times = [t for t in results_recursion_times if t is not None]
valid_ind_times = [t for t in results_indirect_times if t is not None]

if valid_rec_times:
    plt.plot(sizes_used[:len(valid_rec_times)], valid_rec_times, label='Рекурсия', marker='o')
if valid_ind_times:
    plt.plot(sizes_used[:len(valid_ind_times)], valid_ind_times, label='Косвенная рекурсия', marker='^')
plt.plot(sizes_used, results_iteration_times, label='Итерация', marker='s')

plt.xlabel('Количество узлов в дереве')
plt.ylabel('Время выполнения (секунды)')
plt.title('Экспериментальная сложность')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()
