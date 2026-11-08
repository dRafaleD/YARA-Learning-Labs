rule Training_Document_Revision_V1 {
    meta:
        description = "Intentionally broad rule for false-positive teaching"
        category = "synthetic-training-only"
    strings:
        $a = "DOC-ALPHA" ascii
    condition:
        $a and filesize < 1KB
}
