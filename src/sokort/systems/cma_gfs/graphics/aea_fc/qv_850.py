from sokort.systems.cma_gfs.graphics.aea_fc import AeaFcPlotter


class Plotter(AeaFcPlotter):
    """
    850hPa 比湿

    图片样例请访问NWPC/CMA官网：
        http://nwpc.nmc.cn/list.jhtml?class_id=0313031102
    """
    plot_types = [
        "cn.qv_850"
    ]

    def __init__(self, task: dict, work_dir: str, config: dict, **kwargs):
        AeaFcPlotter.__init__(self, task, work_dir, config, **kwargs)

        self.ncl_script_name = "GFS_GRAPES_QV_P850_FC_AEA.ncl"