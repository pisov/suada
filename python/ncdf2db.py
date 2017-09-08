import sys, getopt
import glob
from tzlocal import get_localzone
from dateutil import parser
import datetime

#from netCDF4 import Dataset as netcdf

def listfiles(basedir, prefix):
  files = []
  try:
    for file in sorted(glob.glob(basedir+'/'+prefix+"*")):
      files.append(file)
  except Exception as e:
    print('Exception reading basefolder {} {}'.format(basedir,e))
  return files


def main(argv):
  basedir='./'
  prefix='wrfout_d02'
  field = None

  try:
    opts, args = getopt.getopt(argv,"h:b:p:f:",["basedir=","prefix=","field="])
  except getopt.GetoptError:
    print 'ncdf2db.py -b <basedir> ['+basedir+'] -p <prefix> ['+prefix+'] -f <field> [None] '
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'ncdf2db.py -b <basedir> ['+basedir+'] -p <prefix> ['+prefix+'] -f <field> [None]'
      sys.exit()
    elif opt in ("-b", "--basedir"):
      basedir = arg
    elif opt in ("-f", "--field"):
      field = arg
    elif opt in ("-p", "--prefix"):
      prefix = arg


  if (field == None):
    print "2D field is not supplied."
    sys.exit(1)

  flist = listfiles(basedir, prefix)

  for file in flist:
    field2D = []
    print 'Processing: ', file

#    ncfile = netcdf(file)
#    strDateTime = ncfile.variables['Times'][0].tostring().replace('_', ' ')
#    local_tz = get_localzone()
#    date = parser.parse(strDateTime)
#    strDateTimeLocal = local_tz.localize(date);

  if not(len(flist)):
    print 'No candidates for impot files found ...'
    sys.exit(1)

if __name__ == "__main__":
   main(sys.argv[1:])

