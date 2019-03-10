# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline as files_p

import os


class CollegeFilesPipeline(files_p):

    def item_completed(self, results, item, info):
        # iterate over the local file paths of all downloaded images
        for result in [x for ok, x in results if ok]:
            path = result['path']
            # here we create the session-path where the files should be in the end
            # you'll have to change this path creation depending on your needs
            target_path = item['local_dir']

            # try to move the file and raise exception if not possible
            if not os.rename(path, target_path):
                raise FileNotFoundError("Could not move image to target folder")

            # here we'll write out the result with the new path,
            # if there is a result field on the item (just like the original code does)
            if self.FILES_RESULT_FIELD in item.fields:
                result['path'] = target_path
                item[self.FILES_RESULT_FIELD].append(result)

        return item

