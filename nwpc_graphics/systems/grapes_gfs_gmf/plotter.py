# coding: utf-8
#
# Total Precipitable Water Vapor (mm)
#   整层可降水量
#   http://nwpc.nmc.cn/list.jhtml?class_id=03130328
#
from pathlib import Path
import datetime
import os
import shutil
import subprocess

import pytimeparse


class BasePlotter(object):
    def __init__(self, task: dict, work_dir: str, config: dict):
        """
        Parameters
        ----------
        task: dict
            task config dict
            {
                "ncl_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "script_dir": "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script",
                "data_path": "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/",
                "start_datetime": datetime.datetime(2020, 1, 11, 0).isoformat(),
                "forecast_time": "3h",
            }
        work_dir: str
            work directory
        config: dict
            service config
            {
                "ncl_lib": "/home/wangdp/project/graph/ncllib",
                "geodiag_root": "/home/wangdp/project/graph/GEODIAG",
            }
        """
        self.task = task
        self.work_dir = work_dir
        self.config = config
        self.ncl_script_name = None

    def run_plot(self):
        """
        Run ncl script to draw plot in work_dir.
        """
        # magic options
        forecast_time_interval = 12
        forecast_data_format = "grib2"
        forecast_data_center = "ecmwf"
        if self.ncl_script_name is None:
            raise ValueError("ncl_script_name should be set.")
        ncl_script_name = self.ncl_script_name  # "GFS_GRAPES_PWAT_SFC_AN_AEA.ncl"

        ncl_lib = self.config["ncl_lib"]  # "/home/wangdp/project/graph/ncllib"
        geodiag_root = self.config["geodiag_root"]  # "/home/wangdp/project/graph/GEODIAG"
        geodiag_tools = str(Path(geodiag_root, "tools"))

        graphic_product_lib_root = ncl_lib

        ncl_dir = self.task["ncl_dir"]  # "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script"
        script_dir = self.task["script_dir"]  # "/home/wangdp/project/graph/operation/GMF_GRAPES_GFS_POST/tograph/script"

        data_path = self.task["data_path"]  # "/sstorage1/COMMONDATA/OPER/NWPC/GRAPES_GFS_GMF/Prod-grib/2020011021/ORIG/"

        start_datetime = datetime.datetime.fromisoformat(self.task["start_datetime"])  # datetime.datetime(2020, 1, 11, 0)
        forecast_timedelta = datetime.timedelta(seconds=pytimeparse.parse(self.task["forecast_time"]))  # datetime.timedelta(hours=3)
        start_day = start_datetime.strftime("%Y%m%d")  # 20200111
        start_time = start_datetime.strftime("%Y%m%d%H")  # 2020011100
        start_hour = f"{start_datetime.hour:02}"  # 00
        forecast_hour = f"{int(forecast_timedelta.total_seconds())//3600:03}"  # 003
        forecast_datetime = start_datetime + forecast_timedelta
        forecast_time = forecast_datetime.strftime("%Y%m%d%H")  # 2020011103

        # create environment
        Path(self.work_dir).mkdir(parents=True, exist_ok=True)

        os.chdir(self.work_dir)

        with open("grapes_meso_date", "w") as f:
            f.write(f"{start_time}{forecast_hour}\n")
            f.write(f"{forecast_time}")

        shutil.copy2(f"{script_dir}/ps2gif_NoRotation_NoPlot.scr", "ps2gif_NoRotation_NoPlot.src")
        shutil.copy2(f"{ncl_dir}/{ncl_script_name}", f"{ncl_script_name}")

        component_directory = Path(__file__).parent
        script_path = "run_ncl.sh"
        shutil.copy2(f"{str(Path(component_directory, script_path))}", script_path)
        shutil.copy2(f"{str(Path(component_directory, 'load_env.sh'))}", "load_env.sh")

        envs = os.environ
        envs.update({
                "GEODIAG_ROOT": geodiag_root,
                "GEODIAG_TOOLS": geodiag_tools,
                "GRAPHIC_PRODUCT_LIB_ROOT": graphic_product_lib_root,
                "FORECAST_DATA_FORMAT": forecast_data_format,
                "FORECAST_DATA_CENTER": forecast_data_center,
                "start_time": start_time,
                "forecast_hour": forecast_hour,
                "forecast_time_interval": f"{forecast_time_interval}",
                "data_path": data_path,
                "ncl_script_name": ncl_script_name,
        })
        pipe = subprocess.Popen(
            [f"./{str(script_path)}"],
            start_new_session=True,
            env=envs
        )

        stdout, stderr = pipe.communicate()
        pipe.wait()
        pipe.terminate()

    def show_plot(self):
        image_list = self._get_image_list()
        from IPython.display import Image, display
        for an_image in image_list:
            display(Image(filename=f"./{an_image['path']}"))

    def _get_image_list(self):
        raise NotImplemented()
