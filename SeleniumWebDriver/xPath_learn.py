from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

"""
有浏览器工具复制的xpath为什么写xpath？
1.元素没有id，name，class等明显或者唯一属性
2.元素id是动态
3.元素定位工具抓取不到
4.复制xpath不稳定
复制1：/html/body/form/p[3]/button
复制2：/html/body/form/p[4]/button
元素本身没有变化，其它元素修改导致该元素定位失效

特点：灵活，稳定，万能
xpath的思想：通过路径找节点（元素属性、内容）

写xpath表达式常用俩种方式：
1.属性：//*[@属性='属性值'] 文本值：
//*[@class='am-dropdown-toggle ']
2.文本值：//*[text()='文本值']
//*[text()='人才招聘']

contains:模糊查询：属性，文本值
//*[contains(@href,'baidu')]
starts_with():以xxx开始：属性，文本值
id:success-dcbe07da-9af1-44ae-bab0-1d2ea88dd775

上下级查询：
//*[@type='password']/../../../div[3]

多个条件and：
//*[@class='mnav' and @type='password']

特殊:
svg:name属性
//*[name()='svg']

"""