rule Lab11_Exact_Marker
{
    meta:
        description = "Matches a harmless training marker"
        purpose = "YARA rule testing practice"

    strings:
        $marker = "YARA_LAB_11_MARKER"

    condition:
        $marker
}

rule Lab11_Two_Indicators
{
    meta:
        description = "Requires two harmless indicators"
        purpose = "Practice positive and negative test cases"

    strings:
        $a = "training-alpha"
        $b = "training-beta"

    condition:
        all of them
}
