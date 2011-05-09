#!/usr/bin/python
import optparse
import re
import os
#
# This program schedules the downloads.
# usage: prog [options] URL
#

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

        (opts, args) = parser.parse_args()

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
