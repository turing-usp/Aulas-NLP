intents:
- greet
- emergency_ambulance
- emergency_insurance_number
- emergency_fire
- emergency_police
- emergency_road_help
- emergency_air_rescue
- affirm

slots:
  Ambulance:
    type: categorical
    values:
        - ambulance
        - hospital wagon
        - mobile hospital
        - red cross truck
        - sick transport
        - paramedics
        - injuries
        - paramedics station
        - paramedics department
  Insurance:
    type: categorical
    values:
        - allowance
        - insurance number
        - insurance Company
        - assurance Company
        - health insurance number
        - insurance Company number
        - life insurance number
        - medical insurance number
        - insurance agent number
        - car insurance number
        - social insurance number
        - insurance toll-free number
        - coverage
        - guarantee
        - protection
  Fire:
    type: categorical
    values:
        - fire department
        - fire brigade
        - firefighters
        - fire chief
        - fire engine
        - fire protection
        - fire authority
        - fire and rescue service
        - fire station
        - fire investigators
        - firefighters station
        - fireman
        - fire patrol
  Police:
    type: categorical
    values:
        - police
        - boys in blue
        - constabulary
        - fuzz
        - law enforcement
        - police force
        - law 
        - Old Bill
        - police officer
        - FBI
        - policemen
        - policewoman
        - policeman
        - cops
        - officers
        - man
        - authority
        - guard
        - patrolman
        - gendarmerie
        - crime prevention
        - police service
        - police department
        - protective services
        - civil guard
        - civic guard
        - troopers
        - sheriff
        - rangers
        - military police
        - police constable
        - police station
        - riot police
        - secret police
        - district police
        - police authority
        - police captain
        - police car
        - police chief
        - police commissioner
        - police detective
        - police headquarter
        - police inspector
        - police liutenant
        - police raid
        - police sergeant
        - police squad
        - police van
        - police wagon
        - state police
        - public services
        - uniforms
        - police department
        - criminal justice
        - highway patrol
        - law enforcement
        - vigilante
        - public security
        - private police
        - police number
        - blue uniforms
  Road_help:
    type: categorical
    values:
        - tow truck
        - wrecker
        - tow car
        - tow truck driver
        - breakdown van
        - breakdown lorry
        - tow 
        - trailer
        - breakdown truck
        - recovery truck
        - breakdown services
        - truck services
        - breakdown services station
        - breakdown services department
        - tow truck company 
  Air_rescue:
    type: categorical
    values:
        - rega
        - rescue by helicopter
        - air-ambulance
        - emergency response unit
        - flying doctors
        - air-emergency
        - air-help
        - helicopter
        - rescue team by helicopter
        - helicopter paramedics
        - helicopter station
        - air-paramedics
        - hospital helicopter
        - air-ambulance department
        - red cross helicopter
        - emergency helicopter
  
entities:
- Ambulance
- Insurance
- Police
- Fire
- Road_help
- Air_rescue


actions:
- utter_greet
- utter_action_help_ambulance
- utter_action_help_insurance
- utter_action_help_fire
- utter_action_help_police
- utter_action_road_help 
- utter_action_help_air_rescue
- utter_affirm
- __main__.ApiAction

