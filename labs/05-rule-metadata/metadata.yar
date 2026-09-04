rule Metadata_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA metadata"
        lab = "05"
        purpose = "education"

    strings:
        $marker = "YARA_METADATA_LAB"

    condition:
        $marker
}
