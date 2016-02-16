#!/usr/bin/env python
'''
This script is useful for conducting manual integrating testing. It helps to
get the small image dataset and age modification time of each image so that
`checkimageset` module from canonical workflow will not complain.

'''
import os
import time
import wget

FILES = (
    '250315MatJC1-Hela_D09_T0001F001L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F001L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F001L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F002L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F002L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F002L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F003L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F003L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F003L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F004L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F004L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F004L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F005L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F005L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F005L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F006L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F006L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F006L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F007L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F007L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F007L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F008L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F008L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F008L01A02Z01C01.tif',
    '250315MatJC1-Hela_D09_T0001F009L01A01Z01C02.tif',
    '250315MatJC1-Hela_D09_T0001F009L01A01Z01C03.tif',
    '250315MatJC1-Hela_D09_T0001F009L01A02Z01C01.tif',
)
TIFF_URL = 'http://pelkmanslab.org/data/D9HYl1wIKmNNbez0/' \
           'HobbesImageSet-CV7Kformat/'


def age_file(filepath, aging=1802):
    '''Make last modification and access time of the file look older.'''
    aging = int(aging)
    current_time = int(time.time())
    new_time = current_time - aging
    os.utime(filepath, (new_time, new_time))
    print('Aging file. Turning it %s (sec) older..' % aging)
    assert current_time - os.path.getmtime(filepath) >= aging


def download_tiny_datatset(images_path):
    '''Download file from the HTTP URL.'''
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    for filename in FILES:
        file_url = TIFF_URL + filename
        out_path = os.path.join(images_path, filename)
        print('Getting: %s \n\t-> %s' % (file_url, out_path))
        wget.download(file_url, out=out_path, bar=None)
        # Age the downloaded file. This beahavior is expected,
        # by check_image_set module.
        age_file(out_path)

if __name__ == '__main__':
    project_path = os.getcwd()
    print('Downloading into: %s' % project_path)
    download_tiny_datatset(os.path.join(project_path, 'images'))

