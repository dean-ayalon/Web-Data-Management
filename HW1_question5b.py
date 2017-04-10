# -*- coding: utf-8 -*-

import requests
import lxml.html
import codecs

def question5b(url):
    r = requests.get(url)
    doc = lxml.html.fromstring(r.content)
    outfile = codecs.open("output.txt", 'w', encoding='utf8')

    outfile.write("Working on " + str(url) + "\n\n")

    # Section a
    outfile.write("***************************\n")
    outfile.write("Section A - Images\n")
    outfile.write("***************************\n")
    for t in doc.xpath("//img[@alt and string-length(@alt) != 0]/@src"):
        outfile.write(t)
        outfile.write("\n")

    # Section b
    outfile.write("***************************\n")
    outfile.write("Section B - External co.il Links\n")
    outfile.write("***************************\n")
    for t in doc.xpath("//a[contains(@href, 'co.il')]/@href"):
        outfile.write(t)
        outfile.write("\n")

    # Section c
    outfile.write("***************************\n")
    outfile.write("Section C - Second Line in First Table \n")
    outfile.write("***************************\n")
    for t in doc.xpath("/descendant::table[1]//tr[2]//td/text()"):
        print(t)
        outfile.write(t)
        outfile.write("\n")

    # Section d
    outfile.write("***************************\n")
    outfile.write("Section D - All Italic Text\n")
    outfile.write("***************************\n")
    # In links
    for t in doc.xpath("//i//a/text()"):
        outfile.write(t)
        outfile.write("\n")
    # Elsewhere
    for t in doc.xpath("//i/text()"):
        outfile.write(t)
        outfile.write("\n")

    outfile.close()


#question5b("https://en.wikipedia.org/wiki/Israel")

question5b("http://www.euronews.com/2015/03/20/uber-taxis-overtake-new-york-yellow-cabs/")
#question5b("https://www.w3schools.com/html/html_tables.asp")