templates:
  utter_greet:
  - text: "Hello, I can offer you assistance on emergency situations, what number are you looking for?"
  utter_action_help_ambulance:
  - text: "The number to call for any type of emergency in Europe is: 112.
          Depending of your country you can call the following numbers: 
          Austria - 144
          Belgium - 100
          Bulgaria - 150
          Croatia - 194
          Cyprus - 199
          Czeckia - 155
          Denmark - 1813
          Estonia - 112
          Finland - 112
          France - 15
          Germany - 112
          Greece - 166
          Hungary - 104
          Ireland - 112 or 999
          Italy - 118
          Latvia - 113
          Lithuania - 112
          Luxembourg - 112
          Malta - 112
          Netherlands - 112
          Poland - 999
          Portugal - 112
          Romania - 112
          Slovakia - 155
          Slovenia - 112
          Spain - 061
          Sweden - 112
          Switzerland - 144
          Unit Kingdom - 112"
  utter_action_help_insurance:
  - text: "-the customer service to call is: 800-899-600
          
          -the car insurance service to call is: 800-899-602
          
          -the life insurance service to call is: 800-899-605
          
          -the health insurance service to call is: 800-899-610" 
  utter_action_help_police:
  - text: "The number to call for any type of emergency in Europe is: 112.
          Depending of your country you can call the following numbers: 
          Austria - 133
          Belgium - 101
          Bulgaria - 166
          Croatia - 192
          Cyprus - 199
          Czeckia - 158
          Denmark - 114
          Estonia - 112
          Finland - 112
          France - 17
          Germany - 110
          Greece - 100
          Hungary - 107
          Ireland - 112 or 999
          Italy - 113
          Latvia - 110
          Lithuania - 112
          Luxembourg - 113
          Malta - 112
          Netherlands - 112
          Poland - 997
          Portugal - 112
          Romania - 112
          Slovakia - 158
          Slovenia - 113
          Spain - 091
          Sweden - 112
          Switzerland - 117
          Unit Kingdom - 112"       
  utter_action_help_fire:
  - text: "The number to call for any type of emergency in Europe is: 112.
          Depending of your country you can call the following numbers: 
          Austria - 122
          Belgium - 100
          Bulgaria - 160
          Croatia - 193
          Cyprus - 199
          Czeckia - 150
          Denmark - 112
          Estonia - 112
          Finland - 112
          France - 18
          Germany - 110
          Greece - 199
          Hungary - 105
          Ireland - 112 or 999
          Italy - 115
          Latvia - 112
          Lithuania - 112
          Luxembourg - 112
          Malta - 112
          Netherlands - 112
          Poland - 998
          Portugal - 112
          Romania - 112
          Slovakia - 150
          Slovenia - 112
          Spain - 080
          Sweden - 112
          Switzerland - 118
          Unit Kingdom - 112"       
  utter_action_road_help:
  - text: "The number to call for any type of emergency in Europe is: 112.
          Depending of your country you can call the following numbers: 
          Austria - 120
          Belgium - +32-25853203
          Bulgaria - +359-70012680
          Croatia - 1987
          Cyprus - +357-22313131
          Czeckia - 1240
          Denmark - 0427-892789
          Estonia - 0330-1591111
          Finland - 0200-8080
          France - +33-3904025-90
          Germany - +49-711530343536
          Greece - 2102443030
          Hungary - 188
          Ireland - 112 or 999
          Italy - 116
          Latvia - 112
          Lithuania - 112
          Luxembourg - 112
          Malta - 112
          Netherlands - 112
          Poland - 112
          Portugal - 112
          Romania - 112
          Slovakia - 112
          Slovenia - 112
          Spain - 112
          Sweden - 112
          Switzerland - 112
          Unit Kingdom - 112"
  utter_action_help_air_rescue:
  - text: "The number to call for any type of emergency in Europe is: 112.
          Depending of your country you can call the following numbers: 
          Austria - 140
          Belgium - 112
          Bulgaria - 1470
          Croatia - 112
          Cyprus - 1441
          Czeckia - 150
          Denmark - 112
          Estonia - +372-6191224
          Finland - 020-211112
          France - +33-556210171
          Germany - 19222
          Greece - 112
          Hungary - 112
          Ireland - 112 or 999
          Italy - 118
          Latvia - 112
          Lithuania - 112
          Luxembourg - 112
          Malta - 112
          Netherlands - 112
          Poland - 112
          Portugal - 112
          Romania - 112
          Slovakia - 112
          Slovenia - 112
          Spain - 112
          Sweden - 112
          Switzerland - 112
          Unit Kingdom - 112"        
  utter_affirm:
  - text: "You're welcome"