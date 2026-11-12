/*
 * Harmless training strings only. Not malware signatures.
 * Evaluate with YARA CLI: yara rules.yar sample.txt
 */
rule Training_Any_Token
{
    meta:
        description = "High recall toy rule for harmless colored tokens"
        purpose = "training"
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        any of them
}

rule Training_Both_Tokens
{
    meta:
        description = "Strict toy rule requiring two harmless colored tokens"
        purpose = "training"
    strings:
        $blue = "BLUE-TOKEN" ascii fullword
        $green = "GREEN-TOKEN" ascii fullword
    condition:
        all of them
}
