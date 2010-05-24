<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="h1[not(@class='nonum')]">
    <xsl:copy>
      <xsl:number level="any" count="h1[not(@class='nonum')]"/>
      <xsl:text>. </xsl:text>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="h2">
    <xsl:copy>
      <xsl:number level="any" count="h1[not(@class='nonum')]"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h1" count="h2"/>
      <xsl:text>. </xsl:text>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="h3">
    <xsl:copy>
      <xsl:number level="any" count="h1[not(@class='nonum')]"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h1" count="h2"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h2" count="h3"/>
      <xsl:text>. </xsl:text>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
  <xsl:template match="h4">
    <xsl:copy>
      <xsl:number level="any" count="h1[not(@class='nonum')]"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h1" count="h2"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h2" count="h3"/>
      <xsl:text>.</xsl:text>
      <xsl:number level="any" from="h3" count="h4"/>
      <xsl:text>. </xsl:text>
      <xsl:value-of select="."/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
