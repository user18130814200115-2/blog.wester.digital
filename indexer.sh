#!/bin/sh

generate_html() {
         cat header.html > index.html
         printf "<pre style=\"font-size: 2vw\">" > all.html

         ls -r posts/* | xargs head -n 3 | sed -Ee 's/==> (.*) <==/<a href=\"\1\">=== \1 ===<\/a>/g' | tee -a all.html | head -n 25 >> index.html

         cat footer.html >> index.html
         printf "</pre>" >> all.html
    
}

generate_rss() {
    echo "\
<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<rss version=\"2.0\">

<channel>
  <title>Wester Digital plaintext blog</title>
  <link>https://blog.wester.digital</link>
  <description>Random blogposts delivered in plaintext</description><item><title>Problems with the RSS feed?</title><description><![CDATA[<pre>Send me an email at <a href=\"mailto:rss@wester.digital\">rss@wester.digital</a> or make an issue on <a href=\"https://github.com/user18130814200115-2/plain.wester.digital\">GitHub</a> with the problem you encountered and I will try to resolve it." > feed.xml

    head -n 9999 posts/* | sed -Ee 's/>/\&amp;gt;/g' -e 's/</\&amp;lt;/g' -e 's/^==.amp.gt. (.*) .amp.lt.==$/<\/pre>]]><\/description><\/item><item><link>https:\/\/blog.wester.digital\1<\/link><title>/g' -e 's/([A-z].., [0-9]* [A-z].. [0-9]...)/<\/title><pubDate>\1<\/pubDate><description><![CDATA[<pre>/g' >> feed.xml

    echo "</pre>]]></description></item></channel></rss>" >> feed.xml
}

generate_index
generate_rss
