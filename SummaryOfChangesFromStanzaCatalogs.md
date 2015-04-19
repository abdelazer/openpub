﻿#summary A summary of changes between Stanza catalogs and the current OPDS draft.
#labels Phase-Support

# Summary of changes between Stanza catalogs and the current OPDS draft. #

This is intended to help people who are migrating legacy catalogs to OPDS.

## Added ##

  * OPDS namespace: `xmlns:opds="http://opds-spec.org/2010/catalog"`

  * Support for full entries

  * Link relation specific to acquisition links: `rel="http://opds-spec.org/acquisition"`

  * Use of profile and type arguments in link elements that point to other OPDS catalogs, e.g.:

```
  <link rel="self"  href="/opds-catalogs/new.xml" type="application/atom+xml;type=feed;profile=opds-
catalog"/>
```


  * Allowance of non-ePub file types, e.g. `type="application/x-mobipocket-ebook"`

  * Addition of `opds:price` element to describe for-pay resources.

## Changes ##

  * New link relations specific to cover image and thumbnails:  `rel="http://opds-spec.org/cover"`,
`rel="http://opds-spec.org/thumbnail"`

## Enhancements ##

  * Recommended use of Dublin Core namespace for metadata such as `dc:publisher`, `dc:language` inside
entries

  * Recommended use of dc:format inside link element:
```
<dc:format>application/x-mobipocket-
ebook</dc:format>
```

  * Specific recommendation to use OpenSearch and OpenSearch descriptors.