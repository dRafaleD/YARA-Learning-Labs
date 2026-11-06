rule Synthetic_Paired_Indicators {
    meta:
        description = "Educational synthetic marker correlation only"
    strings:
        $a = "LAB-ALPHA-2026" ascii
        $b = "LAB-BETA-2026" ascii
    condition:
        $a and $b
}
