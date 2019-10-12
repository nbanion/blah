Slave Statistics of St. Mary's County
=====================================

__This project creates a database of enslaved persons and slave owners__ from
records in the Maryland State Archives. The database is a snapshot of slavery
just prior to abolition in Maryland. The data might help historians explore:

- How many enslaved persons and slave owners were there?
- What was the demographic makeup of enslaved persons?
- How were slave holdings distributed among slave owners?
- When did enslaved persons leave bondage? Any patterns?
- What can we find out about individuals or families?

## Background

American historians study slavery to better understand both the past and the
present. They use archival records to reconstruct the history of slavery.

These old, physical documents are difficult to analyze at scale. Many are hand-
written, and they can be very fragile. Archivists often digitize these documents
and post searchable text online, but it can still be difficult to assemble these
online records into tidy datasets for analysis.

With web scraping and data processing techniques, we can overcome these
challenges and expose old data to modern visualization and analysis techniques.

## Source Material

This dataset comes from [Volume 369](http://aomol.msa.maryland.gov/megafile/msa/speccol/sc2900/sc2908/000001/000369/html/index.html)
of the Archives of Maryland series at the Maryland State Archives. This volume
compiles records from former slave owners who wished to be compensated for their
human property after emancipation in Maryland. Pages 1-145 list the slave owners
and the enslaved persons that they owned, as well as some background including
sex, age, and date of emancipation.

> _Slave Statistics of St. Mary's County Maryland 1864_
>
> Agnes Callum

To create the searchable online records, the Maryland State Archives scans each
page of the source material and uses programs to convert the images to text and
ultimately HTML. Their site includes more [technical details](http://aomol.msa.maryland.gov/megafile/msa/speccol/sc2900/sc2908/html/about.html).

The online version of this volume includes PDFs for the scanned source material,
which can be useful for catching issues with the digitized records.

## Outcome

The primary outcome is a database of enslaved persons and slave owners. The
database schema is organized as follows:

__Enslaved Persons__

|var          |type|description       |
|-------------|----|------------------|
|id (pk)      |num |unique ID.        |
|int_id(fk)   |num |Interview ID.     |
|fname        |char|First name.       |
|lname        |char|Last name.        |
|sex          |char|Sex (M/F).        |
|age          |num |Age in years.     |
|edate        |date|Emancipation date.|

__Slave Owners__

|var       |type|description  |
|----------|----|-------------|
|id (pk)   |num |Unique ID.   |
|int_id(fk)|num |Interview ID.|
|title     |char|Title.       |
|fname     |char|First name.  |
|lname     |char|Last name.   |
|suffix    |char|Suffix.      |

__Interviews__

|var     |type|description                              |
|--------|----|-----------------------------------------|
|idate   |date|Interview date.                          |
|enslaved|num |Number of enslaved persons (as recorded).|

Secondary outcomes might include:

- A user interface for querying the database.
- An exploratory analysis of the database.
- An interactive data visualization app.

## Approach
Coming soon.

## Project Organization
Coming soon.
