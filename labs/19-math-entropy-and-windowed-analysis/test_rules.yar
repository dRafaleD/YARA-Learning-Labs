import "math"

/*
 * Training-only signatures. All sample files are synthetic.
 * High entropy is not a malware verdict.
 */

rule Lab19_HighEntropyFirstWindow : learning entropy
{
    meta:
        description = "A synthetic marker and high-entropy byte window"
        purpose = "Demonstrate math.entropy on an explicit offset and size"
    strings:
        $header = "LAB19_DEMO" ascii
    condition:
        filesize >= 4352 and filesize <= 20KB and
        $header at 0 and
        math.entropy(256, 4096) > 7.5
}

rule Lab19_LowEntropyFirstWindow : learning entropy
{
    meta:
        description = "A synthetic marker followed by repeated bytes"
    strings:
        $header = "LAB19_DEMO" ascii
    condition:
        filesize >= 4352 and filesize <= 20KB and
        $header at 0 and
        math.entropy(256, 4096) < 1.0
}

rule Lab19_HighEntropySecondWindow : learning entropy
{
    meta:
        description = "High entropy in the second window of a mixed file"
    strings:
        $header = "LAB19_DEMO" ascii
    condition:
        filesize >= 8448 and filesize <= 20KB and
        $header at 0 and
        math.entropy(4352, 4096) > 7.5
}
