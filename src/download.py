#!/usr/bin/python

import time
import re
import os

months={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

time_str = time.ctime();

ax = re.match ('\w{0,3} *(\w{0,3}) *(\d+) *(\d\d):(\d\d):\d\d *\d+', time_str)

time_tuple=ax.groups()

mm=months[time_tuple[0]]

dd= time_tuple[1]

if re.match('([0]\d)|([1]\d)', dd) is None:
        dd= '0' + dd

time_stamp=mm + dd + time_tuple[2] + time_tuple[3]

fd=file('/var/local/dl_input', 'r')

file_read=file.read(fd)

s=re.search (time_stamp + ':(\S+)', file_read)

if s is None:
        print 'pattern not found'
        exit (0)
else:
        r=s.groups()

dl_cmd='youtube-dl ' + r[0]

os.system (dl_cmd)
