from sokort.systems.grapes_gfs_gmf.graphics.swfdp import SwfdpPlotter
from sokort.util import get_forecast_hour


class CentralAsiaHgt200Plotter(SwfdpPlotter):
    """
    Central Asia, geopotential height, 200 hPa

    图片样例请访问 NMC 官网：
        http://eng.nmc.cn/ca/publish/up/geopotential_height/200mb2.html
    """
    plot_types = [
        "swfdp.central_asia.hgt_200"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(CentralAsiaHgt200Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "swfdp_ca_hgt_200.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./HGT_200hPa_{self.start_time}{forecast_hour}_SWFDP_CA.png"
        }]
