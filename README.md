**NOTE**: This Action is now deprecated and was replaced by:

- KSP-CKAN/NetKAN-Infra#355
- KSP-CKAN/NetKAN#10608
- KSP-CKAN/KSP2-NetKAN#205

# inflate-netkan

GitHub Action to submit a Netkan to the queue for inflation.
Available for manual triggering in the Actions list.
User can enter the identifier to use.

## Usage

Use this for NetKAN:

```yml
name: Inflate a chosen module
on:
    workflow_dispatch:
        inputs:
            identifier:
                description: Identifier of module to inflate
                required: true
jobs:
    Inflate_module:
        runs-on: ubuntu-latest
        steps:
            - name: Get NetKAN repo
              uses: actions/checkout@v2
              with:
                  path: NetKAN
            - name: Get CKAN-meta repo
              uses: actions/checkout@v2
              with:
                  repository: KSP-CKAN/CKAN-meta
                  path: CKAN-meta
            - name: Manual inflate
              uses: HebaruSan/inflate-netkan@master
              env:
                  AWS_ACCESS_KEY_ID:     ${{ secrets.AWS_ACCESS_KEY_ID     }}
                  AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
                  AWS_DEFAULT_REGION:    ${{ secrets.AWS_DEFAULT_REGION    }}
              with:
                  identifier: ${{ github.event.inputs.identifier }}
                  game id: ksp2
```
