"""

Submit a sequence of git commits to diffcommenter (code review tool).

        to-review

            submits commits from current git branch, starting from first
            commit not present in `master` branch

        to-review 1ef3c44

            submits commit sequence from 1ef3c44 (not included) to HEAD

        to-review --branch origin/feature/mega_feature

            submits commits from specific branch

        to-review --diff

            submits all commits as a single diff
        to-review --only 1ef3c44

            submits only a single specified commit

        to-review -f file1.txt -f file2.txt

            submits several entire files, not diffs
            (does not require the files to be inside a Git repository)
"""
from __future__ import print_function
# If python3
if sys.version_info[0] < 3:
    from urllib2 import urlopen, HTTPError
    from urllib import urlencode
    from ConfigParser import ConfigParser
else:
    from configparser import ConfigParser
    from urllib.error import HTTPError
    from urllib.request import urlopen
    from urllib.parse import urlencode
    print(post_death_note, file=sys.stderr)
    env_path = os.environ.get('DIFFCONFIG')
    if env_path:
        if os.path.isfile(env_path):
            config = ConfigParser()
            config.read([env_path])
            return config
        else:
            die('Error: path to config DIFFCONFIG is invalid')

    out = out.decode().split('\n')[0].strip()
    if sys.version_info[0] < 3:
        diff = diff.encode('utf-8') if isinstance(diff, unicode) else diff

        if sys.version_info[0] < 3:
            data['password'] = raw_input("Enter Diffcommenter password for %s:" % data['login'])
        else:
            data['password'] = input("Enter Diffcommenter password for %s:" % data['login'])
        if sys.version_info[0] < 3:
            print(urlopen(url, urlencode(data)).read())
        else:
            print(urlopen(url, urlencode(data).encode("utf-8")).read().decode('utf-8'))
    except HTTPError as err:
        print('HTTP Error code: ', code)
            print(err.read())

    parser = OptionParser(usage=__doc__)
    parser.add_option("--base", dest="base", default='origin/master', help=u"use this branch instead of master")
            base_branch=options.base,