```bash
uvicorn main:app --env-file environment.txt --port 8001
```

```bash
pytest --cov-report term-missing --cov=src --log-cli-level=INFO -x
```

query
{
  admissionById(id: "995a0dd2-3697-4e40-ae68-5bc3d9fe8c81") {
    __typename
    id
    stateId
    programId
    paymentInfoId
    
    examStartDate
    applicationStartDate
    applicationLastDate
    conditionDate
    paymentDate
    conditionExtendedDate
    requestConditionExtendDate
    requestExtraConditionsDate
    requestExtraDateDate
    examLastDate
    studentEntryDate
    
    endDate
    program {
      __typename
      id
    }
    paymentInfo {
      __typename
      accountNumber
      specificSymbol
      constantSymbol
      IBAN
      SWIFT
      amount
      payments {
        __typename
        bankUniqueData
        variableSymbol
        studentId
        amount
        
      }
    }
  }
}