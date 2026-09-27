rule Lab13_String_Sets
{
    meta:
        description = "Harmless training rule for string sets"
        purpose = "Practice of, prefixes, and grouped indicators"

    strings:
        $net_1 = "network-alpha"
        $net_2 = "network-beta"
        $net_3 = "network-gamma"

        $file_1 = "file-one"
        $file_2 = "file-two"

    condition:
        2 of ($net_*) and any of ($file_*)
}

rule Lab13_Threshold
{
    strings:
        $indicator_1 = "lab13-alpha"
        $indicator_2 = "lab13-beta"
        $indicator_3 = "lab13-gamma"
        $indicator_4 = "lab13-delta"

    condition:
        3 of ($indicator_*)
}
