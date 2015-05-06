
from subprocess import Popen, PIPE
import os
import sys
import urllib
import urllib2


CLIENT_VERSION = None
    sha1, ref = out.strip().split(' ', 1)
def read_diff(only_commit=None, from_commit=None, base_branch='develop', single_diff=False, head='HEAD', diff_context=15):
        cmd = "git show -U%s " % diff_context
def make_fake_diff_from_files(filenames):
    """ Соорудить что-то похожее на вывод diff, если бы добавили несколько новых файлов """
    difflines = []
    difflines.extend([
        "commit 0000000000000000000000000000000000000000",
        "Author: Committer Guy <commiter.guy@gmail.com>",
        "Date:   Tue Feb 19 13:46:55 2013 +0400",
        "",
        "    Fake commit",
        "",
    ])

    for filename in filenames:
        file_lines = ['+' + line.rstrip('\n') for line in open(filename).readlines()]
        difflines.extend([
            "diff --git a/{} b/{}".format(filename, filename),
            "new file mode 100644",
            "index 0000000..1111111",
            "--- /dev/null",
            "+++ a/{}".format(filename),
            "@@ -0,0 +1,{} @@".format(len(file_lines)),
        ])
        difflines.extend(file_lines)
    return '\n'.join(difflines)


        'client_version': str(CLIENT_VERSION),
    try:
        print urllib2.urlopen(url, urllib.urlencode(data)).read()
    except urllib2.HTTPError as err:
        code = err.getcode()
        print 'HTTP Error code: ', code
        if code == 400:
            print err.read()
    parser.add_option("--file", "-f", dest="review_files", default=None, action="append", help=u"review an entire single file instead of a git diff")
    parser.add_option("-C", dest="diff_context", default="15", help=u"number of lines for diff context")
    if options.review_files:
        branch = ', '.join(options.review_files)
        if len(branch) > 50:
            branch = branch[:47] + "..."
        diff = make_fake_diff_from_files(options.review_files)
    else:
        branch = options.branch or get_current_branch_name()
        head = options.branch or 'HEAD'
        if branch.startswith('feature/') or branch.startswith('origin/feature/'):
            base_branch = 'origin/develop'
        # TODO считать оверрайд из argparse

        diff = read_diff(
            base_branch=base_branch,
            only_commit=options.only_commit,
            from_commit=from_commit,
            single_diff=options.single_diff,
            head=head,
            diff_context=options.diff_context,
        )