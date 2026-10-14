/* Harmless classroom corpus. Matching these rules never implies malware. */
rule Lab20_Broad_Marker : training broad
{
    strings:
        $marker = "LAB20_SIGNAL" ascii
    condition:
        $marker
}

rule Lab20_Contextual_Detection : training contextual
{
    meta:
        purpose = "Combine multiple independent markers for reproducible validation"
    strings:
        $marker = "LAB20_SIGNAL" ascii
        $component = "component=widget" ascii
        $mode = "mode=active" ascii
    condition:
        filesize > 0 and filesize < 4096 and
        $marker and $component and $mode
}
