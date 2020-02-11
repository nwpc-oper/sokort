# nwpc-graphics

封装中国气象局数值预报中心数值预报业务系统使用的图片制作脚本。

仅支持使用NCL绘图脚本，目前已支持的数值预报业务系统如下：

- GRAPES全球预报系统
- GRAPES区域3km预报系统

## 安装

从Github项目主页下载最新的代码，并使用pip安装。

本项目不包含业务系统使用的任何图片制作脚本，如果需要使用，请联系数值预报中心。

本项目针对气象局的内网环境开发，需要部署在CMA-PI高性能计算机或挂载二级存储的服务器上。

## 配置

本项目使用配置文件设置业务系统绘图脚本库的位置，参看`config`文件夹。

在运行前使用`NWPC_GRAPHICS_CONFIG`环境变量设置主配置文件`config.yaml`的路径，
或者手动调用load_config()函数设置。

## 使用

### Jupyter Notebook

在 Anaconda 环境中启动 Jupyter Notebook。

执行下面的代码绘制并显示 GRAPES GFS 全球预报系统 2020 年 1 月 13 日 00 时次 24 小时的整层可降水量。

```python
from nwpc_graphics.systems.grapes_gfs_gmf import show_plot

show_plot("pwat_sfc_an_aea", "20200113", "00", "24h")
```

在Jupyter Notebook中运行效果如下图所示

![](./doc/nwpc-graphics-grapes-gfs-pwat-sfc-an-aea.png)

### 命令行程序

本项目提供命令行程序`nwpc_graphics`。下面的代码使用改程序绘制上面的示例，并调用系统默认的图片浏览器显示图片。

```bash
nwpc_graphics show \
    --system=grapes_gfs_gmf \
    --plot-type=pwat_sfc_an_aea \
    --start-date=20200113 \
    --start-time=00 \
    --forecast-time=24h
```

## LICENSE

Copyright 2020, perillaroc, 数值预报中心系统业务室系统运行科。

`nwpc-graphics` 以 [GPL-3.0](./LICENSE.md) 协议授权。

本项目涉及的数值预报业务系统及图片制作脚本版权均属于中国气象局数值预报中心。