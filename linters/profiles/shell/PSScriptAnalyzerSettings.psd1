@{
    # Keep the analyzer's default of all severities, including ParseError.
    IncludeRules = @('*')
    Rules = @{
        PSUseConsistentIndentation = @{
            Enable = $true
            Kind = 'space'
            IndentationSize = 4
        }
        PSUseConsistentWhitespace = @{
            Enable = $true
        }
    }
}
