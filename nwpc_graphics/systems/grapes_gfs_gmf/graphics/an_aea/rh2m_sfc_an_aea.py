# coding: utf-8
"""
2m 相对湿度

003 时效开始

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=03130332
"""
from nwpc_graphics.systems.grapes_gfs_gmf.graphics.an_aea import AnAeaPlotter


class Plotter(AnAeaPlotter):
    plot_types = [
        "rh2m_sfc_an_aea"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        AnAeaPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "GFS_GRAPES_RH2M_SFC_AN_AEA.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _check_forecast_time(self) -> bool:
        return not int(self.forecast_hour) == 0
