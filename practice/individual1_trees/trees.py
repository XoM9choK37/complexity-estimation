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
    elif (node.left is not None) and (node.right is     None):
        return 1  + recursion_count(node.left) + recursion_count(node.right)
    elif (node.left is     None) and (node.right is not None):
        return -1 + recursion_count(node.left) + recursion_count(node.right)
    else:
        return      recursion_count(node.left) + recursion_count(node.right)

def iteration_count(root):
    if root is None:
        return 0
        
    count = 0
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if   (node.left is not None) and (node.right is     None):
            count += 1
        elif (node.left is     None) and (node.right is not None):
            count -= 1
        
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

test_sizes = [50, 500, 5000, 50_000]

results_recursion_times = []
results_iteration_times = []
sizes_used = []

for size in test_sizes:
    values = [random.randint(1, 1000) for _ in range(size)]
    tree_root = generate_tree(values)
    
    try:
        _, rec_time = measure_execution_time(recursion_count, tree_root)
        results_recursion_times.append(rec_time)
        
        _, iter_time = measure_execution_time(iteration_count, tree_root)
        results_iteration_times.append(iter_time)
        
        sizes_used.append(size)
        
    except RecursionError:
        print(f"Ошибка рекурсии при размере {size}. Стек переполнен.")
        try:
            _, iter_time = measure_execution_time(iteration_count, tree_root)
            results_iteration_times.append(iter_time)
            results_recursion_times.append(None)
            sizes_used.append(size)
        except Exception as e:
            print(f"Ошибка при измерении итерации для размера {size}: {e}")

plt.figure(figsize=(12, 8))

valid_rec_times = [t for t in results_recursion_times if t is not None]

if valid_rec_times:
    plt.plot(sizes_used[:len(valid_rec_times)], valid_rec_times, label='Рекурсия', marker='o')
plt.plot(sizes_used, results_iteration_times, label='Итерация', marker='s')

plt.xlabel('Количество узлов в дереве')
plt.ylabel('Время выполнения (секунды)')
plt.title('Экспериментальная сложность')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()

arrs = [
    [5, 1, 2, 7, 8],
    [10, 6, 12, 24, 3, 4, 5, 4.25],
    [1, 2, 3, 4],
    [10, 9, 8, 7, 12],
]
for arr in arrs:
    print(recursion_count(generate_tree(arr)),
          iteration_count(generate_tree(arr)))
