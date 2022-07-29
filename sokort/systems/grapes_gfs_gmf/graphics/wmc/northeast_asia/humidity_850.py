from sokort.systems.grapes_gfs_gmf.graphics.wmc import WmcPlotter
from sokort.util import get_forecast_hour


class NortheastAsiaHumidity850Plotter(WmcPlotter):
    """
    Northeast Asia, Humidity, 850 hPa

    图片样例请访问 WMC-BJ 官网：
        http://www.wmc-bj.net/publish/Models/Weather-Models/GRAPES_GFS/Northeast-Asia/Humidity/850hPa/index.html
    """
    plot_types = [
        "wmc.northeast_asia.humidity_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        super(NortheastAsiaHumidity850Plotter, self).__init__(task, work_dir, config, **kwargs)

        self.ncl_script_name = "nea_humidity_850.ncl"

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"

        return [{
            "path": f"./ENG_NMC_NWPR_SGGRP_ERH_NEA_L85_P9_{self.start_time}00{forecast_hour}00.png"
        }]
