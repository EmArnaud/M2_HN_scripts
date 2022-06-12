<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:template match="@*|node()">
        <xsl:copy>
            <xsl:apply-templates select="@*|node()"/>
        </xsl:copy>
    </xsl:template>

    <xsl:template match="i">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>
    
    <xsl:template match="CENTER">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>

        <xsl:template match="b">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>

    <xsl:template match="sup">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>

    <xsl:template match="sc">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>

    <xsl:template match="lb">
        <xsl:apply-templates select="@*|node()"/>
    </xsl:template>


    <xsl:template match="pb">
    </xsl:template>

     <xsl:template match="corr">
    </xsl:template>

    <xsl:template match="tt">
    </xsl:template>

    <xsl:template match="blockquote">
    </xsl:template>


    
</xsl:stylesheet>
