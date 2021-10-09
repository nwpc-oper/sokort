import datetime
import os
from pathlib import Path
from typing import Dict, Optional, Union

import pandas as pd

from sokort._logging import get_logger
from sokort._util import (
    get_work_dir,
    get_data_path
)
from sokort.config import Config
from sokort.systems.grapes_gfs_gmf._plotter import SystemNclPlotter

logger = get_logger("grapes_gfs_gmf")


class TyphoonPlotter(SystemNclPlotter):
    """
    Plotter for component typhoon.
    """
    def __init__(self, task: Dict, work_dir: str, config: Dict, **kwargs):
        SystemNclPlotter.__init__(self, task, work_dir, config, **kwargs)
        self.typhoon_area = task["typhoon_area"]

    @classmethod
    def create_plotter(
            cls,
            graphics_config: Config,
            start_time: Union[datetime.datetime, pd.Timestamp],
            forecast_time: pd.Timedelta = None,
            data_directory: Optional[Union[str, Path]] = None,
            work_directory: Optional[Union[str, Path]] = None,
            verbose: Union[bool, int] = False,
            **kwargs
    ):
        """Create plotter

        Parameters
        ----------
        graphics_config: dict
            graphics config
        start_time: datetime.datetime or pd.Timestamp
            Start hour
        forecast_time: pd.Timedelta
            Forecast time duration, such as 3h.
        data_directory:
        work_directory:
        verbose:

        Returns
        -------
        SystemNclPlotter
        """
        data_path = get_data_path(
            system_name=cls.system_name,
            start_time=start_time,
            forecast_time=forecast_time,
            data_directory=data_directory
        )
        if verbose:
            logger.debug(f"data directory: {data_path}")

        system_config = graphics_config["systems"]["grapes_gfs_gmf"]
        component_config = system_config["components"]["typhoon"]

        task = {
            "ncl_dir": os.path.expandvars(component_config["ncl_dir"]),
            "script_dir": os.path.expandvars(system_config["system"]["script_dir"]),
            "data_path": data_path,
            "start_datetime": start_time.isoformat(),
            "forecast_time": forecast_time,
            "typhoon_area": kwargs["typhoon_area"]
        }

        # work dir
        work_dir = get_work_dir(
            graphics_config=graphics_config,
            work_directory=work_directory
        )
        if verbose:
            logger.debug(f"work directory: {work_dir.absolute()}")

        config = {
            "ncl_lib": os.path.expandvars(graphics_config["ncl"]["ncl_lib"]),
            "geodiag_root": os.path.expandvars(graphics_config["ncl"]["geodiag_root"]),
            "load_env_script": graphics_config["ncl"]["load_env_script"],
        }

        return cls(
            task=task,
            work_dir=work_dir,
            config=config,
            verbose=verbose
        )

