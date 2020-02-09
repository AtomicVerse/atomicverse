#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

class atomicverse:

    def __init__(self) :
        self.dblist = {}
        self.dbobjs = {}

    def create_new_database(self, dbname) :
        dbname = str(dbname)

        if dbname in self.dblist :
            self.dblist[dbname] = uuid.uuid1()
            self.dbobjs[self.dblist[dbname]] = None
            print('DatabaseObject "{0}" has been created successfully!'.format(dbname))

        else :
            print("DatabaseObject {0} has been exist!".format(dbname))


    def add_value(self, dbname, value) :
        if (not dbname in dbname):
            print("DatabaseObject {0} not found!".format(dbname))

        else :
            self.dbobjs[self.dblist[dbname]] = value
            print('Added value in DatabaseObject {0}!'.format(dbname))




