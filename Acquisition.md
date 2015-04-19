# Introduction #

We need to collect real world acquisition scenarios for each of the four types of supported classes:
  * http://opds-spec.org/acquisition would be a generic acquisition link (useful for free content)
  * http://opds-spec.org/acquisition/buying for content that you can buy
  * http://opds-spec.org/acquisition/lending for content that you can lend
  * http://opds-spec.org/acquisition/subscription for content that you can subscribe to
  * http://opds-spec.org/acquisition/sample for preview content

The following do **not** include a discussion of how the client/user _discovered_ the entry.

# Stories #

## 1 Shelley ##

Shelley has found Semantic Web for the Working Ontologist for $18.99 as a PDF in the Catalog provided by nerdishbooks.com using Reading System X. Nerdish Books allows her to pay via PayPal. Shelley has a PayPal account, so she is sent of to PayPal in a web browser by Reading System X, enters her account information, and returns to Nerdish Books. At this point, the browser receives the PDF content, which is intercepted by Reading System X, added to her library, and displayed for her.

{KHF}

## 2 Hamid ##

Ḥāmid has found How Barack Obama Won in the Catalog provided direct from the publisher, Vintage. He has discovered it using Search Engine Y using the web browser on his laptop. Search Engine Y shows that has three options for purchase, all of which require a credit card:
  * EPUB for $10.99
  * PDF for $10.99
  * EPUB & PDF for $15.99
He selects the EPUB option and his web browser is sent to the Vintage Store web site, where he is prompted to log into his Vintage account or create a new account. He has no Vintage account, so he enters some basic information and his credit card. At this point, he clicks on a "Download" link and saves the EPUB file to his computer.

{KHF}

## 3 Rob ##

Rob is a longtime user of Reading System Z. He needs to get better at singing, so he finds Singing Live: The Performing Skills Guidebook for Contemporary Singers in the default aggregated Catalog provided by Reading System Z. He does not care what the format is (Reading System Z has selected a Mobi file for him), the file (stored by Z), or who the publisher is. Rob has already entered his Google Checkout account information long ago into Reading System Z, which saved it. Z filters Catalog results to exclude titles not available using Google Checkout. Rob is shown a "Read now for $8.99CAD" and happily clicks it (he buys anything he wants--as long as it's less than $10CAD). Seconds later,
he's learning more about singing.

{KHF}

## 4 Valda ##

Valda has found Inherent Vice in Reading System B. Reading System B has an existing partnership with the publisher and offers Valda an EPUB version for $7.99 using PayPal. She enters her PayPal credentials and Reading System B records the transaction (to report to the publisher later). On the backend, Reading System B requests a one-time URL for the content from the publisher (Reading System B doesn't have a copy of their library, they control it). Using this one-time URL, it downloads the EPUB for Valda and loads it into her personal library.

{KHF}

# Walkthroughs #

## 1 Shelley + PayPal (HTML) ##

(For story Shelley #1)

  1. Reading System X and Nerdish Books do an integration of backend systems to get Reading System X established as a trusted partner with the ability to coordinate sales and access secure resources.
  1. The OPDS Catalog from nerdishbooks.com includes the following entry, partially included below
```
 <entry>
   <title>Semantic Web for the Working Ontologist</title>
   <id>urn:nerdishbooks.com:1166</id>
   <dc:identifier>urn:isbn:</dc:identifier>
   <author>
     <name>Dean Allemang</name>
   </author>
   <author>
     <name>James Hendler</name>
   </author>
   <updated>2009-08-12T00:44:20+00:00</updated>
 ...
   <link type="application/pdf"
            href="https://www.nerdishbooks.com/book/1984.pdf"
            rel="http://opds-spec.org/buying">
     <opds:price currencycode="USD">18.99</opds:price>
     <opds:paymentgateway>https://www.paypal.com/us/</opds:paymentgateway>
   </link>
 </entry>
```
  1. Shelley opens Reading System X
  1. Shelley selects "Nerdish Books" from the list of "OPDS Catalogs"
  1. Reading System X does an HTTP GET for the OPDS Catalog endpoint for Nerdish Books at http://nerdishbooks.com/opds.xml (Shelley finds the title above, not covered here)
  1. Reading System X displays the entry (above) to Shelley with a pretty cover image and some descriptive text and a big button that says "Buy PDF using PayPal for $18.99USD!"
  1. Shelley clicks the big button obligingly
  1. Reading System X opens an embedded web browser and POSTs to PayPal the details of the transaction for $18.99USD on Shelley's behalf using Reading System X's PayPal merchant account.
  1. Shelley is presented an HTML PayPal login screen inside Reading System X's browser, logs in, and confirms that she wants to pay the amount
  1. Reading System X does a callback over HTTP to confirm the transaction succeeded
  1. Reading System X now initiates an authenticated HTTPS request with nerdishbooks.com to download the PDF bytes from https://www.nerdishbooks.com/book/1984.pdf.
  1. Reading System X processes the PDF content and loads it into storage
  1. Reading System X displays the PDF to Shelley.

{KHF}