# -*- coding: utf-8 -*-


class ssr_device(object):
    # https://zhuanlan.zhihu.com/p/437035678
    def __init__(self, ssr_type, ssr_usage="DH", ssr_company=""):
        # 固态继电器型号
        self.ssr_type = ssr_type
        self.ssr_company = ssr_company
        # "DH" for 点火 && "PD" for "配电"
        self.ssr_usage = ssr_usage

    def performance_indicator(self, current_max, duration_max):
        # 单个继电器能够承受40A / 200ms以上的点火需求
        self.current_max = current_max
        self.duration_max = duration_max
        # 寄生导通电阻 (Ω)
        self.rds_on = 0.1  # 缺省值
        

class emr_device(object):

    def __init__(self, emr_type, emr_usage="PD", emr_company=""):
        # 电磁继电器型号
        self.emr_type = emr_type
        self.emr_company = emr_company
        self.emr_usage = emr_usage


class diode_device(object):

    def __init__(self, diode_type, diode_usage="DH", diode_company=""):
        # 二极管型号
        self.diode_type = diode_type
        self.diode_company = diode_company
        self.diode_usage = diode_usage


class resistor_device(object):

    def __init__(self, resistor_type, resistor_usage="DH", resistor_company=""):
        # 电阻型号
        self.resistor_type = resistor_type
        self.resistor_company = resistor_company
        self.resistor_usage = resistor_usage


class ignition_circuit(object):
    
    def __init__(self, ssr_name: list[str], ssr_device: ssr_device,
                 diode_device: diode_device, resistor_device:resistor_device) -> None:
        # 继电器实例
        # 继电器名称
        # 二极管实例
        # 限流电阻实例
        # 电路连接形式
        self.ignition_type = 1
    
    def working_status(self):
        # 时序数量
        # 时序名称
        # 连接器型号
        # 连接器名称
        # 连接器点号
        # 配电电压
        self.voltage_name = "+H1"
        # 导通状态
        self.is_turn_on = False
        # 是否开出时序
        self.is_used = False


if __name__ == '__main__':

    SSR_LSSR0404 = ssr_device("LSSR-0404", ssr_usage="DH", ssr_company="771")
    SSR_LSSR0404.performance_indicator(40, 200)

    DIODE_2CZ117SC = diode_device("2CZ117SC", diode_usage="DH", diode_company="")
    RESISTOR_TRYB31W = resistor_device("TRY-B3-1W", resistor_usage="DH", resistor_company="四川永星")

    print("Done.")
