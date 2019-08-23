# -*- coding: utf-8 -*-
import argparse
import subprocess
from sys import exit
from datetime import datetime
import config

dryrun = False

def pre_sync_hook():
    '''
    '''
    if not dryrun:
        print('Running ' + config.PRE_SYNC_HOOK + ' before sync')
        subprocess.check_call(config.PRE_SYNC_HOOK, shell=True)
        print('Done')
    else:
        print('Would Running ' + config.PRE_SYNC_HOOK + ' before sync')
        print('Done')
    return

def get_remote_backups():
    '''
    '''
    print('Get last backups')
    subprocess.check_output('bash megals.sh --reload', shell=True)
    res = subprocess.check_output('bash megals.sh -l ' + config.REMOTE_DEST, shell=True).strip()
    print('Done')
    return res

def check_remote_backup(paths):
    '''
    if no remote exists
    '''
    print('Evaluate which is next')
    for i in range(config.NUM_BACKUPS):
        if not config.BACKUP_NAME + str(i) in paths:
            msg = 'No Remote folder ' + config.BACKUP_NAME + str(i)
            print(msg)
            return True, i
    print('Done')
    return False, None


def sync_num_backup(num=0):
    '''
    '''
    print('Starting Syncing of ' + config.BACKUP_NAME + str(num))
    if not dryrun:
        subprocess.check_output('bash megals.sh --reload', shell=True)
        subprocess.check_call('bash megamkdir.sh  ' + config.REMOTE_DEST + config.BACKUP_NAME + str(num), shell=True)
        subprocess.check_call(
            'bash megacopy.sh -l ' +
            config.BACKUP_SRC +
            ' -r ' +
            config.REMOTE_DEST +
            config.BACKUP_NAME +
            str(num),
            shell=True
            )
    else:
        print('Would run bash megals.sh --reload')
        print('Would run bash megamkdir.sh  ' + config.REMOTE_DEST + config.BACKUP_NAME + str(num))
        print(
            'Would run bash megacopy.sh -l ' +
            config.BACKUP_SRC +
            ' -r ' +
            config.REMOTE_DEST +
            config.BACKUP_NAME +
            str(num)
        )
    print('Done')
    return

def sync_dir_backup(dir):
    '''
    '''
    print('Starting Syncing of ' + dir)
    if not dryrun:
        subprocess.check_output('bash megals.sh --reload', shell=True)
        subprocess.check_call('bash megarm.sh ' + dir, shell=True)
        subprocess.check_output('bash megals.sh --reload', shell=True)
        subprocess.check_call('bash megamkdir.sh  '+ dir, shell=True)
        subprocess.check_call('bash megacopy.sh -l ' + config.BACKUP_SRC + ' -r ' + dir, shell=True)
    else:
        print('Would run bash megals.sh --reload')
        print('Would run bash megarm.sh ' + dir)
        print('Would run bash megals.sh --reload')
        print('Would run bash megamkdir.sh  '+ dir)
        print('Would run bash megacopy.sh -l ' + config.BACKUP_SRC + ' -r ' + dir)
    print('Done')
    return

def get_oldest_backup(dirs):
    '''
    '''
    print('Get oldest backup')
    dirs = dirs.strip().split('\n')
    folders = []
    for folder in dirs:
        if config.BACKUP_NAME in folder:
            folder = folder.split(' ')
            folder = list(filter(None, folder)) # clear dat list
            folders.append(folder)
    dates = {}
    for folder in folders:
        dates[folder[6]] = datetime.strptime(folder[4] + ' ' + folder[5], '%Y-%m-%d %H:%M:%S')
    oldest_folder = min(dates, key=dates.get)
    print('Done')
    return oldest_folder

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''
        This is a script which do backups to mega.nz
        '''
    )
    parser.add_argument(
        '--dryrun',
        '-d',
        action='store_true',
        dest='dryrun',
        help='''Dryrun of syncing'''
    )
    args = parser.parse_args()

    if args.dryrun:
        print('Dryrun!')
        global dryrun
        dryrun = args.dryrun

    pre_sync_hook()
    res = get_remote_backups()
    missing, num = check_remote_backup(res)
    if missing:
        sync_num_backup(num)
        exit(0)

    oldest_folder = get_oldest_backup(res)
    sync_dir_backup(oldest_folder)
    print('Syncing is done.')
    exit(0)
