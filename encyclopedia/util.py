import re
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from markdown2 import Markdown

#### I made all MD files lowercased because my filesystem is case-sensitive
### Is there a better way or is this an acceptable answer? 

def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def sort_entries(query):
    # Returns a list of all entries matching user search query
    if query:
        return list(filter(lambda entry : re.search(query, entry), list_entries()))
    return

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title.lower()}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title.lower()}.md")
        mdText = f.read().decode("utf-8")
        # Convert given markdown to HMTML then return it
        convertedHtml = Markdown().convert(mdText)
        return convertedHtml
        
    except FileNotFoundError:
        return None
        
def get_entry_editable(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title.lower()}.md")
        return f.read().decode("utf-8")
        
    except FileNotFoundError:
        return None   
