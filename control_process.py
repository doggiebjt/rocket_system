# -*- coding: utf-8 -*-
from utils.feature_name_regex import get_text_prefix, feature_regex_match

from rocket_system import rocket_system
from ground_system import ground_system

if __name__ == '__main__':
    # 地面&箭上控制系统实例化
    rocket_system = rocket_system("YL-1")
    ground_system = ground_system("YL-1")

    # 地面射前测试流程

    # 箭上周期控制流程

    print("Done.")
