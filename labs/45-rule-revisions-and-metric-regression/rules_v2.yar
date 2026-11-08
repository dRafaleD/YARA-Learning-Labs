rule Training_Document_Revision_V2 {
    meta:
        description = "Correlated markers for controlled regression"
        category = "synthetic-training-only"
    strings:
        $a = "DOC-ALPHA" ascii
        $b = "ACTION-VERIFY" ascii
    condition:
        $a and $b and filesize < 1KB
}
