#!/usr/bin/env python3

title = '''\
                  _                   _ _       _ _        _
__      _____ ___| |_ ___ _ __     __| (_) __ _(_| |_ __ _| |
\ \ /\ / / _ / __| __/ _ | '_|    / _` | |/ _` | | __/ _` | |
 \ V  V |  __\__ | ||  __| |   _ | (_| | | (_| | | || (_| | |
  \_/\_/ \___|___/\__\___|_|  (_) \__,_|_|\__, |_|\__\__,_|_|
                                           |__/
'''

welcome_message = '''
Welcome, to Wester.Digital, now in plaintext. Here I post poorly
written content on whatever happens to currently interest me. At
the moment, this includes: technology, philosophy, academia, and
life generally.
'''

# To this, the relevant links get appended for the platform we are on
alternatives = '''
All of my writings are available through the web, gopher and rss:
'''

# To this the email address gets appended formatted in the manner required for the format
footer = '''\
All of my writings are available free of charge and I do not
accept monetary donations. If you are feeling charitable, I
encourage you to donate to a charitable organisation or
non-profit either with your money, time, voice, or other form of
support or to simply help out a someone in need in whatever form
that may take.

Email your questions, comments, or recommendations to
'''

email = 'blog@wester.digital'
all_link = 'All posts'
posts_pre = 'Recent posts:\n'

# Internally used set strings
html_header = '<pre style=\"font-size: 2vw\">'
html_footer = '</pre>'
rss_header = '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>Wester Digital plaintext blog</title><link>https://blog.wester.digital</link><description>Random blogposts delivered in plaintext</description>'
rss_footer = '</channel></rss>'
rule = '\n' + '-' * 65 + '\n\n'
html_all_link = '=== <a href=\"all.html\">' + all_link + '</a> ===\n'
gopher_all_link = '1' + all_link + '\tposts\n'
email_web = '<a href=\"mailto:' + email + '\">&lt;' + email + '&gt;</a>'
email_gopher = '<' + email + '>'
alternatives_web = alternatives + '''\
=== <a href="feed.xml">RSS feed</a> ===
=== <a href="tilde.club:70/1/~user18130814200115/">Gopher Hole</a> ===
'''
alternatives_gopher = alternatives + '''\
h=== RSS feed ===\tURL:https://blog.wester.digital/feed.xml
h=== World Wide Web page ===\tURL:https://blog.wester.digital
'''

# Maximum number of posts on the index and gopher page
max_posts_in_index = 5

# Initialize empty generation strings
html_all_gen = ''
html_gen = ''
gopher_gen = ''
rss_gen = ''

#################################################################
#                                                               #
#                                                               #
#                         Program Start                         #
#                                                               #
#                                                               #
#################################################################

import os
# This is the code to generate all of the indexes for web, gopher, and rss
for file in sorted(os.listdir("posts"), reverse=True):
    with open('posts/' + file) as post:
        post_content = []
        if file[-3:] == 'ref':
            item_type = 9
            for line in post:
                post_content.append(line)
            location = post_content[3][:-1]
        elif file[-3:] == 'txt':
            item_type = 0
            location = 'posts/' + file
            for line in post:
                post_content.append(line)
        else:
            print('Unknown file type for ' + file)
            
    current_html = '=== <a href=\"' + location + '\">' + post_content[0][:-1] + '</a> ===\n' + ''.join(post_content[1:3]) + '\n'
    html_all_gen += current_html

    if max_posts_in_index > 0:
        html_gen += current_html
        gopher_gen += item_type + '=== ' + post_content[0][:-1] + ' ===\t' + location + '\n' + ''.join(post_content[1:3]) + '\n'
        max_posts_in_index -= 1

    rss_gen += '<item><link>https://blog.wester.digital/' + location + '</link><title>' + post_content[0][:-1] + '</title><pubDate>' + post_content[1][:-1] + '</pubDate><description><![CDATA[<pre>' + ''.join(post_content).replace('>', '&amp;gt;').replace('<', '&amp;lt;') + '</pre>]]></description></item>'


# Generate the full pages
index = html_header + title + welcome_message + alternatives_web + rule + posts_pre + html_gen + html_all_link + rule + footer + email_web + html_footer

gopher = title + welcome_message + alternatives_gopher + rule + posts_pre + gopher_gen + gopher_all_link + rule + footer + email_gopher

older = html_header + html_all_gen + html_footer

rss = rss_header + rss_gen + rss_footer

# Here we write each index to the disk
file = open("index.html", "w")
file.write(index)
file.close()

file = open("all.html", "w")
file.write(older)
file.close()

file = open("gophermap", "w")
file.write(gopher)
file.close()

file = open("feed.xml", "w")
file.write(rss)
file.close()
