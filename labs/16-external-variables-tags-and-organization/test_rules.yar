rule Lab16_Tagged_Training_Rule : training linux
{
    meta:
        description = "Harmless rule demonstrating tags and external variables"
        purpose = "Practice rule organization and environment-aware conditions"

    strings:
        $marker = "YARA_LAB16"

    condition:
        $marker and environment == "lab"
}

rule Lab16_Namespace_Style_Grouping : training grouped
{
    meta:
        description = "Harmless grouped rule for organization practice"

    strings:
        $a = "alpha16"
        $b = "beta16"
        $c = "gamma16"

    condition:
        2 of them
}
