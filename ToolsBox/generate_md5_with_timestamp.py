import time
import hashlib


# 获取当前时间戳
current_time = int(time.time() * 1000)

# 拼接字符串
sign_str = 'test' + str(current_time)

# 计算 MD5 哈希值
sign_md5 = hashlib.md5(sign_str.encode()).hexdigest()

# 打印结果（在 Postman 中可设置环境变量）
print(sign_md5)

