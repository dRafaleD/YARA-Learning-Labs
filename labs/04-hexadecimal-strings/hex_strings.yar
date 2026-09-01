rule Hex_Exact_Demo
{
    strings:
        $hex_marker = { 48 45 58 5F 4C 41 42 }

    condition:
        $hex_marker
}

rule Hex_Wildcard_Demo
{
    strings:
        $pattern = { 41 42 ?? 44 45 }

    condition:
        $pattern
}
