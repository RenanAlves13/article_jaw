# Results

This folder contains the input and/or output data used by `analise.py`.

## Expected structure

```
Results/
  deepseck_results/
    <project>/
      zero-*.csv
      few-*.csv
  openai_results/
    <project>/
      zero-*.csv
      few-*.csv
```

## CSV file rules

Each CSV file must contain the columns:

- `Microservice`
- `Responsibilities`
- `Communicates With`

The separator for multiple services in the **Communicates With** column is `;` by default (configurable in `analise.py`).

## Tips

- Keep consistent project names between `deepseck_results/` and `openai_results/`.
- Files that do not start with `zero-` or `few-` will not be processed.
