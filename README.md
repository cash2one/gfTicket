# 广发北京运维工单

## 简介

用于中小安排/统计PC运维人员的工作，并附带一些其他功能。

## 主要功能：


### 工单登记


**普通工单** 

* 根据故障现象创建工单。
    * 可存在多个故障现象，故障现象和工单属多对多关系。
    * 故障现象可影响工单的默认属性。
* 根据所在城区分配工单。
    * 网点\部门隶属于区域。
    * 区域和人员属多对多关系。
* 维护人员可在工单可提交附件。
    * 可创建必须提交附件的工单。
* 简单的统计功能。
* 每次操作简单的日志记录功能。
* 人员分级:
    * 管理员：可进行任何操作。
    * CallCenter：可登记工单。
    * 维护人员：仅可处理工单。
* 对应模块:`SupportTicketSystem`

**批量事件**

* 创建具有统一属性的批量事件，每个子事件可属于独立的网点/部门

### 签到管理

* 运维人员的签到登记
    * 适用于维护人员属于外包编制，独立于企业员工的签到管理系统。
* 人员分级:
    * 访客：查询在岗情况。
    * 维护人员：签到、签退、查看自己的签到记录。
    * 管理员：查看所有人的签到记录。
* 对应模块:`AttendanceSystem`

### 文件下载系统

* 简单的文件上传下载功能，配合其他系统使用。
* 对应模块:`DownloadCenter`

### 运维文档

* 管理员可使用Markdown格式书写运维文档，供企业员工/维护人员使用。
* 人员及文章分级:
    * 访客
    * 普通权限
    * 高级权限
* 文章分类：
    * 基于标签(Tag)
    * 基于涉及的业务系统
* 对应模块:`Document`

### 统一登陆

* 可支持域用户登录或本地用户登录。
* 对应模块:`SSO`


### IP地址扫描

* 按子网添加
    * 子网可选绑定网点/部门，用于查询IP归属
* 扫描子网内的IP
    * 通过Ping：并记录最后一次可用时间。
    * 通过SMB协议：获取主机名。
* 使用python-rq任务队列，在启动16个线程的情况下，每小时扫描约6000个IP。占用2个CPU核心（2.5Ghz Xeon）
* 对应模块:`IPAddress`


## 系统要求

* Python 3.5
* Django >= 1.9.0
* Postgresql >=9.4
* memcached >= 1.4
* redis >= 2.8
* 在Windows下，使用[rq-win](https://github.com/michaelbrooks/rq-win)可使用全部功能，但性能受限。
* 推荐在debian linux下部署生产环境。


## Changelog & Todo



## License

    Copyright 2016 liantian
    http://www.apache.org/licenses/LICENSE-2.0
