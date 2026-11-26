/* Harmless classroom token, not a malware indicator. */
rule Training_Blue {
    strings:
        $token = "BLUE-TOKEN" ascii fullword
    condition:
        $token
}
