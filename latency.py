#!/usr/bin/python
import commands
import time
import json


ip_range_dict = {"203.113.128.0/18": "VT", "220.231.64.0/18": "VT", "125.234.0.0/15": "VT", "117.0.0.0/13": "VT", \
                 "115.72.0.0/13": "VT", "27.64.0.0/12": "VT", "171.224.0.0/11": "VT", "116.96.0.0/12": "VT", \
                 "125.212.128.0/17": "VT", "125.214.0.0/18": "VT", "203.190.160.0/20": "VT", "117.103.192.0/18":"VTC", \
                 "203.162.0.0/16": "VNPT", "203.210.128.0/17": "VNPT", "221.132.0.0/18": "VNPT",\
                 "203.160.0.0/23": "VNPT","222.252.0.0/14": "VNPT", "23.16.0.0/12": "VNPT", "113.160.0.0/11": "VNPT",\
                 "14.160.0.0/11": "VNPT","14.224.0.0/11": "VNPT", "221.132.30.0/23": "VNPT", "221.132.32.0/21": "VNPT",\
                 "210.245.0.0/17": "FPT","58.186.0.0/15": "FPT", "118.68.0.0/14": "FPT", "113.22.0.0/16": "FPT",\
                 "113.23.0.0/17": "FPT","183.80.0.0/16": "FPT", "183.81.0.0/17": "FPT", "1.52.0.0/14": "FPT",\
                 "42.112.0.0/13": "FPT","103.35.64.0/22": "FPT", "43.239.148.0/22": "FPT"}

def check_latency(k,v):
    result = commands.getoutput("fping -s -q -g %s -r 1" % k)
    print result.split('\n')[11].split(" ")[1]
    print result.split('\n')[12].split(" ")[1]
    print result.split('\n')[13].split(" ")[1]
    data = {
        "time": time.strftime("%m/%d/%Y %H:%M:%S"),
        "ipaddress": k,
        "isp":v,
        "minrtt": result.split('\n')[11].split(" ")[1],
        "avgrtt": result.split('\n')[12].split(" ")[1],
        "maxrtt": result.split('\n')[13].split(" ")[1]
    }
    print data
    with open('/var/log/vccloudlatency.log', 'a') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')
if __name__ == "__main__":
    for k,v in ip_range_dict.items():
        check_latency(k,v)
