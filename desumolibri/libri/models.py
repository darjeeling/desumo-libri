from django.db import models

# Create your models here.


class Book:
    title
    edition
    author
    publisher
    frontpage
    create_at
    upload_at
    visible
    information_url # need to use anoymizer url forwarder
    language
    searchable  # need to add haystack
    file_format # epub? pdf ? etc ? jpg zipped
    size # 
    path # file path?

# use library?
class Tag:
    name
    pass

class
