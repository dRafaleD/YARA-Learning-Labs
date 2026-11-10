// Educational labels only. Not a malware detection signature.
rule Synthetic_Document_Pair {
    strings:
        $name = "DOC-CANARY" ascii
        $action = "ACTION-CHECK" ascii
    condition:
        $name and $action
}
