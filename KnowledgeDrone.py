# The Mathias Crawford Knowledge Drone
# 
# Here's how this old bird flies. 
# 
# Set the root url, remembering to remove the # after 'pg='.
# EXAMPLE: http://bookre.org/reader?file=1077091&pg=
# 
# Set the page_count.
# EXAMPLE: You know how numbers work.
# 
# Set the out_folder where you want the images saved.
# EXAMPLE: /Users/Mathias/Desktop/cat_recipes
#
#                    .............                .""".             .""".    
#            ..."""""             """""...       $   . ".         ." .   $    
#        ..""        .   .   .   .   .    ..    $   $$$. ". ... ." .$$$   $    
#      ."    . " . " . " . " . " . " . " .  "" ."  $$$"""  "   "  """$$$  ".   
#    ."      . " . " . " . " . " . " . " .     $  "                    "   $   
#   ."   . " . " . "           "   " . " . "  ."      ...          ...     ".  
#  ."    . " . "    .."""""""""...     " . "  $     .$"              "$.    $  
# ."     . " . " .""     .   .    ""..   . " $ ".      .""$     .""$      ." $ 
#."    " . " .       . " . " . " .    $    " $ "      "  $$    "  $$       " $ 
#$     " . " . " . " . " . " . " . "   $     $             $$.$$             $ 
#$     " . " . " . " . " . " . " . " .  $  " $  " .        $$$$$        . "  $ 
#$     " . " . " . " . " . " . " . " .  $    $      "  ..   "$"   ..  "      $ 
#".    " . " . " . " . " . " . " . "   ."  "  $  . . . $  . .". .  $ . . .  $  
# $    " . " . " . " . " . " . " . "  ."   "            ".."   ".."       
#  $     . " . " . " . " . " . "   .."   . " . "..    "             "    .."   
#  ".      " . " . " . " . " .  .""    " . " .    """$...         ...$"""      
#   ". "..     " . " . " . " .  "........  "    .....  ."""....."""            
#     ". ."$".....                       $..."$"$"."   $".$"... `":....        
#       "".."    $"$"$"$"""$........$"$"$"  ."."."  ...""      ."".    `"".    
#           """.$.$." ."  ."."."    ."."." $.$.$"""".......  ". ". $ ". ". $   
#                  """.$.$.$.$.....$.$.""""               ""..$..$."..$..$."
#

import os
import sys
import urlparse
import urllib
import urllib2
from bs4 import BeautifulSoup

# ONLY EDIT THESE THREE THINGS.
url = 'http://bookre.org/reader?file=1077091&pg='
page_count = 318
out_folder = '/Users/Craig/Desktop/img'
# HALT. DON'T CHANGE ANYTHING BELOW THIS.

def main(url, page_count, out_folder):
    i = 1

    # Grab the doc title
    url_initial = url + '%s' % i
    html_initial = urllib2.urlopen(url_initial)
    soup_initial = BeautifulSoup(html_initial.read())
    title = soup_initial.find('h1', id='srch_wrd')
    title = title.string

    while i <= page_count:
        # Generate the new url
        newurl = url + '%s' % i
        print "Consuming Knowledge on Page", i
        html = urllib2.urlopen(newurl)
        soup = BeautifulSoup(html.read())

        # Grab the page image
        for image in soup.findAll('img', id='page_image', limit=1):
            filename = title + ' ' + 'Pg.' + ' ' +'%s' % i
            outpath = os.path.join(out_folder, filename)
            parsed = list(urlparse.urlparse(newurl))

            if image["src"].lower().startswith("http"):
                urllib.urlretrieve(image["src"], "image.png")
            else:
                new = (parsed[0], parsed[1], image["src"], "", "", "")
                urllib.urlretrieve(urlparse.urlunparse(new), outpath)
        i += 1
    print "ALL KNOWLEDGE CONSUMED"

if __name__ == "__main__":
    if not url.lower().startswith("http"):
        sys.exit(-1)
    main(url, page_count, out_folder)