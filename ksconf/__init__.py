""" ksconf - Kintyre Splunk CONFig tool

Design goals:

 * Multi-purpose go-to .conf tool.
 * Dependability
 * Simplicity
 * No eternal dependencies (single source file, if possible; or packable as single file.)
 * Stable CLI
 * Good scripting interface for deployment scripts and/or git hooks



-------------------------------------------------

Git configuration tweaks


Setup ksconf as an external difftool provider:

    ~/.gitconfig:

        [difftool "ksconf"]
            cmd = "ksconf --force-color diff \"$LOCAL\" \"$REMOTE\" | less -R"
        [difftool]
            prompt = false
        [alias]
            ksdiff = "difftool --tool=ksconf"

    Now can run:  git ksdiff props.conf
    Test command: git config diff.conf.xfuncname



Make normal diffs show the 'stanza' on the @@ output lines

    ~/.gitconfig

        [diff "conf"]
            xfuncname = "^(\\[.*\\])$"

    attributes:
        *.conf diff=conf
        *.meta diff=conf

    Test command:

    git check-attr -a -- *.conf
"""

# _version.py is autogenerated at build time.  But is missing on first call to setup.py
try:
    from _version import version
except ImportError:
    version = None