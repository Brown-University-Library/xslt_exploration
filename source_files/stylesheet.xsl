<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <!-- Output settings -->
    <xsl:output method="xml" indent="yes"/>

    <!-- Template for the root element -->
    <xsl:template match="/TestEntries">
        <scores>
            <!-- Apply templates for each unique person -->
            <xsl:for-each select="Entry[not(PersonName=preceding::Entry/PersonName)]">
                <xsl:variable name="person" select="PersonName"/>
                <Person>
                    <Name><xsl:value-of select="$person"/></Name>
                    <average>
                        <!-- Calculate the average score for this person -->
                        <xsl:value-of select="format-number(sum(../Entry[PersonName=$person]/TestScore) div count(../Entry[PersonName=$person]), '0.0')"/>
                    </average>
                </Person>
            </xsl:for-each>
        </scores>
    </xsl:template>

</xsl:stylesheet>
