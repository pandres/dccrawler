U.S. Court of Appeals for the D.C. Circuit crawler
==================================================

The script hits a url from the U.S Court of appeals of D.C for the latest opinions. 

The results get stored a *results.json* file. The url has a "count" parameter for the amount of latest opinions, set to constant 10. Note that the count seems to be the amount of rows in the document the site generates, which includes the date as a header row, so those gets substracted from the total.

Usage
-----

Run 
    > python dccrawler.py

