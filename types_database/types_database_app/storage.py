# -*- coding: utf-8 -*-
from django.core.files.storage import FileSystemStorage
import os

class AutoNamingStorage(FileSystemStorage):
    def get_available_name(self, name):
        """"Instead of appending underscores adds nicer-looking number."""
        dir_part, file_part = os.path.split(name)
        counter = 0;
        while True:
            try:
                dot_index = file_part.rindex('.')
            except ValueError:
                name = os.path.join(dir_part, \
                    file_part + '-' + counter.__str__())
            else:
                name = os.path.join(dir_part, file_part[:dot_index] + '-' \
                    + counter.__str__() + file_part[dot_index:])
            if not self.exists(name):
                break
            counter += 1
        return name

