```bash
uvicorn main:app --env-file environment.txt --port 8001
```

http://localhost:8001/voyager

```bash
pytest --cov-report term-missing --cov=src --log-cli-level=INFO -x
```

```gql
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
    disciplines {
      __typename
      id
      name
      minScore
      maxScore
      disciplineTypeId
      type {
        __typename
        id
        name
        name
        description
        descriptionEn
      }
      results {
        __typename
        id
        score
        description
        examPlanedDate
        
        student { id }
        examiner { id }
      }
    }
  }
}
```

```gql
{
	_entities(representations: [{ __typename: "UserGQLModel", id: "15315904-811b-4248-ac96-f670104646d6" }]) {
  	...on UserGQLModel {
      admissionDisciplineResults {
        __typename
        id
        description
        score
        examiner { id }
        disciplineId
        discipline {
          __typename
          id
          name
          minScore
          maxScore
          type {
            id
            name
            description
            weight
            minScore
          }
          admission {
            program { id }
            stateId
          }
        }
      }
    }  
  }
}
```

```gql
{
	_entities(representations: [{ __typename: "UserGQLModel", id: "15315904-811b-4248-ac96-f670104646d6" }]) {
  	...on UserGQLModel {
      admissionDisciplineResults {
        __typename
        id
        description
        score
        examiner { id }
        passed
        discipline {
          __typename
          id
          name
          minScore
          maxScore
          type {
            id
            name
            description
            weight
            minScore
          }
          admission {
            program { id }
            stateId
          }
        }
      }
    	admissions {
        __typename
        id
        state { id }
        program { id }
        disciplines {
          __typename
          name
          minScore
          maxScore
          type {
            __typename
            id
            name
            description
            minScore
            weight
            
          }
        }
      }
    }  
  }
}
```