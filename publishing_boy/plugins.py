import os
from datetime import datetime
from publishing_boy import config
"""Here are functions that serve the
role of plugins. Each function
accepts tuple object with:
- filename
- content
- path

Those functions are loaded to the program
by a decorator, during module loading.
Functions are stored inside a list.
"""


def title_extractior(obj):
    """Extract title from content.
    Use NTLK to do stuff with text. - maybe later

    for know i will use first sentence in text

    @return: 'title', generated_content"""
    _, _, _, content = obj

    if not content:
        return 'title', ''

    cut  = 40 if len(content) >= 40 else len(content)

    title = content[:cut].strip() + " ..."
    pos = content.find(".")

    if pos != -1:
        title = content[:pos].strip()

    return 'title', title


def creation_date(obj):
    """Extract date when the file was
    created.

    @return: 'date', date(YYYY-mm-dd HH:MM:SS)"""
    _, _, abspath, _ = obj
    return 'cdate', datetime.fromtimestamp(os.path.getctime(abspath))


def modified_date(obj):
    """Extract date when the file was
    modified.

    @return: 'modified', date(YYYY-mm-dd HH:MM:SS)"""
    _, _, abspath, _ = obj
    return 'mdate', datetime.fromtimestamp(os.path.getmtime(abspath))


def category_extract(obj):
    """Extract category. Category are
    the folder names in path file.

    @return: 'category', 'String, Separated, by'
    """
    _, filepath, _, _ = obj
    names = filter(None, os.path.dirname(filepath).split("/"))
    categories = ", ".join(map(str.capitalize, names))

    return 'categories', categories


def authors(obj):
    """Return authors"""
    return 'authors', config['Posts'].get('author', '')
