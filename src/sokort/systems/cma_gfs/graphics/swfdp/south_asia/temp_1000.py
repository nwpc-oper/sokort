from sokort.systems.cma_gfs.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class SouthAsiaTemp1000Plotter(SwfdpPlotter):
    """
    South Asia, Temperature, 1000 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES-GFS-0521/ET0_ASA_L100_P9.html
    """
    plot_types = [
        "swfdp.south_asia.temp_1000"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(SouthAsiaTemp1000Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_sa_temp_1000.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./Temp_1000hPa_{self.start_time}{forecast_hour}_SWFDP_SA.png"
        }]