'Function to create the HTML string with tags around the word(s)'
'Sample function and result:'
'add_tags(i,Python) -><i>Python</i>'
'add_tags(b, Python Tutorial) -> <b>Python Tutorial</b>'

def HTML_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)
print(HTML_tags('i', 'Apple'))
print(HTML_tags('b', 'Apple Iphone'))

