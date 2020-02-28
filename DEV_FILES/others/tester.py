#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aptdaemon import client
import os
import defer
import time

# def on_transaction_finished():
#     print('Done!')
#     os.system('touch /home/daniel/GitRepos/hsuite/DEV_FILES/hali.txt')

def on_rep(transaction, exit_state):
    print('rep')
    os.system("touch /home/daniel/TEST.txt")

def on_err():
    print('err')

pkgs = ['sl', 'wps-office']
apt_client = client.AptClient()
transaction = apt_client.update_cache()
# transaction = apt_client.install_packages(pkgs)
# transaction.set_locale("de_DE")
transaction.connect("finished", on_rep)
transaction.run()
# time.sleep(1)
print(1)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(3)
# time.sleep(1)
# print(4)
# time.sleep(1)
# print(5)

# def run(trans):
#     transaction.run(reply_handler=trans_has_started, error_handler=on_error)
#     os.system('touch /home/daniel/GitRepos/hsuite/DEV_FILES/run.txt')

# def trans_has_started():
#     print('Start')
#     os.system('touch /home/daniel/GitRepos/hsuite/DEV_FILES/start.txt')

# def on_error(error):
#     print('err')
#     os.system('touch /home/daniel/GitRepos/hsuite/DEV_FILES/err.txt')
#     raise error

# cli = client.AptClient()
# cli.update_cache(reply_handler=run, error_handler=on_error)

# def update_me():
#     apt_client = client.AptClient()
#     try:
#         transaction = yield apt_client.update_cache()
#     except errors.NotAuthorizedError:
#         print ("You are not allowed to update the cache!")
#         raise StopIteration
#     yield transaction.set_locale("de_DE")
#     yield transaction.run()
#     print ("Transaction has started")
#     os.system('touch /home/daniel/GitRepos/hsuite/DEV_FILES/err.txt')
# # sth = defer.inline_callbacks(update_cache)
# update_me()
# print('hey')

# apt_client = client.AptClient()
# pkgs = ['sl', 'umatrix', 'neofetch']
# transaction = apt_client.install_packages(pkgs, reply_handler=run, error_handler=on_error)
# transaction.result