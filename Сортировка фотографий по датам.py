# -*- coding: utf-8 -*-

import os
import shutil
import time
import zipfile


class TimeSorter:

    def __init__(self, path):
        self.birth_time = {}
        self.path = path
        self.normalized_path = os.path.normpath(path)

    def sort(self):
        for dirpath, dirnames, filenames in os.walk(self.normalized_path):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                self.birth_time[file] = (file_time[0], file_time[1])
                full_file_path = os.path.join(dirpath, file)
                new_full_file_path = os.path.join('Photos_by_year/',
                                                  str(self.birth_time[file][0]),
                                                  str(self.birth_time[file][1]))
                if os.path.exists(new_full_file_path):
                    shutil.copy2(full_file_path, new_full_file_path)
                else:
                    os.makedirs(new_full_file_path)
                    shutil.copy2(full_file_path, new_full_file_path)


ts = TimeSorter('/100CANON')
ts.sort()


class ZipTimeSorter(TimeSorter):

    def sort(self):
        zfile = zipfile.ZipFile(self.normalized_path, 'r')
        for filename in zfile.namelist():
            date = zfile.getinfo(filename).date_time
            new_path = os.path.join('photos_by_year', str(date[0]),
                                    str(date[1]))
            zfile.extract(filename)
            if os.path.exists(new_path):
                shutil.move(filename, new_path)
            else:
                os.makedirs(new_path)
                shutil.move(filename, new_path)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'icons')
        shutil.rmtree(path)


# zts = ZipTimeSorter(path='icons.zip')
# zts.sort()
