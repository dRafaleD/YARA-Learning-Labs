rule NoCase_Demo
{
    strings:
        $marker = "HELLO_YARA" nocase

    condition:
        $marker
}

rule ASCII_Wide_Demo
{
    strings:
        $marker = "WIDE_MARKER" ascii wide

    condition:
        $marker
}
