# Absences

    GET **rest/v1/students/{studentId}/absences/details**

## Description
Get a list of the student's events, like absences and lates

## Required Header
* Z-Dev-ApiKey
* Z-Auth-Token
* User-Agent: zorro/1.0
* Z-Auth-Token: token

## Parameters
- **studentId** _(required)_ — your student id obtained with the login

# Response
```json
{
    "events": [
        {
            "evtId": 1065236,
            "evtCode": "ABR1",
            "evtDate": "2021-10-11",
            "evtHPos": null,
            "evtValue": null,
            "isJustified": true,
            "justifReasonCode": "",
            "justifReasonDesc": "Ritardo Breve",
            "hoursAbsence": []
        },
        {
              "evtId": 1637569,
              "evtCode": "ABR1",
              "evtDate": "2021-10-23",
              "evtHPos": null,
              "evtValue": null,
              "isJustified": true,
              "justifReasonCode": "",
              "justifReasonDesc": "Ritardo Breve",
              "hoursAbsence": []
        },
        {
              "evtId": 2511592,
              "evtCode": "ABU0",
              "evtDate": "2021-11-15",
              "evtHPos": 5,
              "evtValue": 1,
              "isJustified": true,
              "justifReasonCode": "A",
              "justifReasonDesc": "Motivi di salute",
              "hoursAbsence": []
        },
        {
              "evtId": 5149031,
              "evtCode": "ABA0",
              "evtDate": "2022-01-22",
              "evtHPos": null,
              "evtValue": null,
              "isJustified": true,
              "justifReasonCode": "A",
              "justifReasonDesc": "Motivi di salute",
              "hoursAbsence": []
        },
        {
              "evtId": 7086768,
              "evtCode": "ABA0",
              "evtDate": "2022-01-31",
              "evtHPos": null,
              "evtValue": null,
              "isJustified": true,
              "justifReasonCode": "C",
              "justifReasonDesc": "Altri motivi",
              "hoursAbsence": [
                  {
                      "hPos": 2,
                      "subject": "DISEGNO E STORIA DELL\"ARTE"
                  },
                  {
                      "hPos": 3,
                      "subject": "SCIENZE NATURALI"
                  },
                  {
                      "hPos": 4,
                      "subject": "FILOSOFIA"
                  },
                  {
                      "hPos": 5,
                      "subject": "MATEMATICA"
                  },
                  {
                      "hPos": 6,
                      "subject": "LINGUA E CULTURA STRANIERA (INGLESE)"
                  }
              ]
        },
        {
              "evtId": 8951323,
              "evtCode": "ABA0",
              "evtDate": "2022-04-21",
              "evtHPos": null,
              "evtValue": null,
              "isJustified": true,
              "justifReasonCode": "A",
              "justifReasonDesc": "Motivi di salute",
              "hoursAbsence": []
        },
        {
              "evtId": 10166045,
              "evtCode": "ABU0",
              "evtDate": "2022-05-21",
              "evtHPos": 3,
              "evtValue": null,
              "isJustified": false,
              "justifReasonCode": null,
              "justifReasonDesc": null,
              "hoursAbsence": []
        }
    ]
}
```
