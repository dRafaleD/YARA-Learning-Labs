include "helpers.yar"

rule Lab17_Composed_From_Include : training modular
{
    meta:
        description = "Harmless rule composed from included helper rules"
        purpose = "Practice YARA include files and multi-file rule organization"

    condition:
        Lab17_Helper_Training_Header and
        Lab17_Helper_Two_Markers
}
