from sokort.systems.grapes_gfs_gmf._plotter import SystemPlotter
from sokort._util import get_forecast_hour


class FcAhnePlotter(SystemPlotter):
    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        SystemPlotter.__init__(self, task, work_dir, config, **kwargs)

    def get_image_list(self):
        forecast_hour = f"{get_forecast_hour(self.forecast_timedelta):03}"
        return [{
            "path": f"./AHNE_FC_{forecast_hour}.png"
        }]