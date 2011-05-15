#!/usr/bin/python
import optparse
import sys
import re
import os
#
# This program schedules the downloads.
# usage: prog [options] URL
#

def list_jobs(opt, optstr, val, parser):
        months={'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05',
                'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10',
                'Nov':'11', 'Dec':'12'}

        os.system ('at -l > /tmp/at-output')
        fd=file ("/tmp/at-output", 'r')

        fd1 = file ("/var/local/dl_input", "r")
        job_details = file.read (fd1)

        pattern = '(\d+)\s*(\w+) *(\w+) (\d+) (\d\d):(\d\d):\d\d \d+'
        sh_jobs=file.readline (fd)
        while sh_jobs != '':
                obj = re.match (pattern, sh_jobs)
                lst = obj.groups ()
                pattern1 = months [lst[2]] + lst[3] + lst[4] + lst[5] + ":(\w+)"
                obj = re.search (pattern1, job_details)
                if obj is not None:
                        matched_lst = obj.groups ()
                        print lst[0] +  " " + lst[1] + " " + lst[2] + " " + \
                              lst[3] + " " + lst [4] + ":" + lst[5] + " " + \
                              matched_lst [0]
                sh_jobs = file.readline (fd)

        sys.exit()

def delete_jobs(job):
        string = 'at -d ' + job
        os.system (string)
        print job + " unschduled"
        sys.exit ()

if  __name__ == '__main__':
        Valid_date='([0][1-9]|[1][0-2])([0][1-9]|[1][0-9]|[2][0-9]|[3][0-1])([0-1][0-9]|[2][0-3])([0-5][0-9])'

        parser = optparse.OptionParser (
                        usage='Usage: %prog [options] URL',
                        version='0.0.1',
                        conflict_handler='resolve',
        )

        parser.add_option ('-h', '--help', action='help',
                           help='print this text and exit')
        parser.add_option ('-t', '--time', dest='sh_time',
                           help='Scheduling time MMDDHHMM(month Day hour min)')
        parser.add_option ('-l', '--list', action='callback',
                           callback=list_jobs, help='''list the scheduled jobs,
                           job_no day month day-of-month time URL''')
        parser.add_option ('-d', '--delete', dest='job_no',
                           help='Delete the job')

        (opts, args) = parser.parse_args()

        if opts.job_no is not None:
                delete_jobs(opts.job_no)

        if args:
                print args
        else:
                parser.error(u'Please enter the URL')

        if opts.sh_time is not None:
                if re.match(Valid_date, opts.sh_time) is None:
                        parser.error (u'Invalid time format')
                else:
                        print opts.sh_time
        else:
                #call download.sh on the URL right now
                pass

        fd = file('/var/local/dl_input', 'a');
        file.write (fd, opts.sh_time + ':' + args[0] + '\n')
        fd.close()

        at_cmd='at -f /bin/download.sh -t ' + opts.sh_time

        print at_cmd

        os.system (at_cmd)
