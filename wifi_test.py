from pywifi import *

signal_threshold = -70
if __name__ == '__main__':
    try:
        wifi = PyWiFi()
        ifaces_list = wifi.interfaces()
        assert ifaces_list[0].status() not in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
        ifaces_list[0].scan()
        bessis = ifaces_list[0].scan_results()
        print("wifi接入点个数：", len(bessis),"，其中信号强度较大的接入点如下：")
        for ap in bessis:
            if ap.signal>signal_threshold:
                print('\t'.join(['%s:%s' % item for item in ap.__dict__.items()]))
    except AssertionError:
        print('断言失败，未找到无线网卡！')