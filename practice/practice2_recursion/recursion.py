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

def theoretical_time_complexity(n):
    """Возвращает теоретическую временную сложность O(n)."""
    return n

def theoretical_space_complexity_recursive(n):
    """
    Возвращает теоретическую пространственную сложность рекурсивной версии.
    В худшем случае (вырожденное дерево) - O(n), в лучшем (сбалансированное) - O(log n).
    """
    return n

def theoretical_space_complexity_iterative(n):
    """
    Возвращает теоретическую пространственную сложность итеративной версии.
    В худшем случае (вырожденное дерево) - O(n), в лучшем (сбалансированное) - O(log n).
    """
    return n

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
plt.title('Экспериментальная сложность: Рекурсивная vs Итеративная vs Косвенная рекурсия')
plt.legend()
plt.grid(True)
plt.yscale('log')
plt.show()

print("\n--- Отчет по анализу сложности ---")

print("\n1. Рекурсивная процедура подсчета вершин:")
print("   - Функция: recursion_count(node)")
print("   - Алгоритм: Рекурсивно вызывает себя для левого и правого поддеревьев,")
print("     добавляя 1 за текущий узел.")
print("   - Теоретическая временная сложность: O(n), где n - количество узлов.")
print("     Обоснование: Каждый узел посещается ровно один раз.")
print("   - Теоретическая пространственная сложность: O(h), где h - высота дерева.")
print("     Это связано с глубиной рекурсии и размером стека вызовов.")
print("     В худшем случае (вырожденное дерево) h=n, в лучшем (сбалансированное) h=log(n).")
print(f"   - Экспериментальные результаты времени выполнения (рекурсия): {valid_rec_times}")
print(f"     для размеров: {sizes_used[:len(valid_rec_times)]}")
print("     (Примечание: На больших размерах может происходить переполнение стека)")

print("\n2. Итеративная процедура подсчета вершин:")
print("   - Функция: iteration_count(root)")
print("   - Алгоритм: Использует явный стек (list) для обхода дерева (аналог DFS).")
print("     Посещает каждый узел один раз.")
print("   - Теоретическая временная сложность: O(n).")
print("     Обоснование: Каждый узел обрабатывается один раз.")
print("   - Теоретическая пространственная сложность: O(h), аналогично рекурсивной.")
print("     Размер явного стека зависит от структуры дерева.")
print(f"   - Экспериментальные результаты времени выполнения (итерация): {results_iteration_times}")
print(f"     для размеров: {sizes_used}")

print("\n3. Процедура подсчета с косвенной рекурсией:")
print("   - Функции: indirect_count, count_vertex_helper1, count_vertex_helper2")
print("   - Алгоритм: Функции вызывают друг друга, образуя цикл вызовов.")
print("     Каждый узел все равно посещается один раз.")
print("   - Теоретическая временная сложность: O(n).")
print("     Обоснование: Несмотря на косвенную рекурсию, общее количество операций")
print("     пропорционально количеству узлов. Рекуррентное соотношение T(n) = 1 + T(n/2) + T(n/2)")
print("     сохраняется в среднем случае, давая O(n).")
print("   - Теоретическая пространственная сложность: O(h), аналогично прямой рекурсии.")
print(f"   - Экспериментальные результаты времени выполнения (косвенная рекурсия): {valid_ind_times}")
print(f"     для размеров: {sizes_used[:len(valid_ind_times)]}")
print("     (Примечание: Также может быть ограничена переполнением стека)")

print("\n4. Анализ экспериментальных результатов:")
print("   - На малых и средних размерах (до ~50000) все три метода показывают")
print("     время выполнения, растущее примерно линейно с количеством узлов.")
print("   - Итеративный метод обычно стабильнее на больших размерах, так как ему")
print("     не грозит переполнение стека вызовов Python.")
print("   - Рекурсивные методы (обычная и косвенная) могут завершиться ошибкой")
print("     RecursionError при достижении максимальной глубины рекурсии.")

print("\n--- Пример работы на небольшом дереве ---")
example_values = [50, 30, 70, 20, 40, 60, 80]
example_tree = generate_tree(example_values)

rec_count = recursion_count(example_tree)
iter_count = iteration_count(example_tree)
ind_count = indirect_count(example_tree)

print(f"Дерево создано из значений: {example_values}")
print(f"Количество узлов (Рекурсия): {rec_count}")
print(f"Количество узлов (Итерация): {iter_count}")
print(f"Количество узлов (Косвенная рекурсия): {ind_count}")
