private rule Lab14_Helper_Header
{
    strings:
        $header = "LAB14"
    condition:
        $header at 0
}

private rule Lab14_Helper_Content
{
    strings:
        $a = "alpha"
        $b = "beta"
        $c = "gamma"
    condition:
        2 of them
}

rule Lab14_Composed_Detection
{
    meta:
        description = "Harmless training rule composed from private helper rules"
        purpose = "Practice rule references and modular detection logic"

    condition:
        Lab14_Helper_Header and Lab14_Helper_Content
}
