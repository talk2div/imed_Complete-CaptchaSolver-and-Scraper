# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import sqlite3

# class SQLlitePipeline(object):

#     def open_spider(self, spider):
#         self.connection = sqlite3.connect("my_database.db")
#         self.c = self.connection.cursor()
#         try:
#             self.c.execute('''
#                 CREATE TABLE imed(
#                     Col_1_P TEXT,
#                     Col_1_G TEXT,
#                     Col_1_I TEXT,
#                     Col_1_H TEXT,
#                     Col_1_K TEXT,
#                     Col_1_J TEXT,
#                     Col_1_N TEXT,
#                     Col_1_L TEXT,
#                     Col_1_O TEXT,
#                     Col_1_M TEXT, 
#                 )

#             ''')
#             self.connection.commit()
#         except sqlite3.OperationalError:
#             pass

#     def close_spider(self, spider):
#         self.connection.close()


#     def process_item(self, item, spider):
#         self.c.execute('''
#             INSERT INTO imed(Col_1_P,Col_1_G,Col_1_I,Col_1_H,Col_1_K,Col_1_J,Col_1_N,Col_1_L,Col_1_O,Col_1_M) VALUES(?,?,?,?,?,?,?,?,?,?)

#         ''', (
#             item.get('Col_1_P'),
#             item.get('Col_1_G'),
#             item.get('Col_1_I'),
#             item.get('Col_1_H'),
#             item.get('Col_1_K'),
#             item.get('Col_1_J'),
#             item.get('Col_1_N'),
#             item.get('Col_1_L'),
#             item.get('Col_1_O'),
#             item.get('Col_1_M')
#         ))
#         self.connection.commit()
#         return item