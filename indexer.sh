#!/bin/sh

generate_html() {
         printf "<pre style=\"font-size: 2vw\">" > all.html
         printf "<pre style=\"font-size: 2vw\">" > index.html
         cat header.txt >> index.html
         printf "All content on this blog also avaiable in the form of an RSS feed at\n<a href=\"feed.xml\">feed.xml</a>.\n\n----------------------------------------------------------------------\n\nRecent posts:\n" >> index.html

         ls -r posts/* | xargs head -n 3 | sed -Ee 's/==> (.*) <==/<a href=\"\1\">=== \1 ===<\/a>/g' | tee -a all.html | head -n 25 >> index.html

         printf "=== <a href="all.html">Older Posts</a> ===" >> index.html
         cat footer.txt >> index.html
         printf "</pre>" >> all.html
         printf "<a href=\"mailto:blog@wester.digital\">&lt;blog@wester.digital&gt;</a></pre>" >> index.html
    
}

generate_rss() {
    echo "\
<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<rss version=\"2.0\">

<channel>
  <title>Wester Digital plaintext blog</title>
  <link>https://blog.wester.digital</link>
  <description>Random blogposts delivered in plaintext</description><item><title>Problems with the RSS feed?</title><description><![CDATA[<pre>Send me an email at <a href=\"mailto:rss@wester.digital\">rss@wester.digital</a> or make an issue on <a href=\"https://github.com/user18130814200115-2/plain.wester.digital\">GitHub</a> with the problem you encountered and I will try to resolve it." > feed.xml

    head -n 9999 posts/* | sed -Ee 's/>/\&amp;gt;/g' -e 's/</\&amp;lt;/g' -e 's/^==.amp.gt. (.*) .amp.lt.==$/<\/pre>]]><\/description><\/item><item><link>https:\/\/blog.wester.digital\/\1<\/link><title>/g' -e 's/([A-z].., [0-9]* [A-z].. [0-9]...)/<\/title><pubDate>\1<\/pubDate><description><![CDATA[<pre>/g' >> feed.xml

    echo "</pre>]]></description></item></channel></rss>" >> feed.xml
}

generate_gophermap() {
    cat header.txt > gophermap
    printf "\n----------------------------------------------------------------------\n\nRecent posts:\n" >> gophermap
    head -n 1 posts/* | head -n 15 | tail -r | tr '\n' ';' | sed -e 's/.==. /	/g' -e 's/ .==//g' -e 's/;;/;/g' |tr ';' '\n' | sed -e 's/^[A-z]/0&/g' >> gophermap
    printf "1All Posts	posts\n" >> gophermap
    cat footer.txt >> gophermap
    printf "<blog@wester.digital>" >> gophermap
}

generate_html
generate_rss
generate_gophermap
