# -*- coding: utf-8 -*-
from utils.feature_name_regex import get_text_prefix, feature_regex_match


class ignt_point(object):

    def __init__(self, cnct_type, positive_point, negative_point):
        # 连接器型号
        self.cnct_type = cnct_type
        # 此路桥丝正端/负端对应点号
        self.positive_point = positive_point
        self.negative_point = negative_point
        # 此路桥丝正端/负端是否与其他路桥丝正端/负端短接
        self.positive_short = False
        self.negative_short = False


class explosive_device(object):

    def __init__(self, expo_type, cnct_type, point_count, ignt_count):
        # 火工品型号
        self.expo_type = expo_type
        # 连接器型号
        self.cnct_type = cnct_type
        # 连接器点号数量
        self.point_count = point_count
        # 桥丝数量
        self.ignt_count = ignt_count

    def ignt_property(self, ignt_type, ignt_resistor, ignt_current, melt_time):
        # 桥丝 (igniter) 类型 1: 钝感 2: 半钝感 0: others
        self.ignt_type = ignt_type
        # 桥丝电阻 (Ω)
        self.ignt_resistor = ignt_resistor
        # 桥丝点火电流范围 (A)
        self.ignt_current = ignt_current
        # 熔断时间范围 (ms)
        self.melt_time = melt_time

    def cnct_property(self, ignt_point):
        # 桥丝对应连接器接口点号 [ignt_point]
        self.ignt_point = ignt_point

        # 正端/负端 短接列表 (桥丝之间短接)
        self.positive_short = []
        self.negative_short = []


class explosive_signal(explosive_device):

    def __init__(self, sig_name, sig_set, pos_name, device_en: explosive_device):
        super().__init__(device_en.expo_type, device_en.cnct_type, device_en.point_count, device_en.ignt_count)
        # 时序名称
        self.sig_name = sig_name
        self.sig_name_abbr = ""
        # 时序开出组
        self.sig_set = sig_set
        # 安装位置 (舱段级别)
        self.pos_name = pos_name
        self.pos_name_abbr = ""

        self.ignt_property(device_en.ignt_type, device_en.ignt_resistor, device_en.ignt_current, device_en.melt_time)
        self.cnct_property(device_en.ignt_point)
        self.positive_short = device_en.positive_short
        self.negative_short = device_en.negative_short

    def cnct_info(self, cnct_name, cnct_dict):
        self.cnct_name = cnct_name  # 连接器名称
        self.cnct_dict = cnct_dict  # 连接器点号说明


if __name__ == '__main__':
    # 火工品类 explosive_device
    fsj2_23b = explosive_device("FSJ2-23B", "YQ13-0802ZJ", 2, 1)
    fsj2_23b.ignt_property(1, (1, 1), (5, 10), (20, 5))
    m_ignt_point = []
    for positive_point, negative_point in [("1", "2")]:
        s_ignt_point = ignt_point(fsj2_23b.cnct_type, positive_point, negative_point)
        m_ignt_point.append(s_ignt_point)
    fsj2_23b.cnct_property(m_ignt_point)

    rd_1a = explosive_device("RD-1A", "JY27496E15F18ePN-H", 18, 6)
    rd_1a.ignt_property(2, (1, 1), (2.5, 10), (20, 5))
    m_ignt_point = []
    for positive_point, negative_point in [("1,2", "13"), ("3,4", "14"), ("5,6", "15"),
                                           ("7,8", "16"), ("9,10", "17"), ("11,12", "18")]:
        s_ignt_point = ignt_point(rd_1a.cnct_type, positive_point, negative_point)
        s_ignt_point.negative_short = True
        m_ignt_point.append(s_ignt_point)
    rd_1a.cnct_property(m_ignt_point)
    rd_1a.negative_short = [13, 14, 15, 16, 17, 18]

    # 时序类 explosive_signal
    xyjfdjdh = explosive_signal("芯一级发动机点火", "Gxf21&Gxf22", "芯一级级间段", fsj2_23b)
    xyjfdjdh.sig_name_abbr = get_text_prefix(xyjfdjdh.sig_name)
    xyjfdjdh.pos_name_abbr = get_text_prefix(xyjfdjdh.pos_name)
    xyjfdjdh.cnct_info("DH11", dict())

    xyjsfdcjh = explosive_signal("芯一级伺服电池激活", "Gxf31&Gxf32", "芯一级尾段", rd_1a)
    xyjsfdcjh.sig_name_abbr = get_text_prefix(xyjsfdcjh.sig_name)
    xyjsfdcjh.pos_name_abbr = get_text_prefix(xyjsfdcjh.pos_name)
    xyjsfdcjh.cnct_info("42X7", dict())

    print("Done.")
