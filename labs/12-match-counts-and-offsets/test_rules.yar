rule Lab12_Offset_And_Occurrence
{
    meta:
        description = "Harmless training rule for offsets and match counts"
        purpose = "Practice @, # and positional conditions"

    strings:
        $marker = "YARA12"
        $tag = "training"

    condition:
        $marker at 0 and #tag >= 2
}

rule Lab12_First_Match_Position
{
    strings:
        $word = "position"

    condition:
        $word and @word[1] < 64
}
