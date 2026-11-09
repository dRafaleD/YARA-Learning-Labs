// Harmless document-marker examples; no malware signatures.
rule Synthetic_Broad {
    strings:
        $marker = "TEST-CANARY" ascii
    condition:
        $marker
}

rule Synthetic_Strict {
    strings:
        $marker = "TEST-CANARY" ascii
        $action = "ACTION-CHECK" ascii
    condition:
        $marker and $action
}
