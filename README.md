# meganz
Megatools itself is cool but a bit cumbersome if you want to work automated.


## Why?
Sometimes you want to make backups. Github would be great for that.
But Github forbids anything bigger than 100mb.
At Mega.nz you have 50GB free to use. There you can use this wrapper for "megatools" to manage your whole remote directory.
Once you have uploaded large files, you can even make them shareable under the web interface.

**How cool is that?**

## Requirements
`sudo apt-get install megatools`

# Using sync_backup_to_mega
`python sync_backup_to_mega.py` or `python sync_backup_to_mega.py --dryrun` to look what the script would do.
The script is configured via config.py. There you have the following settings:
* NUM_BACKUPS=4
   * Number of backups that will be kept
* BACKUP_NAME = 'Home'
   * Name of the backup
   * Will also later name the folder in mega.nz
* REMOTE_DEST = '/Root/Backups/'
   * Destination folder on mega.nz
* BACKUP_SRC = '~/'
   * Defines which folder is to be backed up.
* PRE_SYNC_HOOK = '''
   * There you can put a bash command in before starting syncing

The script will add backups until the maximum configured number is reached. The next time you run it, it will delete the oldest backup and replace it.


# megadf.sh
Show your cloud storage space usage/quota


## OPTIONS
* `--total`
    * Show only total available space (free + used).

* `--free`
    * Show only free space.

* `--used`
    * Show only used space.

* `--human, -h`
    * Display file sizes in a human readable format.

* `--mb`
    * Show in MiB units.

* `--gb`
    * Show in GiB units.

* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

# megals.sh
List all remote files


## OPTIONS
* `--export, -e`
    * For all files that are going to be listed, also display public download link with file key.
    * NOTE: Folders export doesn’t work yet.

* `--human, -h`
    * Display file sizes in a human readable format.

* `--header`
    * For long list format, display header describing all listed columns.

* `--long, -l`
    * List additional information about listed filesystem nodes. Node handle, owner, node type, file size, and the last modification date.

* `--recursive, -R`
    * List directories recursively. This is the default if no paths are specified.

* `--names, -n`
    * Show only names of nodes within the directory. This option has effect only if you specified a single path on a command line.

* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

# megamkdir.sh
Create remote directory


## OPTIONS
* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

* <remotepaths>
    * One or more remote directories to create.

* <contactemail>
    * Valid email address of a contact you want to add.



# megarm.sh
Remove remote file or directory


## OPTIONS
* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

* <remotepaths>
    * One or more remote directories to create.

* <contactemail>
    * Valid email address of a contact you want to add.

# megaput.sh
Upload individual files


## OPTIONS
* `--path <remotepath>`
    * Remote path to upload to. If this path is a directory, files are placed into the directory. If this path doesn’t exist, and it’s parent directory does, the file will be uploaded to a specified
    * path (this only works if you specify exactly one file).

* `--no-progress`
    * Disable upload progress reporting.

* `--disable-previews`
    * Never generate and upload file previews, when uploading new files

* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

* `--version`
    * Show version information

* <paths>
    * One or more local files to upload.

# megaget.sh
Download individual files


## OPTIONS
* `--path <path>`
    * Local path to download to. If this path is a directory, files are placed into the directory. If this path doesn’t exist, and it’s parent directory does, the file will be downloaded to a
    * specified file (this only works if you specify exactly one remote path).

* `--no-progress`
    * Disable download progress reporting. This is implied when streaming.

* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

* <remotepaths>
    * One or more remote files to download.

* <remotefile>
    * Remote path to a single file to stream.

# megadl.sh
Download file from a "public" Mega link (doesn’t require login)


## OPTIONS
* `--path <path>`
    * Local directory to download to. Defaults to the current working directory.

    * If <path> is -, remote file will be streamed to stdout.

* `--no-progress`
    * Disable download progress reporting. This is implied when streaming.

* `--print-names`
    * Print names/paths of successfully downloaded files (one per line).

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)

* `--version`
    * Show version information

* <links>
    * File and folder links to download from.

* <filelink>
    * Link to exported file to stream.


# megacopy.sh
Upload or download a directory tree


## OPTIONS
* `-r <remotepath>, --remote <remotepath>`
    * Remote directory path.

* `-l <path>, --local <path>`
    * Local directory path.

* `-d, --download`
    * Download files from the Mega.nz. The default is to upload.

* `-n, --dryrun`
    * Don’t perform any actual changes, just print what would be done.

* `--no-progress`
    * Disable upload progress reporting.

* `--disable-previews`
    * Never generate and upload file previews, when uploading new files

* `--reload`
    * Reload filesystem cache

* `--speed-limit <speed>`
    * Set maximum allowed upload and download speed in KiB/s. This option overrides config file settings. 0 means no limit.

* `--proxy <proxy>`
    * Use proxy server to connect to mega.nz. This option overrides config file settings. More information can be found in libcurl documentation at https://curl.haxx.se/libcurl/c/CURLOPT_PROXY.html.

* `--debug [<options>]`
    * Enable debugging of various aspects of the megatools operation. You may enable multiple debugging options separated by commas. (eg. --debug api,fs)
