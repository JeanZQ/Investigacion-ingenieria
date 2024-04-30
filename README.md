# Share information between services

## Architecture Characteristics to prioritize
- **Reliability**
- **Scalability**
- **Data Consistency**
- **Maintainability**

## Context
Gringotts Bank has multiple services that need to share information between them. It has a service who is the owner of personal information about its clients like: Name, addresses, Floo Network ID, etc. The bank has a developer team that constantly needs to access this information to develop new services. The dilemma is how to keep the information updated and consistent between the services.

## Problem to solve
It's required to create a strategy to share information between services. The strategy should be able to handle a large number of updates and provide consistency and handle ambiguity. For example let say that Donald Mcgonagall is moving to a new address. Then he sends an owl to the bank indicating the new address. The goblin on charge update the address in the personal information service. A few seconds later the department of marketing is making a campaign to protect the Forbidden Forest for deforestation. This department has it own service and is consuming data from the personal information service. The department must send the owl to the new address of Mr. Mcgonagall. The bank needs to ensure that the address is updated in all the services.

## Preconditions
- It's required to create at least two services: one who is the owner of the information and another who consumes the information.
- The information needs to be stored in a database. It could be relational or NoSQL.
- Consider failure scenarios like: network failure, database failure, etc.

## Scoring Parameters
| Characteristic | Description | Scoring Criteria |
| --- | --- | --- |
| **Reliability** | The system's ability to consistently share and update information between services. | - High reliability, no data loss: 3 points <br> - Some data loss, but manageable: 2 points <br> - High data loss, system inconsistencies: 1 point |
| **Scalability** | The ability of the system to handle an increasing amount of work. | - Easily scalable: 3 points <br> - Some scalability features, but with limitations: 2 points <br> - Limited scalability, potential issues with increased load: 1 point |
| **Data Consistency** | The degree to which the system ensures that the same data is available across all services. | - High consistency, no data discrepancies: 3 points <br> - Some inconsistencies, but manageable: 2 points <br> - High inconsistencies, data discrepancies: 1 point |
| **Maintainability** | The ease with which the system can be modified to correct faults, improve performance, or adapt to a changed environment. | - Easy to maintain and modify: 3 points <br> - Moderate difficulty in maintenance and modification: 2 points <br> - High difficulty in maintenance and modification: 1 point |
