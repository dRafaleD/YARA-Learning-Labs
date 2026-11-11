// Fictional markers in harmless text; not malware signatures.
rule Synthetic_Any {
    strings:
        $f1 = "BLUE-TOKEN"
        $f2 = "GREEN-TOKEN"
        $f3 = "ORANGE-TOKEN"
    condition:
        1 of ($f*)
}

rule Synthetic_Two {
    strings:
        $f1 = "BLUE-TOKEN"
        $f2 = "GREEN-TOKEN"
        $f3 = "ORANGE-TOKEN"
    condition:
        2 of ($f*)
}

rule Synthetic_All {
    strings:
        $f1 = "BLUE-TOKEN"
        $f2 = "GREEN-TOKEN"
        $f3 = "ORANGE-TOKEN"
    condition:
        all of ($f*)
}
