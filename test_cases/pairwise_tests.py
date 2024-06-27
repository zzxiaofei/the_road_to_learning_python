from itertools import combinations, product
from allpairspy import AllPairs

# 生成所有可能的值
values = list(range(1, 51))


# 惰性生成 pairwise 测试用例
def generate_pairwise_tests(values, num_dropdowns=5):
    for pair in combinations(range(num_dropdowns), 2):
        for val_pair in product(values, repeat=2):
            test_case = [None] * num_dropdowns
            test_case[pair[0]], test_case[pair[1]] = val_pair
            yield test_case  # 使用生成器


# 使用生成器生成 pairwise 测试用例
pairwise_tests = list(generate_pairwise_tests(values))

# 打印生成的 pairwise 测试用例数量
print("Pairwise 测试用例数量:", len(pairwise_tests))

parameters = [
    [1, 2, 3],  # 参数 A
    ['a', 'b', 'c'],  # 参数 B
    ['X', 'Y', 'Z']  # 参数 C
]

# 生成 Pairwise 测试用例
pairwise_tests = list(AllPairs(parameters))

# 打印生成的测试用例
for i, test in enumerate(pairwise_tests):
    print(f"Test case {i + 1}: {test}")
