rule Lab18_Broad_Training_Rule : training broad
{
    meta:
        description = "Intentionally broad harmless rule for false-positive discussion"

    strings:
        $common = "error" nocase

    condition:
        $common
}

rule Lab18_Contextual_Training_Rule : training contextual
{
    meta:
        description = "Harmless rule that combines multiple indicators and a size gate"

    strings:
        $marker = "YARA_LAB18_MARKER" ascii
        $component = "training_component=parser" ascii
        $version = /version=[0-9]{1,2}\.[0-9]{1,2}/ ascii

    condition:
        filesize < 64KB and
        $marker and
        $component and
        $version
}

rule Lab18_Threshold_Training_Rule : training threshold
{
    meta:
        description = "Harmless threshold rule for balancing precision and coverage"

    strings:
        $a = "feature_alpha" ascii
        $b = "feature_beta" ascii
        $c = "feature_gamma" ascii
        $d = "feature_delta" ascii

    condition:
        3 of ($a, $b, $c, $d)
}
