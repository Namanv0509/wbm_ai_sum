schema_cdx_data = {
    "name": "fetch_cdx_data",
    "description": "Fetch CDX data from the Wayback Machine for a given URL",
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL to fetch the CDX data for",
            },
            "match_type": {
                "type": "string",
                "description": "The type of URL match",
                "enum": ["exact", "prefix", "host", "domain"],
            },
            "limit": {
                "type": "integer",
                "description": "The maximum number of results to return",
            },
            "fields": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of specific fields to return",
            },
            "filters": {
                "type": "array",
                "items": {"type": "string"},
                "description": "A list of filters to apply",
            },
            "from_timestamp": {
                "type": "string",
                "description": "Start timestamp for filtering",
            },
            "to_timestamp": {
                "type": "string",
                "description": "End timestamp for filtering",
            },
        },
        "required": ["url"],
    },
}

schema_fetch_data = {
    "name": "fetch_and_extract_text",
    "description": "Fetch HTML content from a URL and extract relevant metadata",
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL to fetch the HTML content from",
            },
        },
        "required": ["url"],
    },
}

schema_trend_analysis = {
    "name": "get_trend_analysis",
    "description": "Get trend analysis for a URL, including resilience, fixity, and chaos metrics",
    "parameters": {
        "type": "object",
        "properties": {"url": {"type": "string", "description": "The URL to analyze"}},
        "required": ["url"],
    },
}

function_schemas = [schema_cdx_data, schema_fetch_data, schema_trend_analysis]
