"""
1小时降水

图片样例请访问NWPC/CMA官网：
    http://nwpc.nmc.cn/list.jhtml?class_id=050301
"""
from nwpc_graphics.systems.grapes_meso_3km.plotter import SystemPlotter


class Plotter(SystemPlotter):
    plot_types = [
        "prep_1h_10mw"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict):
        SystemPlotter.__init__(self, task, work_dir, config)

        self.ncl_script_name = "grapes_meso_prep_1hr_10mw.ncl"

        if not self._check_forecast_time():
            raise ValueError(f"forecast time must greater than 0h.")

    def _get_image_list(self):
        return [{
            "path": f"GRAPES-MESOS-prep-{self.start_time}1hr_{self.forecast_hour}_China.png"
        }]

    def _check_forecast_time(self) -> bool:
        forecast_hour = int(self.forecast_hour)
        return not forecast_hour == 0
