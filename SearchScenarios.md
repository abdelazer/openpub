# Search Standardization #

The ability for OPDS clients/readers to be able to search multiple catalogs in a standardized manner is important.

Here are some scenarios involving search that I think we should tackle. Please help in completing and correcting the examples below!

---


# Simple search #

A client should be able to query a catalog for a for a search term or phrase.

Example: A search for "Mark Twain" will return both titles authored by Mark Twain and titles about Mark Twain. Titles about Mark Twain might include:
  * titles with "Mark Twain" in atom:title
  * titles with "Mark Twain" atom:category
  * titles with "Mark Twain" in the fulltext

Example OpenSearch URL template:
```
<Url template="http://example.com/?q={searchTerms}&amp;page={startPage?}" type="application/atom+xml"/>
```

Catalogs that implement simple OpenSearch:
  * Feedbooks
  * IA

Clients that implement simple OpenSearch:
  * OLPC "Get IA Books" Activity
  * Ibis
  * archive.org [HTML OPDS client](http://www.archive.org/bookserver/catalog/)


---

# Advanced search using SRU in OpenSearch #

  * http://www.crossref.org/CrossTech/2009/06/aligning_opensearch_and_sru.html
  * http://www.nature.com/opensearch/opensearch.xml


---



# Advanced search #

A client should be able to query a catalog for a for a search term or phrase, and further limit the results by a specific metadata term.

Example: A search for "Missouri" AND author:"Mark Twain" should return titles about Missouri written by Mark Twain.

Example query:
```
http://bookserver.archive.org/catalog/opensearch?q=Missouri+AND+creator:Mark+Twain
```


**TODO:** Example OpenSearch URL template.


---


# Advanced search for just bibliographic metadata #

Similar to the above scenario, but no general search term is included.

Example: A search for author:"Mark Twain" should return just titles written by Mark Twain.

Example query:
```
http://bookserver.archive.org/catalog/opensearch?q=creator:Mark+Twain
```

**TODO:** Example OpenSearch URL template


---


# Search restricted by language #
If an OPDS client knows that the user is only interested in titles written specific language, it should be able to automatically restrict the search to just this language.

The [OpenSearch Parameter name reference](http://www.opensearch.org/Specifications/OpenSearch/1.1#Parameter_names) states:
> An OpenSearch description document should include one "Language" element for each language that the search  engine supports. If the search engine also supports queries for any arbitrary language then the OpenSearch description document should include a Language element with a value of "`*`". The "language" template parameter in the OpenSearch URL template can be used to allow the search client to choose among the available languages.

**TODO** Example OpenSearch URL template

Example query
```
http://bookserver.archive.org/aggregator/opensearch?q=language:hi
```

Some catalogs will also support filtering by language using the HTTP 1.1 **Accept-Language** header

---


# Search restricted by format #
If an OPDS client is only able to handle certain kinds of formats, it should be able to query OPDS catalogs for just titles in the formats it can read.

Example: A client application can only read EPUB files, and not PDFs or other ebook formats. It should be able to query for just this kind of format.

Using HTTP 1.1 **Accept:** header
  * for epubs with no drm
    * Accept: application/atom+xml;profile=opds application/epub+zip

Using search args:
```
http://bookserver.archive.org/aggregator/opensearch?q=format:epub
```

**TODO** Example OpenSearch URL template:


---


# Search restricted by drm modality #
If an OPDS client is only able handle certain kinds of DRM, it should be able to query OPDS catalogs for just those titles.

Example: A client application that does not implement the Adobe ACS SDK can only read non-DRM'ed PDFs and EPUBs. It should be able to restrict search results to just these titles that it can read.

Using HTTP 1.1 **Accept:** header
  * for epubs with no drm plus epubs with ACS4 drm.
    * Accept: application/atom+xml;profile=opds application/epub+zip application/epub+zip;drm=http://ns.adobe.com/adept

**TODO** Using search args

**TODO** Example OpenSearch URL template:

---


# Search an aggregator for all titles sold by a particular feed provider #

Example: Search the IA aggregator for all titles sold by O'Reilly.
```
http://bookserver.archive.org/aggregator/opensearch?q=provider:OReilly
```

**TODO:** Add OpenSerach URL template and example. Is this based on atom:source?


---


# Search an aggregator for a particular title sold by a particular feed provider #

Example query:
```
http://bookserver.archive.org/aggregator/opensearch?q=title:perl+AND+provider:OReilly
```

**TODO:** Add OpenSerach URL template


---


# Search for titles from a particular publisher #

Example: Search for all titles published by Samhain.

**TODO:** Add OpenSerach URL template and example