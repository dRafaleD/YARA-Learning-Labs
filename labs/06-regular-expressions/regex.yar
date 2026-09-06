rule Regex_Demo
{
    meta:
        author = "dRafaleD"
        description = "Harmless practice rule for learning YARA regular expressions"
        lab = "06"
        purpose = "education"

    strings:
        $ticket = /LAB-[0-9]{4}/
        $user = /user_[a-z]{3,8}/ nocase

    condition:
        $ticket and $user
}
