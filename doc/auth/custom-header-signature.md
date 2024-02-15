
# Custom Header Signature



Documentation for accessing and setting credentials for apiHeader.

## Auth Credentials

| Name | Type | Description | Getter |
|  --- | --- | --- | --- |
| token | `str` | - | `token` |
| api-key | `str` | - | `api_key` |



**Note:** Auth credentials can be set using `ApiHeaderCredentials` object, passed in as named parameter `api_header_credentials` in the client initialization.

## Usage Example

### Client Initialization

You must provide credentials in the client as shown in the following code snippet.

```python
client = MultiauthsampleClient(
    api_header_credentials=ApiHeaderCredentials(
        token='token',
        api_key='api-key'
    )
)
```


