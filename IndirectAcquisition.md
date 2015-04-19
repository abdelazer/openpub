# Introduction #

We've had a lot of discussions about how we could handle indirect acquisition in OPDS. At this point, we all agree that an acquisition link for an indirect acquisition should use "text/html" in its atom:link@type but discussions are still open about how we should list the formats.


# Alternatives #

## Inline dc:format ##

```
<link type="text/html" href="/buy/1" rel="http://opds-spec.org/acquisition/buy">
  <dc:format>application/epub+zip</dc:format>
  <dc:format>application/pdf</dc:format>
  <opds:price currencycode="USD">8.99</opds:price>
</link>
```

Criticism:
  * the semantic is not really good: we can't say that a link is in another format too (dc:format)
  * we can't provide extra metadata for each format or provide a link for such format


## RDF resources ##

```
<link type="text/html" href="/buy/1" rel="http://opds-spec.org/acquisition/buy">
  <opds:price currencycode="USD">8.99</opds:price>
  <dcterms:hasFormat>http://www.website.com/buy/1.epub</dcterms:hasFormat>
  <dcterms:hasFormat>http://www.website.com/buy/1.pdf</dcterms:hasFormat>
  <rdf:Description rdf:about="http://www.website.com/buy/1.epub"> 
    <dc:format>application/epub+zip</dc:format> 
  </rdf:Description> 
  <rdf:Description rdf:about="http://www.website.com/buy/1.pdf"> 
    <dc:format>application/pdf</dc:format> 
  </rdf:Description> 
</link>
```

Criticism:
  * nice semantic and extensibility
  * complex (do we really want RDF in our links ?)
  * requires a URI for each resource, which might be a problem for some catalogs

## Using another inline atom:link ##

```
<link type="text/html" href="/buy/1" rel="http://opds-spec.org/acquisition/buy">
  <opds:price currencycode="USD">8.99</opds:price>
  <link href="http://www.website.com/buy/1.epub" type="application/epub+zip"> 
    <dc:extent>789 kbytes</dc:extent> 
  </link>
  <link href="http://www.website.com/buy/1.pdf" type="application/pdf" /> 
</link>
```

Criticism:
  * could support use cases similar to basic RDF without requirements for another namespace
  * lack of known semantic for atom:link in another atom:link