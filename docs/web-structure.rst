==================
Web Page Structure
==================


This project scrapes data from `Volume 369
<http://aomol.msa.maryland.gov/000001/000369/html/index.html>`_ from the
Archives of Maryland Online.

**Pages 1 - 145** have the records of interest. Here is `page 1
<http://aomol.msa.maryland.gov/000001/000369/html/am369--1.html>`_ for example.

At the center of each page, there is a box listing slave owners. Under the slave
owners' names are tables of formerly enslaved persons. The pages have different
numbers of owners and enslaved persons, true to the source documents.

In the HTML, these data are in nested tables. The box is a single cell in the
outer table (row 2, cell 1). The owner data and tables of enslaved persons all
reside in this cell, separated by line break elements.

We want to capture each individual owner and the tables of enslaved persons.

The following xpath will identify the components of interest. ::

  Add xpath here.

To get all of the pages, we just need to iterate the page number at the end of
the URL. Alternatively, we could use the "NEXT >>" buttons to navigate from one
page to the next.
