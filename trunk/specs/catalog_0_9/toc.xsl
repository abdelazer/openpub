<?xml version="1.0"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
  <xsl:template match="*">
    <xsl:apply-templates/>
  </xsl:template>
  <xsl:template match="text()">
  </xsl:template>
  <xsl:template match="/">
  <div id="toc">
  <h1 class="nonum">Table of Contents</h1>
  <xsl:apply-templates/>
  </div>
  </xsl:template>
  <xsl:template match="div[div/h1]">
    <ul>
      <xsl:apply-templates/>
    </ul>
  </xsl:template>
  <xsl:template match="div[h1]">
    <xsl:variable name="pid" select="@id"/>
    <xsl:value-of select="pid"/>
    <li>
      <a>
        <xsl:attribute name="href"><xsl:value-of select="concat('#', $pid)"/></xsl:attribute>
        <xsl:value-of select="*[1]"/>
      </a>
    </li>
    <xsl:if test=".//h2">
      <ul>
        <xsl:apply-templates/>
      </ul>
    </xsl:if>
  </xsl:template>
  <xsl:template match="div[h2]">
    <xsl:variable name="pid" select="@id"/>
    <xsl:value-of select="pid"/>
    <li>
      <a>
        <xsl:attribute name="href"><xsl:value-of select="concat('#', $pid)"/></xsl:attribute>
        <xsl:value-of select="*[1]"/>
      </a>
    </li>
    <xsl:if test=".//h3">
      <ul>
        <xsl:apply-templates/>
      </ul>
    </xsl:if>
  </xsl:template>
  <xsl:template match="div[h3]">
    <xsl:variable name="pid" select="@id"/>
    <xsl:value-of select="pid"/>
    <li>
      <a>
        <xsl:attribute name="href"><xsl:value-of select="concat('#', $pid)"/></xsl:attribute>
        <xsl:value-of select="*[1]"/>
      </a>
    </li>
    <xsl:if test=".//h4">
      <ul>
        <xsl:apply-templates/>
      </ul>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
