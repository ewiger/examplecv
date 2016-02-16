#!/usr/bin/python
'''
Running ilastik in headless mode on a cluster.

@author Yauhen Yakimovich <eugeny.yakimovitch@gmail.com>

For ilastik documentation see
http://ilastik.org/documentation/pixelclassification/headless.html

'''
import os
import sh


ROOT = os.path.dirname(os.path.abspath(__file__))
RUN_ILASTIK = os.path.expanduser('~/anaconda/run_ilastik.sh')
# run_ilastik = sh.Command('LAZYFLOW_THREADS=1 LAZYFLOW_TOTAL_RAM_MB=4000 ' +
run_ilastik = sh.Command(RUN_ILASTIK)


def get_ilastik_help():
    result = run_ilastik('--help')
    print result.stdout


def batch_ilastik(images_path):
    result = run_ilastik('--headless',
                         '--project', ROOT + '/example_pixelclass.ilp',
                         '--raw_data', '"%s"' % images_path,
                         # '--segmentation_image ', "ilseg/*.png",
                         )
    print dir(result)
    if result.exit_code != 0:
        print dir(result)

if __name__ == '__main__':
    # get_ilastik_help()
    batch_ilastik(ROOT + '/images/250315MatJC1-Hela_D09_T0001F001L01A02Z01C01.tif')
